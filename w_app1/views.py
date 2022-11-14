from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=c9246b554713d21f42bb2b916c52ab20'

    if(request.method == 'POST'):
        form = CityForm(request.POST)   # создаем объект на основе класса, который содержит форму
        form.save()                     # сохраняем данные в БД

    form = CityForm                     # очистим форму при перезагрузке страницы

    cities = City.objects.all()         # обращаемся к таблице City, выбираем из нее все данные
    all_cities = []
    for city in cities:                                         # перебираем полученные данные
        res = requests.get(url.format(city.name)).json()        # узнаем погоду для каждого города
        city_info = {                                           # записываем нужные данные в словарь
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)                     # записываем словарь в список

    context = {'all_info': all_cities, 'form': form}     # передаем список и форму в html-шаблон
    return render(request, 'weather/index.html', context)
