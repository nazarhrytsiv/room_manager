# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-06 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20170206_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
