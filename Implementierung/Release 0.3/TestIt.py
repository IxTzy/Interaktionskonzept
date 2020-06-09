import paho.mqtt.client as mqtt
import time
import random
import string
# Methode um Daten zu senden


def sendData():
    topic = "/hshl/ambulances/"  # Das Topic in dem gesendet werden soll
    # Die Daten die gesendet werden sollen
    payLoad = "klaus 52.2296756,25.0122287 True abc2"
    print("sendet")
    client.publish(topic, payLoad)

    topic = "/hshl/firefighters/"  # Das Topic in dem gesendet werden soll
    # Die Daten die gesendet werden sollen
    payLoad = "Günter 50.2296756,29.0122287 True fire2"
    print("sendet")
    client.publish(topic, payLoad)

    topic = "/hshl/polices/"  # Das Topic in dem gesendet werden soll
    # Die Daten die gesendet werden sollen
    payLoad = "kleemens 51.2296756,7.0122287 True pol2"
    print("sendet")
    client.publish(topic, payLoad)

    topic = "/hshl/hospitals/"  # Das Topic in dem gesendet werden soll
    # Die Daten die gesendet werden sollen
    payLoad = "HospitalMcBrokenFinger 56.2296756,5.0122287 12 hops5 123 einExpter,Nocheiner,UndNochEiner"
    print("sendet")
    client.publish(topic, payLoad)

    topic = "/hshl/users/"  # Das Topic in dem gesendet werden soll
    # Die Daten die gesendet werden sollen
    payLoad = "klaus 22.2296756,28.0122287 accident abc5"
    print("sendet")
    client.publish(topic, payLoad)


# Event, dass beim Verbindungsaufbau aufgerufen wird


def on_connect(client, userdata, flags, rc):
    sendData()  # Aufruf der Senden Methode


# Dont change anything from here!!
BROKER_ADDRESS = "mr2mbqbl71a4vf.messaging.solace.cloud"  # Adresse des MQTT Brokers
client = mqtt.Client()

client.on_connect = on_connect  # Zuweisen des Connect Events
# Benutzernamen und Passwort zur Verbindung setzen
client.username_pw_set("solace-cloud-client", "nbsse0pkvpkvhpeh3ll5j7rpha")
client.connect(BROKER_ADDRESS, port=20614)  # Verbindung zum Broker aufbauen

print("Connected to MQTT Broker: " + BROKER_ADDRESS)
client.loop_forever()  # Endlosschleife um neue Nachrichten empfangen zu können
