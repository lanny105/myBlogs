# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20170305_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='visit',
            field=models.IntegerField(default=0),
        ),
    ]
