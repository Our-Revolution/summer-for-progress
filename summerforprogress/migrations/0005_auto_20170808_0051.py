# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-08 00:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summerforprogress', '0004_representative_last_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='representative',
            old_name='workers_rights',
            new_name='wall_street',
        ),
    ]
