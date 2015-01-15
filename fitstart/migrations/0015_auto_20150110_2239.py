# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0014_exercisetype_exercise_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisetype',
            name='exercise_class',
            field=models.CharField(blank=True, max_length=10, default=None, null=True),
            preserve_default=True,
        ),
    ]
