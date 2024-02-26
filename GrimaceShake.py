print("\n************************************************************\n")

print("Weather Branch\n")

#Import Libaries Here
import random
from time import sleep

#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variable to call the weather() once VRS(Vehicle Response System)
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Snowing":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of",weatherAlert,
              "weather conditions")
        print("VRS has been engaged only allowing you to drive 50 mph.")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of",weatherAlert,
              "weather conditions")
        print("VRS has been engaged only allowing you to drive 40 mph.")
    elif weatherAlert == "Raining":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions")
        print("VRS has been engaged only allowing you to drive 60 mph.")


vehicleResponseSystem()