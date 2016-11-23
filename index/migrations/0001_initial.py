# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms
import index.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sliderhome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', django_resized.forms.ResizedImageField(upload_to=index.models.get_upload_file_name)),
                ('title', models.CharField(default=b'', max_length=40, null=True, blank=True)),
                ('isshow', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'name tuor', max_length=100)),
                ('photo', django_resized.forms.ResizedImageField(upload_to=index.models.get_upload_file_name1)),
                ('cost', models.FloatField()),
                ('days', models.PositiveIntegerField()),
                ('is_sale', models.BooleanField(default=False)),
                ('cost_sale', models.FloatField(default=0, null=True, blank=True)),
                ('date', models.DateField()),
                ('inside', models.BooleanField(default=True)),
            ],
        ),
    ]
