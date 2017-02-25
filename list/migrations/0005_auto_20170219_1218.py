# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_auto_20170219_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='plist',
            name='price',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plist',
            name='quantity',
            field=models.IntegerField(default=454),
            preserve_default=False,
        ),
    ]
