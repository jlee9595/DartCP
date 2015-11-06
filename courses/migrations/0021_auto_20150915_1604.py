# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20150915_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distrib',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('abbrv', models.CharField(unique=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='distribs',
            field=models.ManyToManyField(blank=True, to='courses.Distrib'),
        ),
    ]
