# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-07 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summerforprogress', '0003_auto_20170807_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='representative',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]