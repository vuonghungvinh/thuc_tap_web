# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20161210_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='tours',
            name='startaddress',
            field=models.CharField(default='Ho Chi Minh', max_length=100),
        ),
    ]
