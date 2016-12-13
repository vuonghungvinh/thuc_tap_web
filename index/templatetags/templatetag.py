from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
def subcost(value, cost):
	return value - cost

@register.filter
def animate(value):
	print value
	val = value%4
	if val==1:
		return -200
	elif val==2:
		return -100
	elif val==3:
		return 100
	else:
		return 200

@register.filter
def percentchild(value):
	if value.is_sale:
		cost = value.cost_sale
	else:
		cost = value.cost
	return cost*value.child/100

@register.filter
def percentadult(value):
	if value.is_sale:
		return value.cost_sale
	else:
		return value.cost