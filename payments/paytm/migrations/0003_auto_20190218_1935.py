# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0002_auto_20170309_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytmhistory',
            name='BANKNAME',
            field=models.CharField(verbose_name='BANK NAME', max_length=50, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='BANKTXNID',
            field=models.IntegerField(verbose_name='BANK TXN ID', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='CURRENCY',
            field=models.CharField(verbose_name='CURRENCY', max_length=4, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='GATEWAYNAME',
            field=models.CharField(verbose_name='GATEWAY NAME', max_length=30, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='ORDERID',
            field=models.CharField(verbose_name='ORDER ID', max_length=30),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='PAYMENTMODE',
            field=models.CharField(verbose_name='PAYMENT MODE', max_length=10, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='RESPCODE',
            field=models.IntegerField(verbose_name='RESP CODE'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='RESPMSG',
            field=models.TextField(verbose_name='RESP MSG', max_length=250),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='STATUS',
            field=models.CharField(verbose_name='STATUS', max_length=12),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNAMOUNT',
            field=models.FloatField(verbose_name='TXN AMOUNT'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNDATE',
            field=models.DateTimeField(verbose_name='TXN DATE', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNID',
            field=models.IntegerField(verbose_name='TXN ID'),
        ),
    ]
