# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-03 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailId', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]