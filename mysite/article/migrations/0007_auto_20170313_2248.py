# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 05:48
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20170313_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='temp/img/'),
        ),
    ]
