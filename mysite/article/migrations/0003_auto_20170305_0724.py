# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170305_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
