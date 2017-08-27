# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-02 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DnsRecord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='minimum',
            field=models.IntegerField(blank=True, default=None, help_text='Minimum time for SOA record(default TTL)', null=True, verbose_name='minimum'),
        ),
    ]