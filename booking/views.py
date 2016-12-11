from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from index.models import Tours
# Create your views here.
@login_required
def home(request, id):
	tour = Tours.objects.get(id=id)
	return render(request, 'booking/booking.html', {'tour': tour})