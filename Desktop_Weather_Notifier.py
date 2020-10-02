import requests
from pynotifier import Notification

url = "https://api.openweathermap.org/data/2.5/weather?q="
cityname = "aurangabad"
api_key = '0e81c7d679b178bd9f2307abf7ef82da'

data = requests.get(url+cityname+'&appid='+api_key).json()

city = data['name']
country = data['sys']['country']
temperature = data['main']['temp_max'] - 273.15
weather = data['weather'][0]['main']
wind_speed = float(data['wind']['speed'])
humidity = data['main']['humidity']
pressure = data['main']['pressure']
if data ["cod"] != "404":
    Notification(
        title = city+","+country,
        description = f'{temperature}°C {weather}    Wind Speed{wind_speed}\n  Humidity{humidity}\n  Pressure{pressure}',
        duration = 100,
        icon_path = 'Weather.ico',
        urgency = Notification.URGENCY_CRITICAL).send()
    
else:
    print("City Not Found!!!")   
    
    
    