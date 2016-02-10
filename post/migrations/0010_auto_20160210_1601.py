# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-10 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_auto_20160120_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-post_date'], 'verbose_name': 'Посты', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='tags',
        ),
    ]
