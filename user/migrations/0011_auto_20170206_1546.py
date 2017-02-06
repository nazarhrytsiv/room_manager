# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-06 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20170206_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.CharField(max_length=620),
        ),
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Group'),
        ),
    ]
