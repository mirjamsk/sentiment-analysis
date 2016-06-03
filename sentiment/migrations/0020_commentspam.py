# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0019_auto_20160531_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentSpam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('spam_api1', jsonfield.fields.JSONField(default=b'{"type": "", "is_spam": false}')),
                ('idcomment', models.OneToOneField(db_column='idcommento', on_delete=django.db.models.deletion.CASCADE, related_name='comment_spam', to='sentiment.Comment')),
            ],
            options={
                'db_table': 'im_commento_spam',
                'managed': True,
            },
        ),
    ]
