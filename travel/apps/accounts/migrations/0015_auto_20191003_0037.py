# Generated by Django 2.1.12 on 2019-10-03 04:37

import apps.accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20191003_0033'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
    ]
