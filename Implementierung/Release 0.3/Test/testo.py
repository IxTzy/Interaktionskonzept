import numpy as np
from entitys import *
AmbulanceArray = np.array([])

print(len(AmbulanceArray))
AmbulanceArray = np.append(AmbulanceArray, Ambulance(
    "Klaus", [120.0, 5451], True, "amb1"))

print(len(AmbulanceArray))
AmbulanceArray = np.append(AmbulanceArray, Ambulance(
    "Klaus", [120.0, 5451], True, "amb1"))

print(len(AmbulanceArray))
AmbulanceArray = np.append(AmbulanceArray, Ambulance(
    "Klaus", [120.0, 5451], True, "amb1"))

print(len(AmbulanceArray))
AmbulanceArray = np.append(AmbulanceArray, Ambulance(
    "Klaus", [120.0, 5451], True, "amb1"))

print(len(AmbulanceArray))
AmbulanceArray = np.append(AmbulanceArray, Ambulance(
    "Klaus", [120.0, 5451], True, "amb1"))

print(len(AmbulanceArray))
AmbulanceArray = np.append(AmbulanceArray, Ambulance(
    "Klaus", [120.0, 5451], True, "amb1"))
print(len(AmbulanceArray))
print(len(AmbulanceArray))
print(len(AmbulanceArray))
print(len(AmbulanceArray))
print(len(AmbulanceArray))
print(len(AmbulanceArray))
print(len(AmbulanceArray))
print(len(AmbulanceArray))

AmbulanceList = []
print(len(AmbulanceList))
AmbulanceList.append(Ambulance(
    "Klafus", [120.0, 5451], True, "amb1"))
print(len(AmbulanceList))
AmbulanceList.append(Ambulance(
    "Klfgfhgfggfaus", [120.0, 5451], True, "amb1"))
print(len(AmbulanceList))
AmbulanceList.append(Ambulance(
    "Klaus", [120.0, 5451], True, "amb1"))
print(len(AmbulanceList))
AmbulanceList.append(Ambulance(
    "Klaus", [120.0, 5451], True, "amb1"))
print(len(AmbulanceList))
AmbulanceList.append(Ambulance(
    "Klaus", [120.0, 5451], True, "amb15554"))
print(len(AmbulanceList))
AmbulanceList.append(Ambulance(
    "Klaus", [120.0, 5451], True, "amb111"))
print(len(AmbulanceList))
AmbulanceList.append(Ambulance(
    "Klaus", [120.0, 5451], True, "amb111111"))
print(len(AmbulanceList))
    "Klaus", [120.0, 5451], True, "amb11"))
print(len(AmbulanceList))

List.append(Ambulance(
    "Klaus", [120.0, 5451], True, "amb111111"))




def check():
    for x in range(0, 12):
        print("Check: ", x)
        if AmbulanceList[4].id == "amb1":
            print("There is an entity with the same id: ",
                  AmbulanceList[4].driverName)
            return False
        print("alles gucci")
    return True

    if check(split[3], AmbulanceList) == True:
        AmbulanceList.append(
            Ambulance(split[0], locationSplit, split[2], split[3]))


check()
