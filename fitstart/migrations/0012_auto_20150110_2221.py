# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0011_exercisetype_exercise_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisetype',
            name='exercise_class',
            field=models.CharField(max_length=2, blank=True, null=True, default=None),
            preserve_default=True,
        ),
    ]
