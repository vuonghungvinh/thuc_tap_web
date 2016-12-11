# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=11)),
                ('note', models.CharField(default=b'', max_length=200)),
                ('adult', models.IntegerField(max_length=2)),
                ('children', models.IntegerField(max_length=2)),
                ('total', models.FloatField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListCustomer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('date', models.DateField(null=True, blank=True)),
                ('gender', models.BooleanField(choices=[(True, b'Male'), (False, b'Female')])),
                ('address', models.CharField(max_length=200)),
                ('type_customer', models.BooleanField(choices=[(True, b'Adult'), (False, b'Children')])),
                ('cost', models.FloatField(default=0)),
                ('booking', models.ForeignKey(related_name='list_booking', to='booking.Booking')),
            ],
        ),
    ]
