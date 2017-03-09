# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaytmHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ORDERID', models.CharField(max_length=30, verbose_name=b'ORDER ID')),
                ('TXNDATE', models.DateTimeField(default=datetime.datetime(2017, 3, 9, 12, 32, 37, 79976), verbose_name=b'TXN DATE')),
                ('TXNID', models.IntegerField(verbose_name=b'TXN ID')),
                ('BANKTXNID', models.IntegerField(null=True, verbose_name=b'BANK TXN ID', blank=True)),
                ('BANKNAME', models.CharField(max_length=50, null=True, verbose_name=b'BANK NAME', blank=True)),
                ('RESPCODE', models.IntegerField(verbose_name=b'RESP CODE')),
                ('PAYMENTMODE', models.CharField(max_length=10, null=True, verbose_name=b'PAYMENT MODE', blank=True)),
                ('CURRENCY', models.CharField(max_length=4, null=True, verbose_name=b'CURRENCY', blank=True)),
                ('GATEWAYNAME', models.CharField(max_length=30, null=True, verbose_name=b'GATEWAY NAME', blank=True)),
                ('MID', models.CharField(max_length=40)),
                ('RESPMSG', models.CharField(max_length=250, verbose_name=b'RESP MSG')),
                ('TXNAMOUNT', models.FloatField(verbose_name=b'TXN AMOUNT')),
                ('STATUS', models.CharField(max_length=12, verbose_name=b'STATUS')),
                ('user', models.ForeignKey(related_name='rel_payment_paytm', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
