# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-09 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('npbapi', '0002_pastscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='league',
            field=models.CharField(default='-', max_length=2),
            preserve_default=False,
        ),
    ]
