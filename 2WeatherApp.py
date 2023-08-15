import requests
import json         #It is used to convert the string o/p into dictionary
import pyttsx3




city=input("Enter the name of the city\n")

url=f"http://api.weatherapi.com/v1/current.json?key=7dd06a18a2f84ea3813111218231705&q={ city}"

r=requests.get(url)

# print(r.text)

wdic=json.loads(r.text) #json.loads() takes string argument and returns dictionary

print(wdic["current"]["temp_c"])       #paste the url in the browser and write the required city...there you will see what to write in the print....whether it's ["current"]["temp_c"] or ["current"]["last_updated_epoch"] or something else

print(wdic["current"]["last_updated_epoch"])


a=pyttsx3.init()
a.say(f"The current weather of {city} is { wdic['current']['temp_c'] }")
a.runAndWait()