# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_course_wcs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='WCs',
            new_name='WC',
        ),
    ]
