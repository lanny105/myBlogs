# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 07:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2017, 3, 5, 7, 17, 30, 615763, tzinfo=utc))),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
