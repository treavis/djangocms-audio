# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_audio', '0003_auto_20170628_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='text_description',
            field=djangocms_text_ckeditor.fields.HTMLField(verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='text_instrumentation',
            field=models.CharField(max_length=255, verbose_name='Instrumentation', blank=True),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='text_length',
            field=models.CharField(max_length=255, verbose_name='Length', blank=True),
        ),
        migrations.AlterField(
            model_name='audiofile',
            name='text_year',
            field=models.CharField(max_length=255, verbose_name='Year', blank=True),
        ),
    ]
