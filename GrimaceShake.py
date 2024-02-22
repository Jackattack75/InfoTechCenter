#Import Libraries Here
import time
import sys
import random
from time import sleep

#Welcome Branch Starts Here
time_To_Sleep = 2

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(time_To_Sleep)

#Code to have the ellipsis add a dot every 0.5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center Operating System Booting" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!\n")


#Gasoline Branch Starts Here
print("*****************************************************************\n")
print("Gasoline Branch\n")

#Function that lists Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Moble","Costco","Meijer","7Eleven"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby

#Function will call the gasLevelGauge to determin our gas level and then find a close gas station
#by calling the listOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform( 1, 25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1, 50),1)
    gasLevel = gasLevelGauge()
    if gasLevel == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2.5)
        print("    ***Calling Triple AAA***")
    elif gasLevel == "Low":
        print("Your gas tank is extremly low, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationsLow,"miles away")
    elif gasLevel == "Quarter Tank":
        print("Your gas tank is on a Quarter Tank, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationsQuarterTank,"miles away")
    elif gasLevel == "Half Tank":
        print("your gas tank is a half of a tank full which is plenty to get to your destination")
    elif gasLevel == "Three Quarter Tank":
        print("Your gas tank is at three quarter tank")
    else:
        print("Your gas tank is full - YAY!!!! - Congratulations!!!!")
    

gasLevelAlert()