import requests

from config import API_KEY

print("====== 🌤️  WEATHER APP  🌤️ ======")

while True:
    city = input("\nWhat city's weather would you like to see? (If you want to exit, type 'exit'): ")

    if city.lower() == "exit":
        print("👋 App got closed! Bye!")
        break

    # API URL banana
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    # API ko request bhejo
    response = requests.get(url)
    data = response.json()

    # Response check karo
    if response.status_code == 200:
        print("\n===========================")
        print(f" City       : {data['name']}, {data['sys']['country']}")
        print(f" Temperature : {data['main']['temp']}°C")
        print(f" Feels Like  : {data['main']['feels_like']}°C")
        print(f" Weather     : {data['weather'][0]['description']}")
        print(f" Humidity    : {data['main']['humidity']}%")
        print(f" Wind Speed  : {data['wind']['speed']} m/s")
        print("===========================")

    elif response.status_code == 401:
        print("❌ API Key is invalid.")
        break

    elif response.status_code == 404:
        print("❌ City Not Found. (Like: Delhi, Mumbai, London)")

    else:
        print(f"❌ Something went wrong: {response.status_code}")