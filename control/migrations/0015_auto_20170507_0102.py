# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 17:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0014_auto_20170506_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.Activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='applyfor',
            name='community',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='applyfor', to='control.Community'),
        ),
    ]