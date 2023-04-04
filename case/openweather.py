import requests
import os
from dotenv import load_dotenv

load_dotenv()
city = input("Enter City:")

BaseUrl = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = os.getenv("api_key")
url  = BaseUrl + "appid=" + api_key + "&q="+ format(city)
res = requests.get(url)
data = res.json()

humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
description = data['weather'][0]['description']
temp = data['main']['temp']

print('Temperature:',temp,'°C')
print('Wind:',wind)
print('Pressure: ',pressure)
print('Humidity: ',humidity)
print('Description:',description)