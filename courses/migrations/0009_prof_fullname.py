# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20150909_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='fullname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
