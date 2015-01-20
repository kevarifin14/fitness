# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0024_auto_20150119_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
