# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-06 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20170206_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(),
        ),
    ]
