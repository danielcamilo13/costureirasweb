# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-29 04:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_remove_abatimento_total_desconto'),
    ]

    operations = [
        migrations.AddField(
            model_name='abatimento',
            name='dt_faturado',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 12, 29, 4, 7, 33, 68205, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='abatimento',
            name='faturado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
