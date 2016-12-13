# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_tours_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtour',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Please describe your tour here', max_length=8000),
        ),
    ]
