# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('num', models.PositiveSmallIntegerField(null=True)),
                ('CRN', models.CharField(max_length=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('abbrv', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dept', models.ForeignKey(null=True, to='courses.Dept')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(null=True, to='courses.Dept'),
        ),
        migrations.AddField(
            model_name='course',
            name='prof',
            field=models.ManyToManyField(null=True, to='courses.Prof'),
        ),
    ]
