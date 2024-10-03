import requests

API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def main():

    city = input("\nEnter city name: ")
    weather = get_weather(city)


def get_weather(city_name):

    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"

    # Send the request and get the response
    response = requests.get(complete_url)

    # Convert the response to JSON format
    data = response.json()

    # Check if the city is found
    if data["cod"] != "404":
        print(data)

        # Extract main dictionary block which contains weather info
        main = data["main"]
        weather = data["weather"][0]

        # Extract the temperature, pressure, humidity, and description
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]

        # Print the weather information
        print(f"\nWeather in {city_name}:")
        print(f"Description: {weather_description.capitalize()}")
        print(f"Temperature: {temperature}°C")
        # print(f"Pressure: {pressure} hPa")
        # print(f"Humidity: {humidity}%")
    else:
        print(f"City {city_name} not found.")


if __name__ == "__main__":
    main()
