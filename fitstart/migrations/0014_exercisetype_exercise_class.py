# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0013_remove_exercisetype_exercise_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisetype',
            name='exercise_class',
            field=models.CharField(null=True, blank=True, default=None, max_length=2),
            preserve_default=True,
        ),
    ]
