# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-01 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instameals', '0010_order_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pickup_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]