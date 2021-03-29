import json
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=45211,us&appid=5794afd3e218f087d0fe7f30b95a295d')
data=r.json()

print(data)