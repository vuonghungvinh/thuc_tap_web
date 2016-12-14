from django.db import models
from index.models import Tours
# Create your models here.
class Booking(models.Model):
	choice_status = (
		(0, 'pendding'),
		(1, 'accept'),
		(2, 'cancel'),
		(3, 'completed'),
	)
	user = models.ForeignKey("auth.User")
	tour = models.ForeignKey(Tours, related_name='booking_tour', default=0)
	name = models.CharField(max_length=200, default='', null=False, blank=False)
	email = models.EmailField(max_length=100)
	address = models.CharField(max_length=200)
	phone = models.IntegerField(max_length=11)
	note = models.CharField(max_length=200, default='')
	adult = models.IntegerField()	
	children = models.IntegerField(default=0)
	total = models.FloatField(default=0)
	status = models.IntegerField(choices=choice_status, default=0)

class ListCustomer(models.Model):
	choice_gender = (
		(True, 'Male'),
		(False, 'Female'),
	)
	choice_type = (
		(True, 'Adult'),
		(False, 'Children'),
	)
	booking = models.ForeignKey("Booking", related_name="list_booking")
	name = models.CharField(max_length=200, default='', null=False, blank=False)
	date = models.DateField(null=True, blank=True)
	gender = models.BooleanField(choices=choice_gender)
	address = models.CharField(max_length=200)
	type_customer = models.BooleanField(choices=choice_type)
	cost = models.FloatField(default=0)