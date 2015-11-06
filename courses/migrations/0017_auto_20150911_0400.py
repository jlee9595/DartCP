# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_auto_20150910_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='num',
            new_name='number',
        ),
    ]
