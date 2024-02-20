print("*****************************************************************")
print("Gasoline Branch\n\n")

#Import Libaries Here
import random
from time import sleep

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


gasLevelAlert()

