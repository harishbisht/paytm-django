# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytmhistory',
            name='RESPMSG',
            field=models.TextField(max_length=250, verbose_name=b'RESP MSG'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNDATE',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'TXN DATE'),
        ),
    ]
