# Generated by Django 2.1.12 on 2019-10-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0024_destinationmap_description_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='number_of_reservations',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
