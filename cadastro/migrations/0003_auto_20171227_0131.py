# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-27 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20171227_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abatimento',
            name='desconto',
            field=models.ForeignKey(max_length=40, on_delete=django.db.models.deletion.CASCADE, to='cadastro.tipo_desconto'),
        ),
    ]
