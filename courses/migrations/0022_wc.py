# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_auto_20150915_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='WC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('abbrv', models.CharField(unique=True, max_length=10)),
            ],
        ),
    ]
