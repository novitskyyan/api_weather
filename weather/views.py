from json import loads, dump
from time import sleep

from django.http import JsonResponse
from django.shortcuts import render
from weather_api import weather


def index(request):
    sleep(2)
    with open('weather.json', "r", encoding="UTF-8") as file:
        if len(file.read()) != 0:
            file.seek(0)
            context = loads(file.read())
        else:
            context = {"1": {"city": "ыпквпв", "weather": []},
                       "2": {"city": "пвпвпв", "weather": []},
                       "3": {"city": "впвпав", "weather": []},
                       "4": {"city": "впвпввп", "weather": []}}
            with open("weather.json", "w", encoding='UTF-8') as json_file:
                dump(context, json_file)
        print(context)
    return render(request, 'weather/index.html', context)


def get_weather(request):
    if request.method == 'GET':
        city = request.GET.get("city")
        w = weather.Weather(city)
        info = {'city': city, 'weather': w.get_info()[1:]}
        with open("weather.json", "w", encoding='UTF-8') as json_file:
            dump(info, json_file)
        data = {"message": "ok"}
        return JsonResponse(data)
