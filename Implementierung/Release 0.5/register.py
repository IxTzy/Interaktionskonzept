from entitys import *
from manager import *
import paho.mqtt.client as mqtt
import sys

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
Große test datei
Changed to JSON
--------------------
TBD
Auftreten und bearbeiten meherer Reasons
Code aufräumen
    doppelten code in Funktionen auslagern
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
    try:
        if state == True:
            topic = str + id
            client.subscribe(topic)
            print("Subscribed to: " + topic)
            string = "Successfully added! Channel for further Communication is: " + topic

            message = {
                "message": string,
                "isAntwort": True
            }
            client.publish(str, json.dumps(message))
            print(message)
        else:
            print(id + ": Already exists! Change the Id!")
            # client.publish(str, id + ": Already exists! Change the Id!")
        pass
    except Exception as e:
        print(e, " in Subscription Method")
        raise


def deciderData():
    returnList = [FirefighterList, AmbulanceList, PoliceList, HospitalList]
    return returnList


def on_message(client, userdata, message):
    try:
        name = ""
        location = ""
        id = ""
        reasons = ""
        doctors = ""
        freeRooms = ""
        specialists = ""
        isFree = ""

        jsonData = json.loads(message.payload)
        if "isAntwort" in jsonData:
            print("isAntwort: ", jsonData['isAntwort'])

        else:

            print("is not an Antwort")
            if message.topic.split("/")[2] == "users":
                name, location, id, reasons = messageHandling(
                    jsonData, "users")

            elif message.topic.split("/")[2] == "hospitals":
                name, location, id, doctors, freeRooms, specialists = messageHandling(
                    jsonData, "hospitals")

            elif message.topic.split("/")[2] == "firefighters":
                name, location, id, isFree = messageHandling(
                    jsonData, "entity")

            elif message.topic.split("/")[2] == "polices":
                name, location, id, isFree = messageHandling(
                    jsonData, "entity")

            elif message.topic.split("/")[2] == "ambulances":
                name, location, id, isFree = messageHandling(
                    jsonData, "entity")

            data = [name, location, id, isFree, reasons,
                    doctors, freeRooms, specialists]

            topic = message.topic

            print("TOPIC= ", topic, jsonData)

        ###########################UPDATE PROCESS#######################################
            if topic.split("/")[3] != "":
                print("update process")
                compareNupdate(message.topic.split("/"), data,
                               location, allEntityList, allEntityList, id)
    ###########################REGISTRATION PROCESS#######################################

    # Split = name latLong isFree ID
    # SPlitHosp = name latLong doctors id freeRooms specialists

            elif topic == "/hshl/ambulances/" or "/hshl/firefighters/" or "/hshl/polices/" or "/hshl/hospitals/" or "/hshl/users/":
                print("generate process")
                # if message.topic.split("/")[3] == "":
                # registration of new entitys
                if topic == "/hshl/ambulances/":
                    if checkNadd(id, AmbulanceList, Ambulance, [name, location, isFree, id], location, "amb") == True:

                        sub("/hshl/ambulances/", id, True)
                    else:
                        sub("/hshl/ambulances/", id, False)

                elif topic == "/hshl/firefighters/":
                    if checkNadd(id, FirefighterList, Firefighter, [name, location, isFree, id], location, "fire") == True:
                        sub("/hshl/firefighters/", id, True)
                    else:
                        sub("/hshl/firefighters/", id, False)

                elif topic == "/hshl/polices/":
                    if checkNadd(id, PoliceList, Police, [name, location, isFree, id], location, "pol") == True:
                        sub("/hshl/polices/", id, True)
                    else:
                        sub("/hshl/polices/", id, False)

                elif topic == "/hshl/hospitals/":
                    if checkNadd(id, HospitalList, Hospital, [name, location, doctors, id, freeRooms, specialists], location, "hosp") == True:
                        sub("/hshl/hospitals/", id, True)
                    else:
                        sub("/hshl/hospitals/", id, False)

                elif topic == "/hshl/users/":
                    if checkNadd(id, userCarList, userCar, [name, location, reasons, id], location, "user") == True:
                        sub("/hshl/users/", id, True)
                        # start the decider in the event that there is an accident
                        decider(userReason=reasons, userLocation=location, FirefighterList=FirefighterList,
                                AmbulanceList=AmbulanceList, PoliceList=PoliceList, HospitalList=HospitalList, id=id)
                    else:
                        sub("/hshl/users/", id, False)

        pass
    except Exception as e:
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        raise


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
