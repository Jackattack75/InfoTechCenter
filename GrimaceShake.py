print("*****************************************************************")
print("Gasoline Branch\n\n")

#Import Libaries Here
import random

def GasLevelGauge():
    GasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    CurrentGasLevel = random.choice(GasLevelList)
    return CurrentGasLevel


print(GasLevelGauge())