# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'pendding'), (1, b'accept'), (2, b'cancel'), (3, b'completed')]),
        ),
    ]
