# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms
import profile.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.BooleanField(choices=[(True, 'Male'), (False, 'Female')])),
                ('date', models.DateField(null=True, blank=True)),
                ('avatar', django_resized.forms.ResizedImageField(upload_to=profile.models.get_upload_file_user_profile)),
                ('phone', models.CharField(default='', max_length=15)),
                ('address', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(related_name='profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
