# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-29 01:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_delete_abatimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicosReview',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('servicos.servicos',),
        ),
    ]