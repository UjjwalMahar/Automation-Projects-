import requests

API_KEY = "d8fb12ca3c398dbfbb61386116b2cd8d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name : ")

requests_url =  f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    temperature = round(data["main"]["temp"]-273.15,2)
    print("Weather is of {} is : ".format(city),weather)
    print("Temperature is of {} is : ".format(city),temperature,"clesius")
else:
    print("Error Occured")