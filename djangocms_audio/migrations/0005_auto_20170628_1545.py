# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_audio', '0004_auto_20170628_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='audio_file',
            field=filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='File', blank=True, to='filer.File', null=True),
        ),
    ]
