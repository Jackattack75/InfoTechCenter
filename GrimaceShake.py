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
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50 mph.")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of",weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 40 mph.")
    elif weatherAlert == "Raining":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60 mph.")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60 mph.")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 70 mph.")
    elif weatherAlert == "Icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forecast of",weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 30 mph.")
    else:
        print("\nNational Weather Service forecast", weatherAlert,"weather conditions")
        sleep(1.5)
        print("VRS has been disengaged! Drive at your own risk.")



vehicleResponseSystem()