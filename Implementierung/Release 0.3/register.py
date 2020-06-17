from entitys import *
from manager import *
import paho.mqtt.client as mqtt


'''
DONE
User Creation !!!1!!!!elf!!!
Krankenhaus verwaltung
    update und anlegen
User verwaltung
    update und anlegen
Daten verarbeitung
    Entfernungsbestimmung
Handling der verschienden Situationen
    decider Methode
User update überwachung
Alarm Funktion
--------------------
TBD
Variablen umbennen
Code aufräumen
    doppelten code in Funktionen auslagern
Große test datei
Hospital Handling
    unterscheidung welches krankenhaus welche spezialisten hat
    wie viele freie räume gibt es
Alarm funktion um update der variablen erweitern
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
        client.subscribe(str + id, 2)
        topic = str + id
        print("Subscribed to: " + topic)

        client.publish(
            str, ": Successfully added! Channel for further Communication is: " + topic)
    else:
        client.publish(str, id + ": Already exists! Change the Id!")


def deciderData():
    returnList = [FirefighterList, AmbulanceList, PoliceList, HospitalList]
    return returnList


def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))  # Nachricht Dekodieren
    # Nachricht bei leerzeichen splitten

    split = str(msg).split(" ")
    locationSplit = split[1].split(",")
    # convert to float
    locationSplit[0] = float(locationSplit[0])
    locationSplit[1] = float(locationSplit[1])

    # Convert isFree argument from string to bool when its not an Hospital or a User
    if message.topic.split("/")[2] != "hospitals" and message.topic.split("/")[2] != "users":
        if split[2] == "True":
            split[2] = True
        else:
            split[2] = False
    # Create a list out of the specialists and save it to [5] in split
    elif message.topic.split("/")[2] == "hospitals":
        split[5] = split[5].split(",")

###########################REGISTRATION PROCESS#######################################
    print("asajsdjasd:" + split[3])
    if message.topic.split("/")[3] == "":
        # registration of new entitys
        if message.topic == "/hshl/ambulances/":
            if checkNadd(split[3], AmbulanceList, Ambulance, split, locationSplit, False) == True:
                sub("/hshl/ambulances/", split[3], True)
            else:
                sub("/hshl/ambulances/", split[3], False)

        elif message.topic == "/hshl/firefighters/":
            if checkNadd(split[3], FirefighterList, Firefighter, split, locationSplit, False) == True:
                sub("/hshl/firefighters/", split[3], True)
            else:
                sub("/hshl/firefighters/", split[3], False)

        elif message.topic == "/hshl/polices/":
            if checkNadd(split[3], PoliceList, Police, split, locationSplit, False) == True:
                sub("/hshl/polices/", split[3], True)
            else:
                sub("/hshl/polices/", split[3], False)

        elif message.topic == "/hshl/hospitals/":
            # The additional True Argument is used to recognize that its an hospital!
            if checkNadd(split[3], HospitalList, Hospital, split, locationSplit, "hosp") == True:
                sub("/hshl/hospitals/", split[3], True)
            else:
                sub("/hshl/hospitals/", split[3], False)

        elif message.topic == "/hshl/users/":
            if checkNadd(split[3], userCarList, userCar, split, locationSplit, "user") == True:
                sub("/hshl/users/", split[3], True)
                # start the decider in the event that there is an accident before registration
                decider(userReason=split[2], userLocation=locationSplit, FirefighterList=FirefighterList,
                        AmbulanceList=AmbulanceList, PoliceList=PoliceList, HospitalList=HospitalList)
            else:
                sub("/hshl/users/", split[3], False)


###########################UPDATE PROCESS#######################################

    else:
        compareNupdate(message.topic.split("/"), split,
                       locationSplit, allEntityList, allEntityList)

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
