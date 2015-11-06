# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20150827_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, to='courses.Dept'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prof',
            field=models.ManyToManyField(blank=True, to='courses.Prof', null=True),
        ),
    ]
