# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-12-27 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='abatimento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ds_desconto', models.CharField(blank=True, max_length=90)),
                ('dt_entrada', models.DateField(blank=True)),
                ('dt_saida', models.DateField(blank=True)),
                ('qte_desconto', models.IntegerField(blank=True, default=0)),
                ('vr_unitario_desconto', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('total_desconto', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_desconto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ds_desconto', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='abatimento',
            name='desconto',
            field=models.ForeignKey(max_length=15, on_delete=django.db.models.deletion.CASCADE, to='cadastro.tipo_desconto'),
        ),
        migrations.AddField(
            model_name='abatimento',
            name='nm_costureira',
            field=models.ForeignKey(blank=True, max_length=40, on_delete=django.db.models.deletion.CASCADE, to='cadastro.costureira'),
        ),
    ]
