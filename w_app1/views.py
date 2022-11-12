from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    city = 'London'
    country = 'uk'
    #url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={API_key}'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid=c9246b554713d21f42bb2b916c52ab20'

    res = requests.get(url.format(city,country)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon']
    }
    context = {'info': city_info}

    return render(request, 'weather/index.html', context)
