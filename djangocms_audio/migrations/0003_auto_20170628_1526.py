# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_audio', '0002_auto_20160825_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='text_instrumentation',
            field=models.TextField(verbose_name='Instrumentation', blank=True),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='text_length',
            field=models.TextField(verbose_name='Length', blank=True),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='text_year',
            field=models.TextField(verbose_name='Year', blank=True),
        ),
    ]
