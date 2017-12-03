import requests as req
import json
import pandas as pd
from citipy import citipy
import matplotlib.pyplot as plt

lat = []
n = [0,1,2,3,4,5]

for row in n:
    # lat.append(row)
    # print("lat:" + str(row))
    city = citipy.nearest_city(row, 101)
    lat.append(city.city_name)
# # print(lat)

url = 'http://api.openweathermap.org/data/2.5/weather/'
api_key = "00e1e179e7275d087f40c8b9313ae8a8"
params = {'appid': api_key,
            'q': '',
            'units': 'metric'}
weather_data = []
lat_data =[]
temp_data = []
# cities = ['Chennai', 'Berkeley', 'Chicago']

for city in lat:
    params['q'] = city
    response = req.get(url, params=params).json()
    weather_data.append(response)
print(weather_data)
for data in weather_data:
    lat_data.append(data['coord']['lat'])
    temp_data.append(data['main']['temp'])
weather_fact = {'temp': temp_data, 'lat': lat_data}
weather_fact = pd.DataFrame(weather_fact)
print(weather_fact.head())
