# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-02 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20171202_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='colecao',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='colecao',
            name='colecao',
            field=models.CharField(max_length=90, primary_key=True),
        ),
    ]