# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-05 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kokowalk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]