# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-03 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0002_commentsentiment_postsentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsentiment',
            name='idcomment',
            field=models.ForeignKey(db_column='idcommento', on_delete=django.db.models.deletion.CASCADE, to='sentiment.Comment', unique=True),
        ),
        migrations.AlterField(
            model_name='postsentiment',
            name='idpost',
            field=models.ForeignKey(db_column='idpost', on_delete=django.db.models.deletion.CASCADE, to='sentiment.Post', unique=True),
        ),
    ]