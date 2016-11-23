from django.shortcuts import render
from index.models import Tours, Sliderhome, DetailTour
# Create your views here.

def home(request):
	sliders = Sliderhome.objects.filter(isshow=True)
	giamgia_trongnuoc = Tours.objects.filter(is_sale=True, inside=True)
	giamgia_ngoainuoc = Tours.objects.filter(is_sale=True, inside=False)
	dacbiet_ngoainuoc = Tours.objects.filter(is_sale=False, inside=False)
	dacbiet_trongnuoc = Tours.objects.filter(is_sale=False, inside=True)
	context = {
		'giamgia_trongnuoc': giamgia_trongnuoc,
		'giamgia_ngoainuoc': giamgia_ngoainuoc,
		'dacbiet_ngoainuoc': dacbiet_ngoainuoc,
		'dacbiet_trongnuoc': dacbiet_trongnuoc,
		'sliders': sliders
	}
	return render(request, 'index/home.html', context)

def detail(request, id):
	detals=DetailTour.objects.get(tour_id=id)
	context = {'detail': detals}
	return render(request, 'index/detail.html', context)