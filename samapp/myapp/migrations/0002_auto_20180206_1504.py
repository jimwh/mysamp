# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-06 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_mod_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='university',
            name='last_mod_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='auth.Group'),
        ),
    ]
