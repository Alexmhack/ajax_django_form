from django.shortcuts import render
from django.http import JsonResponse

def index(request):
	return render(request, 'index.html')


def service_view(request):
	return render(request, 'services.html')


def features_view(request):
	return render(request, 'features.html')


def pricing_view(request):
	return render(request, 'pricing.html')


def contact_view(request):
	return render(request, 'contact.html')


def blog_view(request):
	return render(request, 'blog.html')


def about_view(request):
	return render(request, 'about.html')


visits = dict()
data = dict()


def send_view_visit(request):
	view = request.GET.get("viewPage")
	visits[view] = 10
	data['total'] = visits[view]
	print(data)
	print(visits)

	return JsonResponse(data)