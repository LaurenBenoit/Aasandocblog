# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 16:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='added_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='history',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='specialization',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='verified_date',
        ),
    ]
