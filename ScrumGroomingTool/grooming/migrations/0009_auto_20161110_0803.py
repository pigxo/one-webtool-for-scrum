# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-10 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grooming', '0008_auto_20161109_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='grooming',
            name='feature',
            field=models.CharField(default='RAN-', max_length=200, verbose_name='Feature'),
        ),
        migrations.AlterField(
            model_name='grooming',
            name='sprint',
            field=models.CharField(default='Sprint', max_length=200, verbose_name='Sprint'),
        ),
    ]
