# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='exercise_one',
            field=models.ForeignKey(default=None, null=True, related_name='one', to='fitstart.Exercise'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise_three',
            field=models.ForeignKey(default=None, null=True, related_name='three', to='fitstart.Exercise'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='exercise_two',
            field=models.ForeignKey(default=None, null=True, related_name='two', to='fitstart.Exercise'),
            preserve_default=True,
        ),
    ]
