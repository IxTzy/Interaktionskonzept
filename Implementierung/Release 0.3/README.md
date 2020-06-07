# Release 0.3
Es können Feuerwehr, Polizei, Krankenwägen, UserCars und Krankenhäuser registriert werden, in dem eine Nachricht an das jeweilige Topik gesendet wird. Die Nachricht muss dabei wie folgt für Feuerwehr, Polizei und Krankenwägen formatiert werden:
```python
"driverName Lat,Long isFree Id"
```
Für Krankenhäuser muss folgende Formatierung verwendet:
```python
"HospitalName Lat,Long Doctors Id freeRooms specialists"
```
Für UserCars ergibt sich folgende Formatierung:
```python
"driverName lat,long reason Id"
```
| Plugin | README |
| ------ | ------ |
| driverName | Der Name der Fahrer/in |
| Lat,Long | Längen- und Breitengrad |
| isFree | Angabe, ob das Fahrzeug gerade verfügbar ist |
| Doctors | Anzahl der Ärzte in dem Krankenhaus |
| Id | Einzigartige Fahrzeug Id |
| freeRooms | Wie viele freie räume gibt es |
| specialists | Liste an spezialisten |
| reason | Aktueller zustand |

Beispiele für Krankenhaus und UserCar:

```python
"HospitalMcBrokenFinger 56.2296756,5.0122287 12 hops5 123 einExpter,Nocheiner,UndNochEiner"

"Klaus 22.2296756,28.0122287 heart_attack abc5"
```


Zu beachten ist, dass die einzelnen Attribute durch Leerzeichen getrennt werden. Die Trennung des Längen- und Breitengrades erfolgt jedoch durch ein ",". Ein Beispiel würde so aussehen:
```python
"Kleemens 123.50,123.55 True amb1"
```
Diese Nachricht wird auf einem der allgemeinen Kanäle versendet.
```python
"/hshl/ambulances/", "/hshl/polices/", ....
```
Wurde ein Fahrzeug hinzugefügt, wird ein neuer Kommunikationskanal geöffnet, über den die zukünftige Kommunikation für dieses Fahrzeug abgewickelt wird. Die Adresse des neuen Kanals ist die Adresse des allgemeinen Kanals + die Id des Fahrzeuges:
```python
"/hshl/ambulances/amb1"
```
Bei Aktualisierungen werden die Daten über diesen Kanal im selben Format wie bei der Anmeldung versendet.

Entfernungen und die Position des UserCars bei entsprechender Reason werden über den Kommunikationskanal zurückgegeben. Eine Antwort auf dem Kanal sieht wie Folgt aus:

```python
"Send: User reason: heart_attack. User Location: [22.2296756, 28.0122287]. Distance: 3339.6181455116725 to: /hshl/ambulances/abc2"
```
### Changelog
    1. Support für UserCars sowie Krankenhäuser
    1.1 Update Funktionalität für Krankenhäuser und UserCars
    2. Berechnung der Entfernung
    3. Handling der verschiedenen Situationen
    4. Implementierung der Alarm Funktion
### TBD
    1. Berechnung der Entferung für Krankenhäuser anhand der Spezialisten und der Freien Räume
    2. Aktualisieren des isFree Attributes durch die Alarm Funktion
