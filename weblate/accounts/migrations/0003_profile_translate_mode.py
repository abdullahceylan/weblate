# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-04 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='translate_mode',
            field=models.IntegerField(choices=[(0, 'Full editor'), (1, 'Zen mode')], default=0, verbose_name='Translation editor mode'),
        ),
    ]
