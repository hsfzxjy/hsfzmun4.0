# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 11:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20170211_1918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discussion',
            options={'verbose_name': '讨论组', 'verbose_name_plural': '讨论组'},
        ),
        migrations.AlterField(
            model_name='discussion',
            name='members',
            field=models.ManyToManyField(related_name='discussions', to=settings.AUTH_USER_MODEL, verbose_name='成员'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='名称'),
        ),
    ]
