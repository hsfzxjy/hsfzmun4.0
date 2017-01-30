# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 10:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_article_attachments'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='mentions',
            field=models.ManyToManyField(related_name='mentioned_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]