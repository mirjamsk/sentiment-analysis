# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 17:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0022_commentspam_spam_api1_ol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentspam',
            old_name='spam_api1',
            new_name='spam_api1_with_comment_author',
        ),
    ]
