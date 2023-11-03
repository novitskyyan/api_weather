from django.shortcuts import render
from django.http import JsonResponse

from weather_api import weather

def index(request):
    context = {'weather': ["Москва", "Самара", "Казань", "Новгород"]}
    return render(request, 'weather/index.html', context)


def get_weather(request):
    if request.method == 'GET':
        city = request.GET.get("city")
        w = weather.Weather(city)
        print(w.get_info())
        data = {"message": "ok"}
        return JsonResponse(data)