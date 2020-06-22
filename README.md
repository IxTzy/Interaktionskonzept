# Implementierung
[Release 0.1][rel01] 
<br>
[Release 0.2][rel02]
<br>
[Release 0.3][rel03]
<br>
[Release 0.4][rel04]
<br>
[Registration Process Diagramm][rp]
<br>
[User Reason Diagramm][ur]
<br>
[Requirements][req]
<br>

# Interaktionskonzept Seminar
Das Ziel des Projektes ist es die entstehenden Anfragen mit den jeweiligen Daten situationsbedingt zu bearbeiten. Dazu soll es definierte Schnittstellen für verschiedene Services geben die über MQTT kommunizieren.

## Functional Requirements DE
FREQ00 - Die Kommunikation muss über definierte Topics stattfinden <br/>
FREQ01 - Die Anwendung muss online verfügbar sein <br/>
FREQ02 - Es muss ein Exception Handling geben </br>
FREQ03 - Die Anwendung muss Entfernungen berechnen können </br>
FREQ04 - Die Anwendung muss eine Liste über verfügbare Ressourcen führen </br>
FREQ05 - Die Anwendung muss situationsbedingt entscheiden können </br>
FREQ06 - Falsche Anfragen müssen eine Fehlermeldung als Antwort haben </br>

## Functional Requirements EN
FREQ00 - Communication must take place via defined topics <br/>
FREQ01 - The application must be available online <br/>
FREQ02 - There must be exception handling </br>
FREQ03 - The application must be able to calculate distances </br>
FREQ04 - The application must keep a list of available resources </br>
FREQ05 - The application must be able to decide depending on the situation </br>
FREQ06 - Wrong requests must have an error message as an answer </br>

## Non Functional Requirements DE
NFREQ00 - Die Kommunikation muss über ein Protokoll stattfinden <br/>

## Non Functional Requirements EN
NFREQ00 - Communication must take place over a protocol <br/>


## Diagramme
### Use Case Diagram

![useCasePicutre](/Doku/Diagramme/usecase_svg.svg)

### Sequence Diagram
![SequnceDiagram](/Doku/Diagramme/sequence_svg.svg)


[rel01]: https://github.com/IxTzy/Interaktionskonzept/tree/master/Implementierung/Release%200.1
[rel02]: https://github.com/IxTzy/Interaktionskonzept/tree/master/Implementierung/Release%200.2
[rel03]: https://github.com/IxTzy/Interaktionskonzept/tree/master/Implementierung/Release%200.3
[rel04]: https://github.com/IxTzy/Interaktionskonzept/tree/master/Implementierung/Release%200.4
[rp]: https://github.com/IxTzy/Interaktionskonzept/blob/master/Doku/Diagramme/RegistrationProcess.pdf
[ur]: https://github.com/IxTzy/Interaktionskonzept/blob/master/Doku/Diagramme/UserReason.pdf
[req]: https://github.com/IxTzy/Interaktionskonzept/blob/master/Doku/Requirements/README.md
