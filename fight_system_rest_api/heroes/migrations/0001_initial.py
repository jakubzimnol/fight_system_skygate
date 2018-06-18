# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('kind', models.CharField(choices=[('B', 'Big creature'), ('M', 'Medium creature'), ('S', 'Small creature')], default='Big creature', max_length=50)),
                ('dead', models.BooleanField(default=False)),
                ('date_of_dead', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='fight',
            name='loser_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='looser', to='heroes.Hero'),
        ),
        migrations.AddField(
            model_name='fight',
            name='winner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='heroes.Hero'),
        ),
    ]
