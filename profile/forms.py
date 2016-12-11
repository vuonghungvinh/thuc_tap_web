from django import forms
from .models import UserProfile
from django.shortcuts import render
from django import template
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
class ImageWidget(forms.FileInput):
	def __init__(self, attrs={}):
		super(ImageWidget, self).__init__(attrs)
	def render(self, name, value, attrs=None):
		output = []
		if value and hasattr(value, "url"):
			output.append(('<a target="_blank" href="%s">' '<img src="%s" style="height: auto; width: 250px" /></a> '% (value.url, value.url)))
		output.append(super(ImageWidget, self).render(name, value, attrs))
		return mark_safe(u''.join(output))

class MyProfileForm(forms.ModelForm):
	date = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker', 'readonly':'true'}))
	avatar = forms.ImageField(widget=ImageWidget)
	class Meta:
		model = UserProfile
		fields = ('gender', 'date', 'avatar', 'phone', 'address')
	def __init__(self, *args, **kwargs):
	    super(MyProfileForm, self).__init__(*args, **kwargs)
	    self.fields['date'].label = "Date birth"

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email')
		