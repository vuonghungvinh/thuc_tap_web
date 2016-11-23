from __future__ import unicode_literals
from django.db import models
from django_resized import ResizedImageField
import re
from datetime import datetime
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your models here.
def get_upload_file_name(instance, filename):
	name = re.sub(ur'[^a-zA-Z0-9._\-()]', '', str(filename))
	name1 = re.sub(ur'[^a-zA-Z0-9]', '', str(datetime.today()))
	name = str(name1)+str(name)
	return os.path.join("uploads/slider", name)
def get_upload_file_name1(instance, filename):
	name = re.sub(ur'[^a-zA-Z0-9._\-()]', '', str(filename))
	name1 = re.sub(ur'[^a-zA-Z0-9]', '', str(datetime.today()))
	name = str(name1)+str(name)
	return os.path.join("uploads/tours", name)

def get_upload_file_name_tour_slider(instance, filename):
	name = re.sub(ur'[^a-zA-Z0-9._\-()]', '', str(filename))
	name1 = re.sub(ur'[^a-zA-Z0-9]', '', str(datetime.today()))
	name = str(name1)+str(name)
	return os.path.join("uploads/tours_sliders", name)

class Sliderhome(models.Model):
	photo = ResizedImageField(upload_to=get_upload_file_name, size=[1024, 768])
	title = models.CharField(max_length=40, default='', null=True, blank=True)
	isshow = models.BooleanField(default=True)
	def __str__(self):
		return self.title
	def save(self, *args, **kwargs):
		# delete old file when replacing by updating the file
		try:
			this = Sliderhome.objects.get(id=self.id)
			if this.photo != self.photo:
				this.photo.delete(save=False)
		except: pass # when new photo then we do nothing, normal case
		super(Sliderhome, self).save(*args, **kwargs)

class Tours(models.Model):
	name = models.CharField(default='name tuor', max_length=100)
	photo = ResizedImageField(upload_to=get_upload_file_name1, size=[1024, 768])
	cost = models.FloatField()
	days = models.PositiveIntegerField()
	is_sale = models.BooleanField(default=False)
	cost_sale = models.FloatField(default=0, null=True, blank=True)
	date = models.DateField(null=True, blank=True)
	inside = models.BooleanField(default=True)
	# def __str__(self):
	# 	return self.name
	def __str__(self):
		return str(self.name)
	def save(self, *args, **kwargs):
		# delete old file when replacing by updating the file
		try:
			this = Tours.objects.get(id=self.id)
			if this.photo != self.photo:
				this.photo.delete(save=False)
		except: pass # when new photo then we do nothing, normal case
		super(Tours, self).save(*args, **kwargs)

class DetailTour(models.Model):
	tour = models.OneToOneField(Tours, related_name='tour')
	photo1 = ResizedImageField(upload_to=get_upload_file_name_tour_slider, size=[1024, 768])
	photo2 = ResizedImageField(upload_to=get_upload_file_name_tour_slider, size=[1024, 768])
	photo3 = ResizedImageField(upload_to=get_upload_file_name_tour_slider, size=[1024, 768])
	photo4 = ResizedImageField(upload_to=get_upload_file_name_tour_slider, size=[1024, 768])
	detail = models.TextField(max_length=5000, default='Please describe your tour here')
	programmer = models.TextField(max_length=1000, default='Please describe your programmer here')
	local_highlight = models.TextField(max_length=1000, default='Please describe your local highlights here')
	def save(self, *args, **kwargs):
		# delete old file when replacing by updating the file
		try:
			this = DetailTour.objects.get(id=self.id)
			if this.photo1 != self.photo1:
				this.photo1.delete(save=False)
			if this.photo2 != self.photo2:
				this.photo2.delete(save=False)
			if this.photo3 != self.photo3:
				this.photo3.delete(save=False)
			if this.photo4 != self.photo4:
				this.photo4.delete(save=False)
		except: pass # when new photo then we do nothing, normal case
		super(DetailTour, self).save(*args, **kwargs)