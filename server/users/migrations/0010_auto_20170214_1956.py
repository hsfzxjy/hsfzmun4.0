# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lang_code',
            field=models.CharField(default='all', max_length=10),
        ),
    ]
