# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-29 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0006_auto_20171229_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='finalizado',
            field=models.BooleanField(),
        ),
    ]