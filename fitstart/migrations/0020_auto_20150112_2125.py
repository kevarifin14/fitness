# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0019_auto_20150112_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='start_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_date',
        ),
    ]
