# small API exercise to get weather information from http://api.weatherstack.com/
# Prints weather information from selected location
import requests
import json
import sys


def main(api_key, location):
    api_address = 'http://api.weatherstack.com/'
    responce = requests.get(api_address + 'current?access_key=' + api_key + '&query=' + location)

    #start if statement
    if responce.status_code == 200:
        print("Connection to API was successfull, start fecthing weather information from " + location)
        responce_to_dict = responce.json()
        request = responce_to_dict['request']
        location = responce_to_dict['location']
        current = responce_to_dict['current']
        print("Location which weather information is fetched: " +location['name'])
        print("Location country: " +location['country'])
        print("Locations latitude: " +location['lat'] + " " + " and longitude: " + location['lon'])
        print("Current temperature: " +str(current['temperature']) +" c")
        print("Weather description: " +str(current['weather_descriptions']))
        print("Wind speed is: " +str(current['wind_speed']))
    else:
        print("Something went wrong, please check API key")


if __name__ == "__main__":
    print("Give API_key as first argument, and city as second argument")
    api_key = str(sys.argv[1])
    location = str(sys.argv[2])
    main(api_key, location)
