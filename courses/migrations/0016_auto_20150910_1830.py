# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20150910_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='building',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='room',
            field=models.CharField(null=True, blank=True, max_length=100),
        ),
    ]
