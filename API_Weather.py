# small API exercise to get weather information from http://api.weatherstack.com/
# Prints weather information from selected location
import requests
import json
import time


def main():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    api_key = config["API_KEY"]
    locations = config["locations"]   # list of locations

    api_address = "http://api.weatherstack.com/"

    for location in locations:
        response = requests.get(
            api_address + "current?access_key=" + api_key + "&query=" + location
        )

        if response.status_code == 200:
            print("Fetching weather information from " + location)

            data = response.json()

            location_name = data['location']['name']
            country = data['location']['country']
            latitude = data['location']['lat']
            longitude = data['location']['lon']
            temperature = data['current']['temperature']
            description = data['current']['weather_descriptions'][0]
            wind_speed = data['current']['wind_speed']

            print("Location:", location_name)
            print("Country:", country)
            print("Latitude:", latitude, "Longitude:", longitude)
            print("Temperature:", temperature, "c")
            print("Weather description:", description)
            print("Wind speed:", wind_speed)

            with open("results.txt", "a") as results_file:
                results_file.write(
                    f"{location_name};{country};{latitude};{temperature};{description};{wind_speed}\n"
                )
            #need to add 1 sec sleep, without it will return 429 return code
            time.sleep(1)

        else:
            print("Something went wrong for location:", location +" " + str(response.status_code))


if __name__ == "__main__":
    main()