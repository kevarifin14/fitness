# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0023_auto_20150113_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateField(default=datetime.datetime(2015, 1, 19, 15, 57, 59, 605314)),
            preserve_default=True,
        ),
    ]
