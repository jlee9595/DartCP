# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20150910_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='terms',
        ),
        migrations.AddField(
            model_name='course',
            name='building',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='enrollment',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='limit',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='room',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='section',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='term',
            field=models.ForeignKey(blank=True, to='courses.Term', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='CRN',
            field=models.CharField(max_length=10, blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='course',
            name='period',
            field=models.ForeignKey(blank=True, to='courses.Period', null=True),
        ),
    ]
