# Generated by Django 2.1.15 on 2020-01-04 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_auto_20200103_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('sent_at', models.DateTimeField(blank=True, null=True, verbose_name='sent at')),
                ('read_at', models.DateTimeField(blank=True, null=True, verbose_name='read at')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_dm', to=settings.AUTH_USER_MODEL, verbose_name='Recipient')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_dm', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
        ),
    ]
