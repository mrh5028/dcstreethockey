# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-01 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0010_auto_20170228_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roster',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='roster',
            name='last_name',
        ),
        migrations.AddField(
            model_name='roster',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='leagues.Player'),
        ),
    ]
