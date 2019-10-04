from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from apps.landing_page.views import (
    CommmunityView,
    CategoriesView,
    DetailDestinationView,
    SaveSearchView,
    DeleteRegisterView,
    PrivacySettingView,
)

from apps.destinations.views import BookingSaveView

admin.autodiscover()

urlpatterns = [
    url(
        r'^sitemap\.xml$',
        sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}},
    ),

    url(
        r'^rosetta/',
        include('rosetta.urls'),
    ),

    path(
        'api/',
        include('apps.api.urls', namespace='api'),
    ),
]

urlpatterns += i18n_patterns(
    url(
        r'^nested_admin/',
        include('nested_admin.urls'),
    ),

    url(
        r'^admin/',
        admin.site.urls,
    ),

    url(
        r'^impersonate/',
        include('impersonate.urls'),
    ),

    path(
        'summernote/',
        include('django_summernote.urls'),
    ),

    url(
        r'^accounts/',
        include("apps.accounts.urls", namespace='accounts'),
    ),

    url(
        r'^community',
        CommmunityView.as_view(),
    ),
    url(
        r'^category/destination/(?P<slug>\w+)',
        DetailDestinationView.as_view(),
        name='view_detail_destination',
    ),

    url(
        r'^category/(?P<alias>\w+)',
        CategoriesView.as_view(),
        name='view_category',
    ),

    path(
        'paypal/',
            include('apps.payments.paypal.urls'),
    ),

    path(
        'destinations/',
        include("apps.destinations.urls", namespace='destinations'),
    ),

    path(
        'personal-search/',
        SaveSearchView.as_view(),
        name='personal-search',
    ),

    path(
        'make-booking/',
        BookingSaveView.as_view(),
        name='make-booking',
    ),

    path(
        'delete-register/',
        DeleteRegisterView.as_view(),
        name='delete-register',
    ),

    path(
        'setting-privacy/',
        PrivacySettingView.as_view(),
        name='setting-privacy',
    ),

    

    url(
        r'^',
        include('cms.urls'),
        name='index',
    ),


)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
