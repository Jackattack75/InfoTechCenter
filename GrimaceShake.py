print("*****************************************************************")
print("Gasoline Branch\n\n")

#Import Libaries Here
import random

#Function that lists Gas Levels, randomly choosing one and returning its value
def GasLevelGauge():
    GasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    CurrentGasLevel = random.choice(GasLevelList)
    return CurrentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Moble","Costco","Meijer","7Eleven"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby


print(GasLevelGauge())
print(listOfGasStations())