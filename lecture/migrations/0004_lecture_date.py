# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 11:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_auto_20170228_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 1, 11, 22, 40, 91000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
