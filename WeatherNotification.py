import requests as re
from plyer import notification

API_KEY = "d8fb12ca3c398dbfbb61386116b2cd8d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = "pithoragarh"

requests_url =  f"{BASE_URL}?appid={API_KEY}&q={city}"
response = re.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    temperature = round(data["main"]["temp"]-273.15,2)
    notification.notify(title = "Pithoragarh : ",
                        message =  "Weather is "+(data['weather'][0]["description"])+"\n"
                        + "Temperature is " + str(round(data["main"]["temp"]-273.15,2))+" degree celsius",
                        app_icon = "D:\AutiomationProjectsPython\gnome_weather_few_clouds.ico",
                        timeout = 5
                        )
else:
    print("Error Occured")
