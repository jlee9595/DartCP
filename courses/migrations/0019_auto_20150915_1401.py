# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20150911_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='enrollment',
            field=models.CharField(max_length=100, default='-'),
        ),
    ]
