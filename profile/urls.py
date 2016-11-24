from django.conf.urls import patterns, url
from django.conf import settings
from profile import views

urlpatterns = [
	url(r"^$", views.myprofile, name="myprofile"),
	# url(r"^details/(?P<id>\d+)/$", views.detail, name="detail"),
]