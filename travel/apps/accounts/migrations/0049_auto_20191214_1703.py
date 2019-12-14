# Generated by Django 2.1.12 on 2019-12-14 21:03

import apps.accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0048_auto_20191213_0831'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='customeruser',
            name='about_me',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='About me'),
        ),
    ]
