# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_tours_startaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='child',
            field=models.FloatField(default=50),
        ),
    ]
