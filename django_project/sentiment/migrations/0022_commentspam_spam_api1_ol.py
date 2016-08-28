# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 17:00
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0021_commentspam_spam_api1_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentspam',
            name='spam_api1_ol',
            field=jsonfield.fields.JSONField(default=b'{"type": "", "is_spam": false}'),
        ),
    ]