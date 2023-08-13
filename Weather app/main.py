#Weather app
#date(11-08-2023)
import requests
import json
import win32com.client as wincom

city=input("Enter the name of the city:\n")
url=f"http://api.weatherapi.com/v1/current.json?key=2445c91072244e009cf134112231108&q={city}"

r=requests.get(url)
print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]


speak = wincom.Dispatch("SAPI.SpVoice")

speak.Speak(f"the current weather in {city} is {w} degrees.")
