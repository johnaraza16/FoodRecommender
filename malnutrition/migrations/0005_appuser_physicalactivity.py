# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-06 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malnutrition', '0004_food_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='physicalactivity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
