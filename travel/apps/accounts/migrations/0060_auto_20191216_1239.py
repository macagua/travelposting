# Generated by Django 2.1.12 on 2019-12-16 16:39

import apps.accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0059_auto_20191216_1239'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customeruser',
            managers=[
                ('objects', apps.accounts.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
    ]
