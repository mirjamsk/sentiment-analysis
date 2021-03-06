# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-03 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0006_auto_20160403_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentsentiment',
            old_name='sentiment',
            new_name='sentiment_api1',
        ),
        migrations.RenameField(
            model_name='postsentiment',
            old_name='sentiment',
            new_name='sentiment_api1',
        ),
        migrations.RemoveField(
            model_name='commentsentiment',
            name='idpost',
        ),
        migrations.AlterField(
            model_name='postsentiment',
            name='idpost',
            field=models.OneToOneField(db_column='idpost', on_delete=django.db.models.deletion.CASCADE, related_name='post_sentiment', to='sentiment.Post'),
        ),
    ]
