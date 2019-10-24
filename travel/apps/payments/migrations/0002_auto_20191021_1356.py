# Generated by Django 2.1.12 on 2019-10-21 17:56

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='price',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=8, null=True, verbose_name='Precio'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('USD', 'USD $')], default='USD', editable=False, max_length=3),
        ),
    ]