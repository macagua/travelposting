# Generated by Django 2.1.12 on 2019-10-07 18:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0019_destinationrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_destinie', django.contrib.gis.db.models.fields.PointField(help_text='To generate the map for your location', srid=4326)),
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='destinations.Destination', verbose_name='Destino')),
            ],
        ),
    ]
