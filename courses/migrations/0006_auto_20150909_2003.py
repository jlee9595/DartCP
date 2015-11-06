# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20150903_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
