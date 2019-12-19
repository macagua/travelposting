# Generated by Django 2.1.15 on 2019-12-19 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0010_auto_20191022_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=300)),
                ('ip_client', models.GenericIPAddressField(blank=True, null=True, verbose_name='Address IP')),
            ],
        ),
    ]