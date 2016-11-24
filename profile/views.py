from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from models import UserProfile
from django.contrib.auth.models import User
from .forms import MyProfileForm, UserForm
# Create your views here.
@login_required
def myprofile(request):
	user = get_object_or_404(User, id=request.user.id)
	try:
		profile = UserProfile.objects.get(user_id=request.user.id)
	except:
		profile = None
	if request.method == 'POST':
		pass
	else:
		userf = UserForm(instance=user)
		profilef = MyProfileForm(instance=profile)
	return render(request, 'profile/myprofile.html', {'userf': userf, 'profilef': profilef})