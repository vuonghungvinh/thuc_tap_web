from django.conf.urls import patterns, url
from django.conf import settings
from booking import views

urlpatterns = [
	url(r"^(?P<id>\d+)/$", views.home, name="homepage"),
	url(r"^save/$", views.savebooking, name="save"),
]