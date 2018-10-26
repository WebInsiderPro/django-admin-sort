# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-26 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_another_anotherone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='another',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='anotherone',
            name='another_field',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Note2'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='chapterextrazero',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='another_field',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Note2'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='note',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='one_more',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Note3 (simulating tabular inlines)'),
        ),
        migrations.AlterField(
            model_name='notesextrazero',
            name='another_field',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Note2'),
        ),
        migrations.AlterField(
            model_name='sortablebook',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
    ]
