# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 03:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='IDnum',
            new_name='DDnum',
        ),
    ]
