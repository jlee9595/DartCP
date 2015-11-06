# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20150909_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='abbrv',
            field=models.CharField(unique=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='dept',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
