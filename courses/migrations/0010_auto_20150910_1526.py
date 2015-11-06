# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_prof_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='fullname',
            field=models.CharField(blank=True, unique=True, max_length=50),
        ),
    ]
