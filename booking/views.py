# -*- coding: utf-8 -*-
import sys
print sys.getdefaultencoding()
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from index.models import Tours
from django.http import HttpResponse, JsonResponse
from .models import Booking, ListCustomer
import json
import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.contrib.messages import info, error
from django.core.mail import EmailMultiAlternatives
import time
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
# -*- coding: utf-8 -*-
# Create your views here.
@login_required
def home(request, id):
	tour = Tours.objects.get(id=id)
	return render(request, 'booking/booking.html', {'tour': tour})
@csrf_exempt
@login_required
def savebooking(request):
	datas = json.loads(request.body)
	if request.method == 'POST':
		t=Tours.objects.get(id=datas['info']['tour'])
		adult = int(datas['info']['adult'])
		children=0
		if len(datas['info']['children'])>0:
			children = int(datas['info']['children'])
		if ((adult+children) > int(t.slot)):
			return HttpResponse(json.dumps({'data': 'Bạn nhập quá số lượng cho phép', 'status': 0}), content_type="application/json")
		try:
			booking = Booking(user=request.user, tour_id=datas['info']['tour'], name=datas['info']['name'], email=datas['info']['email'], address=datas['info']['address'], phone=datas['info']['phone'], note=datas['info']['note'], adult=datas['info']['adult'], children=datas['info']['children'], total=datas['info']['total'])
			booking.save()
			for li in datas['listcustomer']:
				customer = ListCustomer(booking_id=booking.pk, name=li['name'], date=li['date'], gender=li['gender'], address=li['address'], type_customer=li['type_customer'], cost=li['cost'])
				customer.save()
			site = get_current_site(request)
			subject = 'New Booking'
			from_email = settings.DEFAULT_FROM_EMAIL
			to = settings.EMAIL_ADMIN
			text_content = 'You have new booking from '+request.user.username+'.'
			html_content = '<h3>You have new booking from '+request.user.username+'.</h3>'
			html_content += '<a href="'+ str(site) +'">please click this link to to site</a>'
			html_content += '<p>'+time.strftime("%d/%m/%Y")+'</p>'
			html_content += "<br/>"
			html_content += "<hr style='background-color:#ddd;height:1px;border:1px;'>"
			html_content += '<p><b>Please do not reply to this message.  This e-mail address is for outgoing purposes only.</b></p>'
			mail = EmailMultiAlternatives(
				subject=subject,
				body="This is a simple text email body.",
				from_email=from_email,
				to=[to]
			)
			mail.attach_alternative(html_content, "text/html")
			mail.send()
			subject = 'New Booking'
			from_email = settings.DEFAULT_FROM_EMAIL
			to = request.user.email
			text_content = ''
			html_content = '<h3>Bạn đã đặt thành công tour: <b>'+ t.name +'</b></h3>'
			html_content += '<h4>Cám ơn bạn đã đăng kí dịch vụ du lịch của chúng tôi.</h4>'
			html_content += '<p>'+time.strftime("%d/%m/%Y")+'</p>'
			html_content += "<br/>"
			html_content += "<hr style='background-color:#ddd;height:1px;border:1px;'>"
			html_content += '<p><b>Please do not reply to this message.  This e-mail address is for outgoing purposes only.</b></p>'
			mail = EmailMultiAlternatives(
				subject=subject,
				body="This is a simple text email body.",
				from_email=from_email,
				to=[to]
			)
			mail.attach_alternative(html_content, "text/html")
			mail.send()
			info(request, ("dnadasndb"))
		except Exception, e:
			return HttpResponse(json.dumps({'data': 'error', 'status': 0}), content_type="application/json")
	return HttpResponse(json.dumps({'data': 'success', 'status': 1}), content_type="application/json")