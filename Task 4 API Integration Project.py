import requests

city = input("Enter City Name: ")

api_key = "21fb67d5e8b4c7d5f870322d71d95a0b"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print("\nWeather Information")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
    else:
        print(data["message"])

except Exception as e:
    print("Error:", e)
    


