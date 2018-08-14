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


def send_view_visit(request):
	view = request.GET.get("view")
	data = {
		'': '',
	}
	return JsonResponse(data)