# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0009_auto_20150109_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='exercise_three',
            field=models.ForeignKey(related_name='three', blank=True, null=True, default=None, to='fitstart.Exercise'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='reps_three',
            field=models.PositiveSmallIntegerField(blank=True, null=True, default=0),
            preserve_default=True,
        ),
    ]
