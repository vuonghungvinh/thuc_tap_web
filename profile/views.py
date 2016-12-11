from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from models import UserProfile
from django.contrib.auth.models import User
from .forms import MyProfileForm, UserForm
from django.contrib.messages import info, error
# Create your views here.
@login_required
def myprofile(request):
	user = get_object_or_404(User, id=request.user.id)
	try:
		profile = UserProfile.objects.get(user_id=request.user.id)
	except:
		profile = None
	if request.method == 'POST':
		userf = UserForm(request.POST, instance=user)
		profilef = MyProfileForm(request.POST, request.FILES, instance=profile)
		if userf.is_valid() and profilef.is_valid():
			form1 = userf.save(commit=False)
			form1.save()
			form2 = profilef.save(commit=False)
			form2.user_id = form1.id
			form2.save()
			userf = UserForm(instance=user)
			profilef = MyProfileForm(instance=profile)
			info(request, ("Updated Profile"))
			user = get_object_or_404(User, id=request.user.id)
			try:
				profile = UserProfile.objects.get(user_id=request.user.id)
			except:
				profile = None
			userf = UserForm(instance=user)
			profilef = MyProfileForm(instance=profile)
	else:
		userf = UserForm(instance=user)
		profilef = MyProfileForm(instance=profile)
	return render(request, 'profile/myprofile.html', {'userf': userf, 'profilef': profilef})