# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0006_exercise_reps'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='workout',
            field=models.ForeignKey(to='fitstart.Workout', default=None),
            preserve_default=True,
        ),
    ]
