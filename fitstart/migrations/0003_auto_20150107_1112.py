# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0002_auto_20150107_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.CharField(null=True, default=None, max_length=50),
            preserve_default=True,
        ),
    ]
