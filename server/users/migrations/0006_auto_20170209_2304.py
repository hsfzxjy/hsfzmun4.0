# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 15:04
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_lang_code'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('i18n_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]