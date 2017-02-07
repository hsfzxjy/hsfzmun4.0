# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_auto_20170130_1809'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ('has_read', '-created')},
        ),
        migrations.AddField(
            model_name='notice',
            name='keyword',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]