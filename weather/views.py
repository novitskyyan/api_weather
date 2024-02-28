from json import loads, dump
from time import sleep

from django.http import JsonResponse
from django.shortcuts import render
from weather_api import weather


def index(request):
    sleep(2)
    # TODO: В случае если json Не пустой, его содержимое передать в context и
    # TODO: и Применить render. В обратном случае создать словарь с правильными
    # TODO: ключами и структурой и записать его в json.
    with open('weather.json', "r", encoding="UTF-8") as file:
        if len(file.read()) != 0:
            file.seek(0)
            context = loads(file.read())
        else:
            # TODO: Правильно выбрать формат словаря, чтобы можно было подставить в шаблон. Плюс понять, как можно подставлять словаря в шаблон django.
            context = {"1": {"city": None, "weather": None},
                       "2": {"city": None, "weather": None},
                       "3": {"city": None, "weather": None},
                       "4": {"city": None, "weather": None}}
            with open("weather.json", "w", encoding='UTF-8') as json_file:
                dump(context, json_file, ensure_ascii=False)
        print(context)
    return render(request, 'weather/index.html', context)


def get_weather(request):
    if request.method == 'GET':
        city = request.GET.get("city")
        w = weather.Weather(city)

        with open("weather.json", "r", encoding='UTF-8') as json_file:
            context = loads(json_file.read())
            if context["1"]['city'] is None:
                context['1']['city'] = city
                context['1']['weather'] = w.get_info()[1:]

        # TODO: Обрабатываем json: 1. считываем json; если есть свободное место из 4, то добавляем город и информацию по погоде; в другом случае, если там есть 4 города с информацией, то удаляем последний 4 и кладем новый в начало.
        with open("weather.json", "w", encoding='UTF-8') as json_file:
            dump(context, json_file, ensure_ascii=False)
        data = {"message": "ok"}
        return JsonResponse(data)
