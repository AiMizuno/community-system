# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-29 08:38
from __future__ import unicode_literals

import control.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0008_auto_20170428_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('create_time', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='act_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='act_name',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='inform',
            old_name='accepter',
            new_name='acceptor',
        ),
        migrations.RemoveField(
            model_name='applyfor',
            name='assoc',
        ),
        migrations.RemoveField(
            model_name='applyfor',
            name='member',
        ),
        migrations.RemoveField(
            model_name='community',
            name='asc_id',
        ),
        migrations.RemoveField(
            model_name='community',
            name='asc_name',
        ),
        migrations.RemoveField(
            model_name='passage',
            name='finished',
        ),
        migrations.RemoveField(
            model_name='passage',
            name='writer',
        ),
        migrations.AddField(
            model_name='activity',
            name='author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='community',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='control.Community'),
        ),
        migrations.AddField(
            model_name='activity',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='applyfor',
            name='community',
            field=models.ForeignKey(default=None, on_delete=control.models.Community, related_name='applyfor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='community',
            name='introduction',
            field=models.CharField(default='', max_length=100, verbose_name='简介'),
        ),
        migrations.AddField(
            model_name='community',
            name='members',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='inform',
            name='sender',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mememberof',
            name='community',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='control.Community'),
        ),
        migrations.AddField(
            model_name='mememberof',
            name='member',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='passage',
            name='author',
            field=models.ManyToManyField(related_name='publish_psg', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='passage',
            name='community',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='control.Community'),
        ),
        migrations.AddField(
            model_name='passage',
            name='create_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='birthdate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='loginkey',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='major',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='applyfor',
            name='apply_time',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='community',
            name='establish_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='passage',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='author',
            field=models.ManyToManyField(related_name='publish_notice', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notice',
            name='community',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='control.Community'),
        ),
    ]