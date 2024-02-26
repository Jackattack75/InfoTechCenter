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

print(weather())