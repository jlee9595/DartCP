# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20150901_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='prof',
            new_name='profs',
        ),
        migrations.AlterField(
            model_name='prof',
            name='dept',
            field=models.ForeignKey(null=True, blank=True, to='courses.Dept'),
        ),
    ]
