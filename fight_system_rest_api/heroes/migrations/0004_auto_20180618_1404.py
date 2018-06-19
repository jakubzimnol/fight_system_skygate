# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0003_auto_20180618_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='big_plant',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='big_plant',
            name='group',
        ),
        migrations.RemoveField(
            model_name='dragon',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='dragon',
            name='group',
        ),
        migrations.RemoveField(
            model_name='humanoid',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='humanoid',
            name='group',
        ),
        migrations.RemoveField(
            model_name='insect',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='insect',
            name='group',
        ),
        migrations.RemoveField(
            model_name='mamal',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='mamal',
            name='group',
        ),
        migrations.RemoveField(
            model_name='reptile',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='reptile',
            name='group',
        ),
        migrations.RemoveField(
            model_name='rodent',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='rodent',
            name='group',
        ),
        migrations.AddField(
            model_name='hero',
            name='breed',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AddField(
            model_name='hero',
            name='group',
            field=models.CharField(default='', max_length=2),
        ),
    ]
