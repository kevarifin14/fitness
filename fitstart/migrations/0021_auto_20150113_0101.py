# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0020_auto_20150112_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='start',
        ),
        migrations.AddField(
            model_name='event',
            name='end',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
