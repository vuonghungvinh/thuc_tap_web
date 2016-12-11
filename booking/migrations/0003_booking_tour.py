# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_tours_slot'),
        ('booking', '0002_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='tour',
            field=models.ForeignKey(related_name='booking_tour', default=0, to='index.Tours'),
        ),
    ]
