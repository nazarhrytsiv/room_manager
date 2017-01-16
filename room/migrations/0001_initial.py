# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-16 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=10)),
                ('desription', models.TextField()),
                ('size', models.IntegerField()),
            ],
        ),
    ]
