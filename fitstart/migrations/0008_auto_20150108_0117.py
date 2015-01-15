# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0007_challenge_workout'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='reps_one',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workout',
            name='reps_three',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workout',
            name='reps_two',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
