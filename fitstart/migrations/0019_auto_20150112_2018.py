# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0018_auto_20150111_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True, blank=True)),
                ('workout', models.ForeignKey(to='fitstart.Workout')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='workout',
            name='timed_one',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
