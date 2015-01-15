# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0022_remove_event_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='timed_five',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='timed_four',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='timed_one',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='timed_six',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='timed_three',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workout',
            name='timed_two',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
    ]
