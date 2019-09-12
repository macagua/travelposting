import logging

from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from easy_thumbnails.files import get_thumbnailer
from rest_framework import status, filters, pagination
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.api import serializers
from apps.destinations.models import Photo


logger = logging.getLogger(__name__)


class DestinationViewSet(ModelViewSet):
    serializer_class = serializers.DestinationSerializer
    queryset = serializers.Destination.objects.all()
    serializer_photo_class = serializers.PhotoWithDestinationSerializer
    pagination_class = pagination.PageNumberPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('user__username', 'name', 'description')
    ordering_fields = ('user', 'name')
    filterset_fields = ('name', 'user')

    @action(detail=True, methods=['get'], permission_classes=[AllowAny])
    def gallery(self, request, pk=None):
        obj = self.get_object()
        queryset = obj.gallery.all()
        serializer = self.serializer_photo_class(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path="gallery/create", permission_classes=[AllowAny])
    def gallery_create(self, request, pk=None):
        data = request.data.copy()
        data['destination'] = pk
        data.setdefault('sort', 999)
        name = f"{data['image'].name}.{data['image'].content_type.split('/')[1]}"
        data['image'].name = name
        data.setdefault('name', name.split('.')[0])
        data.setdefault('thumbnail', get_thumbnailer(
            data['image'],
            f"{name.split('.')[0]}_thumbnail.{data['image'].content_type.split('/')[1]}"))
        serializer = self.serializer_photo_class(data=data)

        if serializer.is_valid():
            self.perform_create(serializer)

            results = {
                'status': True,
                'statusText': 'success',
                'model': serializer.data
            }
            status_code = status.HTTP_201_CREATED
        else:
            results = {
                'status': False,
                'statusText': ', '.join([f"{k}: {v}" for k, v in serializer.errors.items()])
            }
            status_code = status.HTTP_200_OK
        headers = self.get_success_headers(serializer.data)
        return Response(results, status=status_code, headers=headers)

    @action(detail=True, methods=['post', 'put', 'patch'], url_path="gallery/update", permission_classes=[AllowAny])
    def gallery_update(self, request, pk=None):
        id = request.POST.get('id')

        try:
            instance = Photo.objects.get(pk=id)
        except Photo.DoesNotExist:
            raise Http404()

        serializer = self.serializer_photo_class(instance, data=request.data, partial=True)

        data = {
            'status': serializer.is_valid(),
            'statusText': ','.join(
                [f"{k}: {v}" for k, v in serializer.errors.items()]) if serializer.errors else 'success',
        }
        self.perform_update(serializer)
        data.update({'model': serializer.data})
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post', 'delete'], url_path='gallery/delete', permission_classes=[AllowAny])
    def gallery_delete(self, request, pk=None):
        id = request.POST.get('id')

        try:
            instance = Photo.objects.get(pk=id)
        except Photo.DoesNotExist:
            raise Http404()

        self.perform_destroy(instance)
        data = {
            'status': True,
            'statusText': 'success'
        }
        return Response(data, status=status.HTTP_200_OK)