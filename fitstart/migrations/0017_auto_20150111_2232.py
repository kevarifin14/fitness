# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0016_auto_20150111_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='reps_five',
            field=models.PositiveSmallIntegerField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='reps_four',
            field=models.PositiveSmallIntegerField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='reps_one',
            field=models.PositiveSmallIntegerField(default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='reps_six',
            field=models.PositiveSmallIntegerField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='reps_three',
            field=models.PositiveSmallIntegerField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='reps_two',
            field=models.PositiveSmallIntegerField(default=None),
            preserve_default=True,
        ),
    ]
