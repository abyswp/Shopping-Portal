# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('specs', models.TextField()),
                ('unit_price', models.IntegerField()),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], default='Choose Availability Status', max_length=15)),
                ('category', models.CharField(choices=[('Stationary', 'Stationary'), ('Confectionary', 'Confectionary'), ('Garments', 'Garments')], default='Choose Category', max_length=20)),
                ('item_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
