# Aufbau des veröffentlichten PROBoters

Diese Übersicht verbindet den [Originalcode](../README.md), die
[Hardwarebeschreibung von SCHUTZWERK](https://www.schutzwerk.com/en/blog/proboter-02/)
und die [Masterarbeit von 2019](../publications/PROBoter_thesis.pdf).
Sie beschreibt den veröffentlichten Stand, keine fertig geprüfte Bauanleitung.

## Zielbild und Entwicklungsstände

Der PROBoter ist eine Plattform für die automatische Analyse bestückter
Leiterplatten. Der Stand der Blogserie von 2022 sieht bis zu **vier unabhängig
bewegliche elektrische Prüfspitzen**, eine bewegliche Kamera, eine statische
Übersichtskamera und einen Signal-Multiplexer vor. Als Arbeitsraum je Einheit
werden **300 × 200 × 30 mm (X/Y/Z)** genannt. Das Modell unter
[`hardware/3d_models/proboter.stp`](../hardware/3d_models/proboter.stp)
ist ein Solid-Edge-STEP-Export vom 19.04.2022.

Die Masterarbeit dokumentiert einen früheren Prototyp mit **zwei** fahrbaren
Einheiten und einem damals erweiterten Arbeitsraum von 420 × 200 × 50 mm.
Ihre genannten Materialkosten von etwa **2.300 €** beziehen sich auf diese
ältere Zwei-Einheiten-Version einschließlich Mehrwertsteuer, ohne Arbeitszeit.
Der Blog nennt für den späteren aufgebauten Prototyp etwa **5.000 €**
Rohmaterialkosten. Diese Zahlen sind nicht direkt vergleichbar und ersetzen
keine aktuelle Kalkulation.

## Mechanik

- Das Grundgestell besteht aus Aluminiumprofilen mit einer ausziehbaren
  Aufnahme für die zu prüfende Leiterplatte. Oben tragen laut Blog zwei
  lasergeschnittene Stahlplatten zusammen mit 60 × 30-mm-Aluminiumprofilen
  die X-Führungen. Die X-Bewegung nutzt einen beidseitig angetriebenen
  Riemen-Gantry.
- Die Prüfeinheiten bewegen Spitzen in X, Y und Z. Die veröffentlichte
  Beschreibung nennt GT2-Riemen, NEMA-14- und NEMA-17-Motoren sowie
  Linearführungen. Individuelle Formteile sind für 3D-Druck ausgelegt;
  andere Teile benötigen Zuschnitt oder Bearbeitung.
- Das STEP-Modell enthält **447 Einbauvorkommen**. Nach Abzug von
  31 Unterbaugruppen-Vorkommen bleiben **416 Blattteil-Vorkommen mit 120 Namen**.
  Diese sind vollständig in der [CAD-Teileliste](../bom/CAD-Teileliste.md)
  erfasst. Die Geometrie liegt als Gesamtbaugruppe vor; eigenständige
  Fertigungsdateien je Sonderteil und eine geprüfte Zuschnittliste fehlen.
- Die Bestückung des STEP-Modells ist nicht konsistent mit vier vollständigen
  Prüfeinheiten: Es zeigt vier SKR-Boards, aber sechs Motoren, zwei
  Prüfspitzenplatinen und zwei Z-Riemen. Diese Zählung ist eine **CAD-Beobachtung**,
  keine Vorgabe für den Aufbau.

## Sensorik, Elektronik und Optik

- Die [Original-Firmware](../firmware/README.md) ist ein
  PROBoter-spezifischer Marlin-Ableger. Sie nennt vier
  BIGTREETECH-SKR-V1.3-Boards und TMC2130-Schrittmotortreiber. Für jede der
  vier Probe-Konfigurationen muss die Firmware separat gebaut werden.
  In `Configuration.h` sind X, X2, Y und Z als TMC2130 konfiguriert;
  daraus folgen **bis zu vier Treibersteckplätze je Board**. Die tatsächlich
  benötigte Anzahl muss gegen den realen Motorplan geprüft werden.
- Im STEP erscheinen ein Mean-Well-RSP-200-24-Netzteil, zwölf induktive
  M8-Näherungsschalter und zwei optische Endschalter. Ihre elektrischen
  Schnittstellen und die komplette Verdrahtung sind nicht veröffentlicht.
- Der Blog beschreibt **ein** auf einer Prüfeinheit befestigtes USB-Mikroskop
  für zusammengesetzte Detailbilder sowie **eine** statische hochauflösende
  Kamera für die Übersicht. Im STEP sind dagegen **zwei** `usb_microscope`
  benannt. Kamera-Modelle, Linsen, Beleuchtung und Halterung der statischen
  Kamera müssen abgeglichen werden.
- Ein eigens entwickeltes Signal-Multiplexer-Board routet Prüfspitzensignale
  zu Messgeräten und ermöglicht Durchgangstests. Das STEP-Modell enthält nur
  `signal_multiplexer_dummy`; eine Schaltung, Gerber und Elektronik-BOM liegen
  im veröffentlichten Repository nicht vor. Dasselbe gilt für die
  Prüfspitzen-Platinen.
- Für die automatische Kalibrierung beschreibt der Blog eine Referenzplatte
  mit Messingzylindern; die Prozedur kann acht innere oder alle zwölf Punkte
  verwenden. Eine bestellfähige Zeichnung der Platte liegt nicht separat vor.

## Software und Daten

Die [Software-Übersicht](../software/README.md) beschreibt eine
Docker-Compose-Installation mit Web-UI, Hardwaresteuerung, Projektverwaltung,
Bild- und Signalanalyse sowie Reverse-Proxy. Die Hardwaresteuerung ist ein
Python/Quart-Dienst mit REST- und Websocket-Schnittstellen; Bild- und
Signalanalyse werden als eigene Dienste ausgeführt. Die Web-UI basiert auf
Vue. Der [fünfte Blogteil](https://www.schutzwerk.com/en/blog/proboter-05/)
erklärt die Architektur und den Analyseablauf.

Die [Bilddatensatz-Dokumentation](../image_data_sets/README.md)
beschreibt PCB-GOOGLE, PCB-INTERNAL und IC-PINS. Die großen ZIP-Dateien
und trainierten Modelle sind Git-LFS-Zeiger. Mindestens der Abruf von
`ic-pins.zip` schlägt am Upstream-Server fehl; diese Abhängigkeit ist vor einem
vollständigen Start der Bildanalyse zu klären.

## Nächster technischer Schritt

Zuerst die [offenen Punkte](Offene-Punkte.md) zu Varianten, Elektrik und
Fertigungsdaten auflösen. Danach die
[Bestellliste](../bom/Bestellliste.md) auf eine freigegebene Konfiguration
umstellen und erst dann Preise und Lieferbarkeit prüfen.
