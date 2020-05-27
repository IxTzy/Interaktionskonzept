from entitys import *
from manager import *
import paho.mqtt.client as mqtt
import time
import datetime
'''
TBD
Variablen umbennen
Daten verarbeitung
    Entfernungsbestimmung
Krankenhaus verwaltung
    update und anlegen
User verwaltung
    update und anlegen
'''

FirefighterList = []
AmbulanceList = []
PoliceList = []
userCarList = []
HospitalList = []

allEntityList = [FirefighterList, AmbulanceList,
                 PoliceList, userCarList, HospitalList]
# Event, dass beim Verbindungsaufbau aufgerufen wird


def on_connect(client, userdata, flags, rc):
    # Abonnieren des Topics (Hier die jeweiligen Topics einfügen die vorgegeben sind)
    client.subscribe('/hshl/ambulances/')
    print("subscribed to the ambulances topic!")
    client.subscribe('/hshl/firefighters/')
    print("subscribed to the firefighters topic!")
    client.subscribe('/hshl/polices/')
    print("subscribed to the polices topic!")
    client.subscribe('/hshl/hospitals/')
    print("subscribed to the hospitals topic!")
    client.subscribe('/hshl/users/')
    print("subscribed to the users topic!")


def sub(str, id, state):
    if state == True:
        client.subscribe(str + id)
        print("Subscribed to: " + str + id)
        client.publish(
            str, id + ": Successfully added! Channel for further Communication is: " + str + id)
    else:
        client.publish(str, id + ": Already exists! Change the Id!: ")


def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))  # Nachricht Dekodieren
    # Nachricht bei leerzeichen splitten

    split = str(msg).split(" ")
    locationSplit = split[1].split(",")
    locationSplit[0] = float(locationSplit[0])
    locationSplit[1] = float(locationSplit[1])

    if split[2] == "True":
        split[2] = True
    else:
        split[2] = False

    if message.topic.split("/")[3] == "":
        # registration of new entitys
        if message.topic == "/hshl/ambulances/":
            if checkNadd(split[3], AmbulanceList, Ambulance, split, locationSplit) == True:
                sub("/hshl/ambulances/", split[3], True)
            else:
                sub("/hshl/ambulances/", split[3], False)

        elif message.topic == "/hshl/firefighters/":
            if checkNadd(split[3], FirefighterList, Firefighter, split, locationSplit) == True:
                sub("/hshl/firefighters/", split[3], True)
            else:
                sub("/hshl/firefighters/", split[3], False)

        elif message.topic == "/hshl/polices/":
            if checkNadd(split[3], PoliceList, Police, split, locationSplit) == True:
                sub("/hshl/polices/", split[3], True)
            else:
                sub("/hshl/polices/", split[3], False)

        elif message.topic == "/hshl/hospitals/":
            if checkNadd(split[3], HospitalList, Hospital, split, locationSplit) == True:
                sub("/hshl/hospitals/", split[3], True)
            else:
                sub("/hshl/hospitals/", split[3], False)

        elif message.topic == "/hshl/users/":
            if checkNadd(split[3], userCarList, userCar, split, locationSplit) == True:
                sub("/hshl/users/", split[3], True)
            else:
                sub("/hshl/users/", split[3], False)
    else:
        compareNupdate(message.topic.split("/"), split,
                       locationSplit, allEntityList)

        # entity specific handling

        # Dont change anything from here!!
BROKER_ADDRESS = "mr2mbqbl71a4vf.messaging.solace.cloud"  # Adresse des MQTT Brokers
client = mqtt.Client()
client.on_connect = on_connect  # Zuweisen des Connect Events
client.on_message = on_message  # Zuweisen des Message Events

# Benutzernamen und Passwort zur Verbindung setzen
client.username_pw_set("solace-cloud-client", "nbsse0pkvpkvhpeh3ll5j7rpha")
client.connect(BROKER_ADDRESS, port=20614)  # Verbindung zum Broker aufbauen

print("Connected to MQTT Broker: " + BROKER_ADDRESS)
client.loop_forever()  # Endlosschleife um neue Nachrichten empfangen zu können
