from __future__ import unicode_literals
from django.db import models
from django_resized import ResizedImageField
from datetime import datetime
import os
import sys
import re
# Create your models here.
def get_upload_file_user_profile(instance, filename):
	name = re.sub(ur'[^a-zA-Z0-9._\-()]', '', str(filename))
	name1 = re.sub(ur'[^a-zA-Z0-9]', '', str(datetime.today()))
	name = str(name1)+str(name)
	return os.path.join("uploads/user_profile", name)
class UserProfile(models.Model):
	choice_gender = (
		(True, 'Male'),
		(False, 'Female'),
	)
	user = models.OneToOneField("auth.User", related_name="profile_user")
	gender = models.BooleanField(choices=choice_gender)
	date = models.DateField(null=True, blank=True)
	avatar = ResizedImageField(upload_to=get_upload_file_user_profile, size=[1024, 768])
	phone = models.CharField(max_length=15, default='')
	address = models.CharField(max_length=100, default='')
	