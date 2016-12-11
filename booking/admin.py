from django.contrib import admin
from models import Booking, ListCustomer
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Register your models here.

class BookingAdmin(admin.ModelAdmin):
	list_display = ('user', 'name', 'email', 'address', 'phone', 'note', 'adult', 'children', 'total', 'status')
	list_filter = ('user', 'name')
	search_fields = ('user', 'name')

class ListCustomerAdmin(admin.ModelAdmin):
	list_display = ('booking', 'name', 'date', 'gender', 'address', 'type_customer', 'cost')
	list_filter = ('booking', 'name')
	search_fields = ('booking', 'name')

admin.site.register(Booking, BookingAdmin)
admin.site.register(ListCustomer, ListCustomerAdmin)