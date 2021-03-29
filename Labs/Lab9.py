import json
import requests
r = requests.get('http://localhost:3000/')
data=r.json()

for x in data:
    if data == "name":
        continue

for y in data:    
    if data == "color":
        continue
print(x %'is'% y)

