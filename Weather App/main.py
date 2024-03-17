import requests
import json
import os

city = input("Enter the name of the city\n ")

url = (f"https://api.weatherapi.com/v1/current.json?key=7e26708fdba7467c8bb134210241703&q={city}")

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(f"Temprature of {city} is: "+str(wdic["current"]["temp_c"]) +"° C")
os.system(f"say 'The current temperature in {city} is '" +str(wdic["current"]["temp_c"]) +"° C")