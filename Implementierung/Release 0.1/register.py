from entitys import *
from manager import *
import paho.mqtt.client as mqtt
import time
import datetime


FirefighterList = []
AmbulanceList = []
PoliceList = []
userCarList = []
HospitalList = []
# Event, dass beim Verbindungsaufbau aufgerufen wird


def on_connect(client, userdata, flags, rc):
    # Abonnieren des Topics (Hier die jeweiligen Topics einfügen die vorgegeben sind)
    client.subscribe('/hshl/ambulances/')
    print("subscribed to the ambulances topic")
    client.subscribe('/hshl/firefighters/')
    print("subscribed to the firefighters topic")
    client.subscribe('/hshl/polices/')
    print("subscribed to the polices topic")
    client.subscribe('/hshl/hospitals/')
    print("subscribed to the hospitals topic")
    client.subscribe('/hshl/users/')
    print("subscribed to the users topic")


def sup(x):
    client.subscribe(x)
    print("subbed to: ", x)


def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))  # Nachricht Dekodieren
    # Nachricht bei leerzeichen splitten
    split = str(msg).split(" ")
    locationSplit = split[1].split(",")
    locationSplit[0] = float(locationSplit[0])
    locationSplit[1] = float(locationSplit[1])
    split[2] = bool(split[2])

    if split[3][0] == "a":
        if checkNadd(split[3], AmbulanceList, Ambulance, split, locationSplit) == True:
            sup("/hshl/ambulances/" + split[3])

    elif split[3][0] == "f":
        if checkNadd(split[3], FirefighterList, Firefighter, split, locationSplit) == True:
            sup("/hshl/firefighters/" + split[3])

    elif split[3][0] == "p":
        if checkNadd(split[3], PoliceList, Police, split, locationSplit) == True:
            sup("/hshl/polices/" + split[3])

    elif split[3][0] == "h":
        if checkNadd(split[3], HospitalList, Hospital, split, locationSplit) == True:
            sup("/hshl/hospitals/" + split[3])

    elif split[3][0] == "u":
        if checkNadd(split[3], userCarList, userCar, split, locationSplit) == True:
            sup("/hshl/users/" + split[3])

            # Hier die Verarbeitung der Nachricht einfügen

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
print("221")
