# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-17 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_products_pimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='pImage',
            field=models.ImageField(default='/media', upload_to='api/static/images/'),
        ),
    ]
