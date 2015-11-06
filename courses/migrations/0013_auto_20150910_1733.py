# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20150910_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='enrollment',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='limit',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='number',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='section',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
    ]
