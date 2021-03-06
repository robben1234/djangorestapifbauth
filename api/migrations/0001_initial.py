# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('long_position', models.DecimalField(decimal_places=3, max_digits=8)),
                ('lat_position', models.DecimalField(decimal_places=3, max_digits=8)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='places')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
