from django.shortcuts import render
from django.http import JsonResponse

def index(request):
	return render(request, 'index.html')


def send_view_visit(request):
	view = request.GET.get("view")
	data = {
		'': '',
	}
	return JsonResponse(data)