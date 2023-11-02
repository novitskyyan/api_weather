from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http import JsonResponse


def index(request):
    context = {}
    return render(request, 'weather/index.html', context)


def get_weather(request):
    if request.method == 'GET':
        city = request.GET.get("city")
        print(city)
        data = {"message": "ok"}
        return JsonResponse(data)