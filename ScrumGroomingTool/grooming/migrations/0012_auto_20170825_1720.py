# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grooming', '0011_auto_20170825_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atddcase',
            name='suitename',
            field=models.CharField(default='', max_length=200, verbose_name='Suitename'),
        ),
    ]