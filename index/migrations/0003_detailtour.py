# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20161103_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailTour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo1', django_resized.forms.ResizedImageField(upload_to=index.models.get_upload_file_name_tour_slider)),
                ('photo2', django_resized.forms.ResizedImageField(upload_to=index.models.get_upload_file_name_tour_slider)),
                ('photo3', django_resized.forms.ResizedImageField(upload_to=index.models.get_upload_file_name_tour_slider)),
                ('photo4', django_resized.forms.ResizedImageField(upload_to=index.models.get_upload_file_name_tour_slider)),
                ('detail', models.TextField(default='Please describe your tour here', max_length=5000)),
                ('programmer', models.TextField(default='Please describe your programmer here', max_length=1000)),
                ('local_highlight', models.TextField(default='Please describe your local highlights here', max_length=1000)),
                ('tour', models.OneToOneField(related_name='tour', to='index.Tours')),
            ],
        ),
    ]
