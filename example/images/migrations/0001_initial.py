# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-01 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('url', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
