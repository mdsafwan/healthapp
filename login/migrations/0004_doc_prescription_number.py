# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-19 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20160219_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc_prescription',
            name='Number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
