# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20150909_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('abbrv', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='terms',
            field=models.ManyToManyField(to='courses.Term', blank=True),
        ),
    ]
