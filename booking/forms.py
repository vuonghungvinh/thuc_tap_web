from django import forms
from django.shortcuts import render
from django import template
from .models import Booking
from django.utils.safestring import mark_safe
class BookingForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	note = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Booking
		fields = ('name', 'email', 'address', 'phone', 'note')