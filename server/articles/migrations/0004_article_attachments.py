# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
        ('articles', '0003_auto_20170128_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='files.Attachment'),
        ),
    ]
