# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0006_user_isadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='placed',
            field=models.IntegerField(default=0),
        ),
    ]
