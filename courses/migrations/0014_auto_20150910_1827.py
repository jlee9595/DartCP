# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20150910_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='department',
            new_name='dept',
        ),
    ]
