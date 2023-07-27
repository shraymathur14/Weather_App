from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City

# Create your views here.
def index(request):
    cities = City.objects.all()
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID=bf2ea966283fa8aee998114a94dcf86e"
    
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass        

    form = CityForm()
    weather_data=[]
    for city in cities:
        r = requests.get(url.format(city.name)).json()
        city_weather={
            'city': city,
            'temperature': r["main"]["temp"],
            'description': r["weather"][0]["description"],
            'icon': r["weather"][0]["icon"]
        }
        weather_data.append(city_weather)
    return render(request, 'weather/index.html', context={"weather_data":weather_data, 'form' : form})
