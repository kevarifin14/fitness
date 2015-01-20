# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitstart', '0025_auto_20150119_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('quotation', models.CharField(max_length=500)),
                ('author', models.CharField(blank=True, null=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
