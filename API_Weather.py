# small API exercise to get weather information from http://api.weatherstack.com/
# Prints weather information from selected location
import requests
import json


def main():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    api_key = config["API_KEY"]
    location = config["location"]

    api_address = "http://api.weatherstack.com/"
    response = requests.get(api_address + "current?access_key=" + api_key + "&query=" + location)

    if response.status_code == 200:
        print("Connection to API was successful, start fetching weather information from " + location)

        response_to_dict = response.json()

        location_name = response_to_dict['location']['name']
        country = response_to_dict['location']['country']
        latitude = response_to_dict['location']['lat']
        longitude = response_to_dict['location']['lon']
        temperature = response_to_dict['current']['temperature']
        description = response_to_dict['current']['weather_descriptions'][0]
        wind_speed = response_to_dict['current']['wind_speed']

        print("Location which weather information is fetched: " + location_name)
        print("Location country: " + country)
        print("Locations latitude: " + latitude + " and longitude: " + response_to_dict['location']['lon'])
        print("Current temperature: " + str(temperature) + " c")
        print("Weather description: " + description)
        print("Wind speed is: " + str(wind_speed))

        with open("results.txt", "a") as results_file:
            results_file.write(f"{location_name};{country};{latitude};{longitude};{temperature};{description};{wind_speed}"+'\n')

        print("Results saved to results.txt")

    else:
        print("Something went wrong, please check API key")


if __name__ == "__main__":
    main()