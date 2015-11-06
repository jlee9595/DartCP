# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20150910_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='number',
            new_name='num',
        ),
    ]
