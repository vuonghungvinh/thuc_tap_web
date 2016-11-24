from django import forms
# from .models import Fab, Fab_Address, Fab_Transaction, Fab_Reviews
from django.shortcuts import render
from django import template
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()