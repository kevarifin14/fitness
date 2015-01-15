# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0008_auto_20150108_0117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='description',
            new_name='goal',
        ),
    ]
