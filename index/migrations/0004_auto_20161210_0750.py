# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_detailtour'),
    ]

    operations = [
        migrations.AddField(
            model_name='tours',
            name='child',
            field=models.FloatField(default=80),
        ),
        migrations.AddField(
            model_name='tours',
            name='isopen',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='detailtour',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Please describe your tour here', max_length=5000),
        ),
    ]
