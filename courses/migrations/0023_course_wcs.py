# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_wc'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='WCs',
            field=models.ForeignKey(to='courses.WC', null=True, blank=True),
        ),
    ]
