# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0015_auto_20150110_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='exercise_five',
            field=models.ForeignKey(related_name='five', null=True, to='fitstart.Exercise', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_four',
            field=models.ForeignKey(related_name='four', null=True, to='fitstart.Exercise', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workout',
            name='exercise_six',
            field=models.ForeignKey(related_name='six', blank=True, null=True, to='fitstart.Exercise', default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workout',
            name='reps_five',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workout',
            name='reps_four',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workout',
            name='reps_six',
            field=models.PositiveSmallIntegerField(blank=True, null=True, default=0),
            preserve_default=True,
        ),
    ]
