from entitys import *

########## Tests!##########

# Create Np Array to store all entitys
FirefighterArray = np.array([])
AmbulanceArray = np.array([])
PoliceArray = np.array([])
userCarArray = np.array([])
HospitalArray = np.array([])


# Funktion direkt unter dem recive der Nachricht
FirefighterArray = np.append(FirefighterArray, Firefighter(
    "klausobert", (1553, 17), True, "fire01"))
FirefighterArray = np.append(FirefighterArray, Firefighter(
    "hubschraubär", (1553, 17), True, "fire02"))


# print(fire1.driverName, fire1.location, fire1.id, fire1.isFree)

# fire1.updateValues(isFree=False, location=(1656, 897979), driverName="norbert")

# print(fire1.driverName, fire1.location, fire1.id, fire1.isFree)

# car1 = userCar("kleemens", (77, 88), "car1", None)

# print(car1.reasons)

for x in range(0, 2):
    if FirefighterArray[x].isFree == True:
        print(FirefighterArray[x].driverName, "hat zeit brudi!")
    else:
        print(FirefighterArray[x].driverName, "hat keine Zeit brudi!")


ambulance = eval(input("Creat Ambulance: "))  # liest eine liste ein!

# liste wird mit dem constructor bearbeitet
AmbulanceArray = np.append(AmbulanceArray, Ambulance(
    ambulance[0], ambulance[1], ambulance[2], ambulance[3]))

# liest eine liste ein! Bruder ist garkeine liste!
ambulance = eval(input("Creat Ambulance: "))

AmbulanceArray = np.append(AmbulanceArray, Ambulance(
    ambulance[0], ambulance[1], ambulance[2], ambulance[3]))

print(ambulance[1])
