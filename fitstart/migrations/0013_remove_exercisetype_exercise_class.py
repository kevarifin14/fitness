# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0012_auto_20150110_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisetype',
            name='exercise_class',
        ),
    ]
