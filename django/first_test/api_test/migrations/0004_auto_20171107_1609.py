# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0003_auto_20171107_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_time',
            field=models.BigIntegerField(default=0),
        ),
    ]
