# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_auto_20150915_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='limit',
            field=models.CharField(max_length=100, default='-'),
        ),
    ]
