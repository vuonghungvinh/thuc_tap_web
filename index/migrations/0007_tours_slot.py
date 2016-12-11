# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20161210_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='tours',
            name='slot',
            field=models.IntegerField(default=5),
        ),
    ]
