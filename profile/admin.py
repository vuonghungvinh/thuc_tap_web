from django.contrib import admin
from .models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'gender', 'date', 'avatar', 'phone', 'address')
	list_filter = ('user', 'date')
	search_fields = ('user', 'date')

admin.site.register(UserProfile, UserProfileAdmin)