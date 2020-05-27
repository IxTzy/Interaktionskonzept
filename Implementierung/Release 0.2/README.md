# Release 0.2
Es können Feuerwehr, Polizei und Krankenwägen registriert werden, in dem eine Nachricht an das jeweilige Topik gesendet wird. Krankenhäuser sowie User-Fahrzeuge folgen in weitern Updates. Die Nachricht muss dabei wie folgt formatiert werden:
```python
"driverName Lat,Long isFree Id"
```
| Plugin | README |
| ------ | ------ |
| driverName | Der Name der Fahrer/in |
| Lat,Long | Längen- und Breitengrad |
| isFree | Angabe, ob das Fahrzeug gerade verfügbar ist |
| Id | Einzigartige Fahrzeug Id |



Zu beachten ist, dass die einzelnen Attribute durch Leerzeichen getrennt werden. Die Trennung des Längen- und Breitengrades erfolgt jedoch durch ein ",". Ein Beispiel würde so aussehen:
```python
"Klaus 123.50,123.55 True amb1"
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
