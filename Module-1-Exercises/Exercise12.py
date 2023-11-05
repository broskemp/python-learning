import requests
import json

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()

print(response["value"])

while True:
    answer = input("\nDo you want to hear a Chuck Norris joke? Y/N: ").upper()
    if answer == "Y":
        print("\nHere is your Chuck Norris joke:")
        print(response["value"])
    elif answer == "N":
        break
    else:
        print("Please say Y or N.")

weather_request =
weather_response =