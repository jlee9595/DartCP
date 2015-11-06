# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20150910_1652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='dept',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='num',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='profs',
            new_name='professors',
        ),
    ]
