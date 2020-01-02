import requests
from django.shortcuts import render
from .models import City 
from .forms import CityForm

def index(request):  
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'   

    err_msg='' 

    if request.method =='POST' :
        form = CityForm(request.POST)  

        if form.is_valid():
            new_city = form.cleaned_data['name'] 
            existing_city_count = City.objects.filter(name=new_city).count() 
            if existing_city_count==0:
                
                print(r)
                form.save() 
            else:
                err_msg= 'City already exists in the database!'

    form=CityForm() 
    cities=City.objects.all()  

    weather_data=[]

    for city in cities:
        r = requests.get(url.format(city)).json() 
        city_weather= { 
            'city': city.name ,    #name bcoz we want name not object (models.py)
            'temperature': ((r['main']['temp'] - 32)*5)/9,
            'description': r['weather'][0]['description'], 
            'icon': r['weather'][0]['icon'],
             }  
        weather_data.append(city_weather) 
    
    print(weather_data)

    #print(city_weather) 

    context = {'weather_data': weather_data , 'form' : form }
    return render(request,'weather/weather.html', context ) 


    #{"coord":{"lon":-115.15,"lat":36.17},
    #"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
    #"base":"stations",
    #"main":{"temp":46.26,"feels_like":40.46,"temp_min":42.8,"temp_max":48,"pressure":1018,"humidity":52},
    #"visibility":16093,"wind":{"speed":3.36,"deg":260},"clouds":{"all":1},"dt":1577906007,
    #"sys":{"type":1,"id":3527,"country":"US","sunrise":1577890294,"sunset":1577925370},
    #"timezone":-28800,"id":5506956,"name":"Las Vegas","cod":200}