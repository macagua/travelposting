# Generated by Django 2.1.11 on 2019-09-14 11:14

import apps.destinations.fields
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Badges',
                'verbose_name_plural': 'Badge',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='BookingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('days', apps.destinations.fields.DaysCommaField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], default=[], max_length=14, null=True, verbose_name='Días')),
                ('number_ticket', models.IntegerField(blank=True, null=True, verbose_name='Number of tickets per tour')),
                ('special_price_currency', djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('special_price', djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0'), max_digits=19, verbose_name='Special price')),
                ('mode', models.CharField(choices=[('default', 'Week days'), ('exact-dates', 'Exact dates')], default='default', max_length=50, verbose_name='Mode')),
                ('is_active', models.CharField(choices=[('0', 'No'), ('1', 'Yes')], default='0', max_length=3, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'Booking detail',
                'verbose_name_plural': 'Booking details',
                'ordering': ('start_date', 'end_date'),
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='name')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Short description')),
                ('description', models.TextField(blank=True, default='\n<strong>Ingrese su título aquí...</strong><br><br>\n\n<p> <b>Ingrese aquí su texto...</b></p>\n\n<!--more--><br><br>\n\n<p> <b>Ingrese más información aquí...</b></p>\n\n<!--more--><br><br>\n\n<strong>Quienes somos</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<strong>Misión</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<table class="table table-bordered tours-tabs__table" style="width: 100%px;">\n<tbody>\n<tr>\n <td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>\n <td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>\n <td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>INCLUIDO [icon_tick state="on"] </strong></td>\n <td style="width: 574.233px;">\n  <b>Ingrese aquí lo que va incluido en el paquete como una lista...</b>\n  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>\n </td>\n</tr>\n<tr>\n <td style="width: 213px;"><strong>NO INCLUIDO [icon_tick state="off"] </strong></td>\n <td style="width: 574.233px;">\n  <b>Ingrese aquí lo que no va incluido en el paquete como una lista...</b>\n  <ul><li><b><br></b></li><li><b><br></b></li><li><b><br></b></li></ul>\n </td>\n</tr>\n</tbody>\n</table>\n', null=True, verbose_name='description')),
                ('is_deleted', models.BooleanField(default=False, editable=False, verbose_name='is_deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Destino',
                'verbose_name_plural': 'Destinos',
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='DestinationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('var', models.BooleanField(default=False, verbose_name='Variable tour')),
                ('virtual', models.BooleanField(default=False, verbose_name='Virtual')),
                ('descargable', models.BooleanField(default=False, verbose_name='Descargable')),
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='destinations.Destination', verbose_name='Destino')),
            ],
            options={
                'verbose_name': 'Detalle del destino',
                'verbose_name_plural': 'Detalles del destino',
            },
        ),
        migrations.CreateModel(
            name='GeneralDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_price_currency', djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('regular_price', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), max_digits=19, verbose_name='Precio normal')),
                ('sale_price_currency', djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('USD', 'USD $')], default='USD', editable=False, max_length=3)),
                ('sale_price', djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0'), max_digits=19, verbose_name='Precio rebajado')),
                ('date_on_sale_from', models.DateField(blank=True, null=True, verbose_name='Fecha de rebaja inicial')),
                ('date_on_sale_to', models.DateField(blank=True, null=True, verbose_name='Fecha de rebaja final')),
                ('status_imp', models.CharField(choices=[('imponible', 'Imponible'), ('envio', 'Envio solamente'), ('ninguno', 'Ninguno')], default='imponible', max_length=50, verbose_name='Estado del impuesto')),
                ('class_imp', models.CharField(choices=[('estandar', 'Estandar'), ('reduced', 'Reduced Rate'), ('zero', 'Zero Rate')], default='estandar', max_length=50, verbose_name='Clase de impuesto')),
                ('destination_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='general', to='destinations.DestinationDetail', verbose_name='Detalle del destino')),
            ],
            options={
                'verbose_name': 'Detalle general',
                'verbose_name_plural': 'Detalles generales',
            },
        ),
        migrations.CreateModel(
            name='HeaderSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_mode', models.CharField(choices=[('hide', 'Default'), ('banner', 'Imagen'), ('slider', 'Slider'), ('from_list', 'From list')], default='hide', max_length=15, verbose_name='Display mode')),
                ('subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Subtitle')),
                ('image', models.ImageField(blank=True, null=True, upload_to='header/images', verbose_name='Imagen')),
                ('parallax', models.BooleanField(default=True, verbose_name='Parallax')),
                ('image_repeat', models.CharField(blank=True, choices=[('repeat', 'Repeat'), ('no-repeat', 'No repeat'), ('repeat-x', 'Repeat horizontally'), ('repeat-y', 'Repeat vertically')], max_length=150, null=True, verbose_name='Imagen repeat')),
                ('mask', models.CharField(blank=True, choices=[('default', 'Default')], max_length=120, null=True, verbose_name='Mask')),
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='header', to='destinations.Destination', verbose_name='Destino')),
            ],
            options={
                'verbose_name': 'Sección del encabezado',
                'verbose_name_plural': 'Secciones del encabezado',
            },
        ),
        migrations.CreateModel(
            name='InventarioDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=60, verbose_name='SKU')),
                ('manager', models.BooleanField(default=False, help_text='Activa la gestión de inventario por cada producto', verbose_name='¿Gestión de inventario?')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Cantidad de inventario')),
                ('reserva', models.CharField(choices=[('no', 'No permitir'), ('notify', 'Permitir, pero se avisara al cliente'), ('yes', 'Permitir')], default='no', max_length=50, verbose_name='¿Permitir reservas?')),
                ('umb_exist', models.IntegerField(blank=True, default=0, null=True, verbose_name='Umbral de pocas existencias')),
                ('sold_individually', models.BooleanField(default=False, help_text='Activa esto para permitir que solo se pueda comprar uno de estos artículos en cada pedido', verbose_name='Vendido individualmente')),
                ('destination_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='destinations.DestinationDetail', verbose_name='Detalle del destino')),
            ],
            options={
                'verbose_name': 'Detalle de inventario',
                'verbose_name_plural': 'Detalles de inventario',
            },
        ),
        migrations.CreateModel(
            name='OptionTabData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('template', models.TextField(blank=True, null=True, verbose_name='Plantilla')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Opción de la tab',
                'verbose_name_plural': 'Opciones de las tabs',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre')),
                ('sort', models.IntegerField(blank=True, null=True, verbose_name='Sort')),
                ('description', models.TextField(blank=True, default='Sin comentario', null=True, verbose_name='Descripción')),
                ('thumbnail', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='gallery/thumbnail/', verbose_name='Thumbnail')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery/image/', verbose_name='Imagen')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='destinations.Destination', verbose_name='Destino')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
                'ordering': ('sort', 'name'),
            },
        ),
        migrations.CreateModel(
            name='TabData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('option_tab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_tab', to='destinations.OptionTabData', verbose_name='Option tab')),
            ],
            options={
                'verbose_name': 'Tab',
                'verbose_name_plural': 'Tabs',
                'ordering': ('option_tab',),
            },
        ),
        migrations.CreateModel(
            name='TourData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge', models.CharField(blank=True, choices=[('1', 'Ultimo minuto'), ('2', 'Deal del Mes'), ('3', 'FamTrip'), ('4', 'Congresos'), ('5', 'Eventos'), ('6', 'Hotel'), ('7', 'Movilidad'), ('8', 'Ocio +')], max_length=150, null=True, verbose_name='Badge')),
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tour', to='destinations.Destination', verbose_name='Destino')),
            ],
            options={
                'verbose_name': 'Tour',
                'verbose_name_plural': 'Tours',
            },
        ),
        migrations.AddField(
            model_name='tabdata',
            name='tour_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tab', to='destinations.TourData', verbose_name='Tour'),
        ),
        migrations.AddField(
            model_name='bookingdetail',
            name='destination_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='destinations.DestinationDetail', verbose_name='Detalle del destino'),
        ),
    ]