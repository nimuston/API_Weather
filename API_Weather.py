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
        print("Location which weather information is fetched: " +responce_to_dict['location']['name'])
        print("Location country: " +responce_to_dict['location']['country'])
        print("Locations latitude: " +responce_to_dict['location']['lat'] + " " + " and longitude: " + responce_to_dict['location']['lon'])
        print("Current temperature: " +str(responce_to_dict['current']['temperature']) +" c")
        print("Weather description: " +str(responce_to_dict['current']['weather_descriptions']))
        print("Wind speed is: " +str(responce_to_dict['current']['wind_speed']))
    else:
        print("Something went wrong, please check API key")


if __name__ == "__main__":
    print("Give API_key as first argument, and city as second argument")
    api_key = input("Please give API key: ")
    location = input("Please give location which weather details you what: ")
    main(api_key, location)
