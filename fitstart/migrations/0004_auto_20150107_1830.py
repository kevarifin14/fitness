# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0003_auto_20150107_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_type',
            field=models.ForeignKey(to='fitstart.ExerciseType'),
            preserve_default=True,
        ),
    ]
