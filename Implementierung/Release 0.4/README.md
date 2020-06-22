# Release 0.4

Der Austausch von Daten findet wird nun durch JSON realisiert. Alle Funktionen, die in vorherigen Versionen verfügbar waren sind weiterhin vorhanden. Generelle Beispiele finden sich in der Datei [TestIt.py][linkToTestIt].

## Anmelden von Entities

### Generelle Informationen
| Name | Beschreibung |
| ------ | ------ |
| driverName | Der Name der Fahrer/in |
| hospital_name| Der Name des Krankenhauses |
| location | Längen- und Breitengrad |
| isFree | Angabe, ob das Fahrzeug gerade verfügbar ist |
| doctors | Anzahl der Ärzte in dem Krankenhaus |
| id | Einzigartige Fahrzeug Id |
| freeRooms | Wie viele freie Räume gibt es |
| specialists | Liste an Spezialisten |
| reasons | Aktueller zustand |


### Topics

Zur Anmeldung von User cars wird folgendes Topic verwendet:
```python
topic = "/hshl/users/"
```

Zur Anmeldung von Hospitals wird folgendes Topic verwendet:
```python
topic = "/hshl/hospitals/"
```

Zur Anmeldung von Ambulances wird folgendes Topic verwendet:
```python
topic = "/hshl/ambulances/"
```

Zur Anmeldung von Firefighters wird folgendes Topic verwendet:
```python
topic = "/hshl/firefighters/"
```

Zur Anmeldung von Polices wird folgendes Topic verwendet:
```python
topic = "/hshl/polices/"
```

### User
Die JSON Daten müssen für die Erstellung oder das updaten von Usern **!MINDESTENS!** diese Daten enthalten:

```yaml
message = {
    "driver_name": String,
    "location": [float, float],
    "reasons": String,  
    "id": String
}
```

Ein Beispiel:

```yaml
message = {
    "driver_name": "Herrmann",
    "location": [51.3, 23.22],
    "reasons": "None",
    "id": "car1"
}
```

Das Hinzufügen von weiteren Parametern ist ohne Probleme möglich!

#### Reasons
Mögliche Reasons sind:

```python
heart_attack, accident, accident_fire, accident_oil, light_accident, hard_accident, police, ambulance, hospital, None
```

In einem weiteren Update wird es möglich sein mehrere Reasons in einem Array zu versenden.

### Hospitals

Die JSON Daten müssen für die Erstellung oder das updaten von Krankenhäusern **!MINDESTENS!** diese Daten enthalten:


```yaml
message = {
    "hospital_name": String,
    "location": [float, float],
    "doctors": int,
    "id": string,
    "freeRooms": int,
    "specialists": [String, String, ...]
}
```

Ein Beispiel:

```yaml
message = {
    "hospital_name": "Hospitalomat",
    "location": [43.3, 23.22],  
    "doctors": 12,
    "id": "hosp1",
    "freeRooms": 123,
    "specialists": ["specialist1", "specialist2"]
}
```
Das Hinzufügen von weiteren Parametern ist ohne Probleme möglich!

### Police, Ambulance, Firefighter

Die JSON Daten müssen für die Erstellung oder das updaten von Service Fahrzeugen **!MINDESTENS!** diese Daten enthalten:

```yaml
message = {
    "driver_name": String,
    "location": [float, float],  
    "isFree": bool,
    "id": string
}
```

Ein Beispiel:

```yaml
message = {
    "driver_name": "Annegret",
    "location": [33.3, 3.22],
    "isFree": True,
    "id": "amb1"
}
```
Das Hinzufügen von weiteren Parametern ist ohne Probleme möglich!

## Updaten von Entities

**IDs Können nicht verändert werden und bleiben immer gleich!**

Update des User cars mit der ID "car1"
```python
topic = "/hshl/users/car1"
```

```yaml
message = {
    "driver_name": "Herrmann",
    "location": [51.3, 23.22],
    "reasons": "accident",
    "id": "car1"
}
```
Das Updaten anderer Entities funktioniert nach demselben Prinzip.

## Zu erwartende Antowrt

Wird eine Anfrage an den Server gestellt, die bearbeitet werden kann. Wird eine Antwort in diesem Format gesendet:

```yaml
message = {
    'reasons': userReason,
    'location': location,
    'distance': distance
}
```

Ein Beispiel wäre:

```yaml
message = {
    'reasons': "accident",
    'location': [51.3,23.22],
    'distance': 889.4124848067089
}
```
## Changelog
    1. Verarbeitung der JSON Daten
    2. Kleinere Fixes
    3. Umbenennen einiger Variablen

## TBD
    1. Berechnung der Entfernung für Krankenhäuser anhand der Spezialisten und der Freien Räume
    2. Die Möglichkeit mehrere Reasons des Users zu bearbeiten



[linkToTestIt]: https://github.com/IxTzy/Interaktionskonzept/blob/master/Implementierung/Release%200.4/TestIt.py
