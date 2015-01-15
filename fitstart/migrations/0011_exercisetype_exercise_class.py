# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0010_auto_20150109_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisetype',
            name='exercise_class',
            field=models.CharField(max_length=2, default=None),
            preserve_default=True,
        ),
    ]
