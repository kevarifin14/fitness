# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0005_challenge'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='reps',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
