from django.contrib import admin
from models import Sliderhome, Tours, DetailTour
from ckeditor.widgets import CKEditorWidget
from django import forms
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Register your models here.

class SliderAdmin(admin.ModelAdmin):
	list_display = ('photo', 'title', 'isshow')
	list_filter = ('title', 'isshow')
	search_fields = ('title', 'isshow')

class TourAdmin(admin.ModelAdmin):
	list_display = ('name', 'photo', 'cost', 'days', 'is_sale', 'cost_sale', 'date', 'inside', 'isopen', 'child', 'startaddress', 'slot')
	list_filter = ('days', 'date')
	search_fields = ('days', 'date')

class DetailTourForm(forms.ModelForm):
	# detail = forms.CharField(widget=CKEditorWidget())
	programmer = forms.CharField(widget=CKEditorWidget())
	local_highlight = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = DetailTour
		fields = ('tour', 'detail', 'programmer', 'local_highlight', 'photo1', 'photo2', 'photo3', 'photo4')
class DetailTourAdmin(admin.ModelAdmin):
	form = DetailTourForm
	list_display = ('tour', 'detail', 'programmer', 'local_highlight', 'photo1', 'photo2', 'photo3', 'photo4')
	# list_filter = ('detail', 'programmer', 'local_highlight')			
	search_fields = ('detail', 'programmer', 'local_highlight')			
admin.site.register(Sliderhome, SliderAdmin)
admin.site.register(Tours, TourAdmin)
admin.site.register(DetailTour, DetailTourAdmin)