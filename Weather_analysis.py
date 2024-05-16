import requests

def get_weather(api_key, city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temperature = data['main']['temp']
        return temperature
    else:
        print("Failed to retrieve weather data.")
        return None

def control_thermostat(temperature):

    desired_temperature = 20
    if temperature is not None:
        if temperature > desired_temperature:
            print(f"Temperature is {temperature}°C. Turning on the air conditioning.")

        elif temperature < desired_temperature:
            print(f"Temperature is {temperature}°C. Turning on the heater.")

        else:
            print(f"Temperature is {temperature}°C. No action needed.")
    else:
        print("Cannot control thermostat. Temperature data is unavailable.")

def main():

    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    city = "YOUR_CITY_NAME"
    temperature = get_weather(api_key, city)
    control_thermostat(temperature)

if __name__ == "__main__":
    main()
