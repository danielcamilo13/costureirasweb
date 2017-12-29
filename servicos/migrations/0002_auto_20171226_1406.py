# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-26 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='abatimento',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('servicos.servicos',),
        ),
        migrations.CreateModel(
            name='servico',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('servicos.servicos',),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='num_ficha',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='quantidadedesconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='total1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='totaldesconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='valor1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='servicos',
            name='valorunitariodesconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
