# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150901_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prof',
            field=models.ManyToManyField(to='courses.Prof', blank=True),
        ),
    ]
