# Generated by Django 2.1.12 on 2019-10-16 04:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('destinations', '0028_auto_20191015_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=models.TextField(blank=True, default='\n<strong>Quienes somos</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<strong>Misión</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<table class="table table-bordered tours-tabs__table" style="width: 100%px;">\n<tbody>\n<tr>\n<td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>\n<td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>\n</tr>\n</tbody>\n</table>\n', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='description_de',
            field=models.TextField(blank=True, default='\n<strong>Quienes somos</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<strong>Misión</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<table class="table table-bordered tours-tabs__table" style="width: 100%px;">\n<tbody>\n<tr>\n<td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>\n<td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>\n</tr>\n</tbody>\n</table>\n', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='description_en',
            field=models.TextField(blank=True, default='\n<strong>Quienes somos</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<strong>Misión</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<table class="table table-bordered tours-tabs__table" style="width: 100%px;">\n<tbody>\n<tr>\n<td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>\n<td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>\n</tr>\n</tbody>\n</table>\n', null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='description_es',
            field=models.TextField(blank=True, default='\n<strong>Quienes somos</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<strong>Misión</strong><br><br>\n\n<p><b>Por favor ingrese aquí su texto...</b></p><br><br>\n\n<table class="table table-bordered tours-tabs__table" style="width: 100%px;">\n<tbody>\n<tr>\n<td style="width: 213px;"><strong>SALIDA / RETORNO</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la salida...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>HORA DE SALIDA</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la hora de salida...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>HORA DE LLEGADA</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí la hora de llegada...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>NR. DE TOUR PARA RESERVAS</strong></td>\n<td style="width: 574.233px;"><b>Ingrese aquí el nro de tour...</b></td>\n</tr>\n<tr>\n<td style="width: 213px;"><strong>TRASLADO DESDE </strong></td>\n<td style="width: 574.233px;"><strong><b>Ingrese aquí el traslado...</b></strong></td>\n</tr>\n</tbody>\n</table>\n', null=True, verbose_name='description'),
        ),
        migrations.AlterUniqueTogether(
            name='destination',
            unique_together={('user', 'name')},
        ),
    ]
