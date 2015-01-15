# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('exercise_name', models.CharField(max_length=50)),
                ('exercise_type', models.CharField(max_length=50, default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, default=None)),
                ('exercise_one', models.ForeignKey(to='fitstart.Exercise', related_name='one', default=None)),
                ('exercise_three', models.ForeignKey(to='fitstart.Exercise', related_name='three', default=None)),
                ('exercise_two', models.ForeignKey(to='fitstart.Exercise', related_name='two', default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
