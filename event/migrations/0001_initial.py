# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-24 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_name', models.CharField(max_length=200)),
                ('subscription_email', models.CharField(max_length=200)),
                ('subscription_datetime', models.DateTimeField(verbose_name='subscription date and time')),
            ],
        ),
    ]
