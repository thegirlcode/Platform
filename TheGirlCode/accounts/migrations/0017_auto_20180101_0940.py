# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-01 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20180101_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='answer_4_3',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='answer_4_3_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='answer_4_1',
            field=models.IntegerField(default=0),
        ),
    ]
