# Generated by Django 2.1.11 on 2020-08-29 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0050_auto_20200825_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),

    ]