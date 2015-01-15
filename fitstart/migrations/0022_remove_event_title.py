# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0021_auto_20150113_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
    ]
