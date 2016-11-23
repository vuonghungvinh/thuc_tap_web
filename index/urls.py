from django.conf.urls import patterns, url
from django.conf import settings
from index import views

urlpatterns = [
	url(r"^$", views.home, name="homepage"),
	url(r"^details/(?P<id>\d+)/$", views.detail, name="detail"),
]