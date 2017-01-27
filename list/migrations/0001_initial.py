# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('cbname', models.CharField(max_length=15)),
                ('cbid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bill_date', models.DateTimeField(verbose_name='date of purchase')),
                ('bill_time', models.DateTimeField(verbose_name='time of purchase')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_name', models.CharField(max_length=20)),
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pname', models.CharField(max_length=30)),
                ('product_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('quantity', models.FloatField()),
                ('product_type', models.CharField(max_length=20)),
                ('brand_name', models.CharField(max_length=20)),
                ('expiry', models.FloatField()),
                ('effective_price', models.FloatField()),
                ('mrp', models.FloatField()),
                ('vat', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('adm_no', models.IntegerField(primary_key=True, serialize=False)),
                ('phone_no', models.IntegerField()),
                ('cbid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Batch')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='adm_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.User'),
        ),
        migrations.AddField(
            model_name='bill',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Product'),
        ),
        migrations.AddField(
            model_name='batch',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Course'),
        ),
    ]
