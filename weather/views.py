import requests
from django.shortcuts import render


def index(request):  
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1' 
    city="Las Vegas"  
    r= requests.get(url.format(city)).json()

    print(r.text)     

    """ city_weather= { 
        'city': city, 
        'temperature': ,
        'description': , 
        'icon': ,
    }
    """


    return render(request,'weather/weather.html') 


    #{"coord":{"lon":-115.15,"lat":36.17},
    #"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
    #"base":"stations",
    #"main":{"temp":46.26,"feels_like":40.46,"temp_min":42.8,"temp_max":48,"pressure":1018,"humidity":52},
    #"visibility":16093,"wind":{"speed":3.36,"deg":260},"clouds":{"all":1},"dt":1577906007,
    #"sys":{"type":1,"id":3527,"country":"US","sunrise":1577890294,"sunset":1577925370},
    #"timezone":-28800,"id":5506956,"name":"Las Vegas","cod":200}