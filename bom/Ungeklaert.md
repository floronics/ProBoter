# Offene Teile und Klärungsbedarf

Die Liste enthältjede offene Position, auch teilweise bekannte Standardteile. Eine unbekannte Schaltung lässt sich nicht aus einer äußeren STEP-Hülle rekonstruieren.

## nicht identifiziert

| ID / Teil | Bedarf | Nächsterkonkreter Schritt |
| --- | --- | --- |
| CAD-010 Schubladen-Dummyplatte | 1 Stück | Schubladen-Dummy 564×410×12 mm: unklar, ob reale Platte benötigt und welches Material. Nicht stillschweigend ausschließen oder aus Stahl fertigen. |

## Fertigung noch offen

| ID / Teil | Bedarf | Nächsterkonkreter Schritt |
| --- | --- | --- |
| CAD-003 Grundgestell: Rückseite Platte | 1 Stück | 650×270×3 mm, 54 Bohrungen Ø3,4, 10 Bohrungen Ø4,5, 1 Bohrung Ø8. 6 Ø4,5-Bohrungen sitzen auf den langen Profilen (M4 + Nutenstein, siehe M01). Zuschnitt und Bohrungen intern; Zeichnung aus CAD ableiten. |
| CAD-070 Platine Halter rechteckig Stange | 2 Stück | ABWEICHUNG (Entscheidung Luis 17.10.2026): CAD-Vierkantrohr 11,5×11,5×1,5×205 mm (Fusion-Messung) wird durch Alu-Vierkantrohr 12×12×1 mm ersetzt (keine Last; 12×12×1,5 in DE/EU nicht gefunden); gedruckte Schieber CAD-067 auf 12 mm anpassen. Bezugsquelle z. B. e Bay metalexpres (Al Mg Si 0,5, ab 500 mm), Preis und Lager noch prüfen. |
| CAD-075 Prüfspitzen-PCB, unbestückt | 4 Stück | 4 Stück; CAD nur Quader 26,67×10,96×1,6 mm ohne Daten. Entscheidung Luis 17.10.2026: Originaldaten bei SCHUTZWERK angefragt (Anfrage durch Luis versendet, Antwort offen). |
| CAD-096 X-Achse Motor Platte | 1 Stück | 5 mm Stahl, 550×135 mm. Fusion-Messung: 16 Kernlöcher Ø2,46 für M3-Gewinde (Riemenspanner), Senkungen für M6 und Ø22-Durchbrüche für die Motoren. Kontur und Bohrungen aus CAD; Gewinde und Senkungen intern. Zeichnung mit Lagetoleranzen der Führungsbohrungen fehlt. |
| CAD-097 X-Achse Motor Platte 2 | 1 Stück | 5 mm Stahl, 550×135 mm. Fusion-Messung: 16 Kernlöcher Ø2,46 für M3-Gewinde (Riemenspanner), Senkungen für M6 und Ø22-Durchbrüche für die Motoren. Kontur und Bohrungen aus CAD; Gewinde und Senkungen intern. Zeichnung mit Lagetoleranzen der Führungsbohrungen fehlt. |
| CAD-099 X-Achse Seite Platte | 4 Stück | 5 mm Seitenplatte des X-Wagens 55×166,5 mm. Fräszeichnung aus hardware/cad (.par/.dft) ableiten. |
| CAD-100 X-Achse Seite Platte beweglich | 4 Stück | 5 mm Seitenplatte des X-Wagens 55×166,5 mm. Fräszeichnung aus hardware/cad (.par/.dft) ableiten. |
| SYS-003 Signal-Multiplexer, unbestückte Leiterplatte | 1 Stück | SCHUTZWERK-Original: 4 Lagen, Gerber hardware/signal-multiplexer/hardware/gerber 1.1/gerber 1.1.zip (deckungsgleich mit mux.kicad_pcb, geprüft 26.10.2026). Bei JLCPCB bestellen. |
| SYS-004 Kalibrier-Referenzplatte, Alu schwarz | 1 Stück | WERKSTATT (Entscheidung Luis 18.10.2026): Alu gefräst/gebohrt, schwarz eloxiert oder lackiert. Dicke 5,1 mm (cli.py); Größe ca. 130×110 mm aus software/docu/images/calibration_plate_top.png geschätzt. 4 Türme für die erhöhten Stifte; Marker eingraviert. Zeichnung aus den Software-Maßen erstellen. |
| SYS-019 Sensor-Pegelanpassung / Eingangsschutz | 24 Kanäle | Bedarf abhängig von M8-Ausgang; 24 V/3,3 V-Interface. Keine Schaltung/BOM vorhan den; nicht blind 24Module bestellen. |
| SYS-023 Signal-Multiplexer Bestückung | 1 Baugruppe | Board-BOM hardware/signal-multiplexer/hardware/mux.csv (76 Bauteile, u. a. 6 Relais TE 6-1462037-3, SMA, USB-B, DB9). Bestückung bei JLCPCB oder selbst; MPNs/LCSC-Nummern noch zuordnen. |
| SYS-024 Prüfspitzen-PCB Bestückung | 4 Baugruppen | CAD-MM CX/Federkontakte separat; zusätzliche Buchsen und Bauteile erst aus Schaltplan. Unbestückte Platine CAD-075 nicht erneut zählen. |
| SYS-026 Zielplatinen-Versorgungscontroller | 1 Baugruppe | Softwareziel /dev/proboter_target-power-controller; Schaltung, Firmware/Hardware und Kabel fehlen. Separat vom RSP-Netzteil. |

## teilweise geklärt

| ID / Teil | Bedarf | Nächsterkonkreter Schritt |
| --- | --- | --- |
| CAD-009 Grundgestell: Schlepp Energiekette Halter | 4 Stück | Fusion-Messung: Alu-Flachprofil 16×80×650 mm (932 mm², 2 Kerne Ø5) mit 18 M3-Gewinden. Kandidat DOLD 80x 16S I-Typ Nut 8 (60886-Z), gleiche Serie wie CAD-103, aber 813 mm² und laut Produktseite M8-Kern. Kerngröße an der DOLD-Zeichnung prüfen; M3-Gewinde in der Werkstatt. |
| CAD-058 ISO 8673 Mutter M8 | 53 Stück | Norm und Maße mit CAD abgeglichen; Artikel 24122 08 1. A4 statt A2; H 6,5 statt 6,8. Datenblatt nennt Linksgewinde, vermutlich Datenfehler: vor Bestellung klären. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026). ISO 8673 M8×1 passt zu den M8×1-Gewinden der induktiven Sensoren. Sensoren liefern meist 2 Muttern mit; dann nur Reserve kaufen. |
| CAD-061 MMCX-Stecker gerade mit RG316, offenes Ende | 4 Stück | Fusion: MMCX-Stecker mit Kabel Ø2,5 = RG316. rf-connectors.pl liefert MMCX-Pigtails RG316 offen nur bis 30 cm; 1 m nur mit SMA-Gegenstecker (abschneiden) oder als Sonderanfertigung. Länge an Kette/Messgerät festlegen. |
| CAD-062 MMCX-Stecker gewinkelt mit RG316, offenes Ende | 4 Stück | rf-connectors.pl PT_MMCX MLS030Q: gewinkelt, RG316, offen, 30 cm, 33,95 zł. Für 1–1,5 m Sonderlänge anfragen oder MMCX–SMA 1 m kürzen. |
| CAD-073 Aufnahmehülse R75 mit Drahtende (CAD: P75-2_W) | 8 Stück | Fusion-Messung: Ø1,2 × 25,4 mm, Drahtende Ø0,6 × 5 mm = R75-Aufnahmehülse für P75 (Bohrung ca. 1,4 mm). Kein EU-Angebot mit Preis gefunden; Peaktest R75-Serie nur auf Anfrage. |
| SYS-001 TMC2130 SPI Treibermodule | 16 Stück | 4 je SKR für X/X2/Y/Z. RBS13024: 4 Treiber mit Kühlkörpern und Kabel, SPI-Pins laut Fotos vorgelötet. Revision nicht angegeben; SPI-Modus laut Datenblatt per Lötbrücke CFG4/CFG5 prüfen. |
| SYS-002 Stationäre Übersichtskamera ELP-USBFHD01M-H100 | 1 Stück | Gewählt (Luis 17.10.2026): ELP-USBFHD01M-H100, 1080p, UVC, 100°, Preis auf Anfrage; Lochraster beim Kauf bestätigen. Fusion-Messung: Halter CAD-025 hat 4 M2-Bohrungen im Raster 28×28 mm = 32×32-mm-USB-Platinenkamera (z. B. ELP, 1080p, UVC, M12-Objektiv), keine Webcam (Entscheidung Luis 17.10.2026). Logitech C920 passt nicht. |
| SYS-009 LED-Anschluss an den Heizbett-Ausgang der Licht-Steuerplatine | 1 Satz | Configuration_adv.h:4396 setzt PROBOTER_LIGHT_CONTROL_PIN auf HEATER_BED_PIN; M376 steuert Helligkeit. Kein separater USB-LED-Controller nötig. Stecker/Leitungen, Strom und Flimmern prüfen; keine zusätzliche MOSFET-Platine pauschal kaufen. |
| SYS-010 USB-Hub 7Port aktiv | 1 Stück | Steuergeräte am Hub; zwei separate Kamera-Hostports vorausgesetzt. Netzteil und Hubkabel enthalten. |
| SYS-011 USB-Kabel für 4 SKR | 4 Stück | Host USB-A auf Board USB-B bestätigen; Länge vorläufig 2 m je Board, Ports/Verlegung prüfen. |
| SYS-012 USB-Kabel für MUX/UART/Zielversorgung | 3 Stück | 3 Verbindungen aus Softwarekonfiguration, Geräteseite und enthaltene Kabel offen; nur nach Geräteauswahl kaufen. |
| SYS-013 Bewegliche Kameraleitung / USB-Verlängerung | 1 Stück | Schleppkettengeeignete Leitung/Länge/Stecker offen; Kamera-Beipack gegenrechnen. |
| SYS-014 Motorleitungen 4adrig | 32 m | Plan 16×2 m; Schleppkettenradius, Querschnitt/Strom, Aderfarben und reale Wege offen. |
| SYS-015 Motor-Gegenstecker und Crimpkontakte | 32 Satz | Plan 2 Enden je 16 Motoren. Board-/Motorhersteller-Raster und Kontaktzahl prüfen; beiliegende Kabel abziehen. |
| SYS-017 Sensor-Gegenstecker und Kontakte | 28 Satz | 24 induktiv+4 optisch; bei steckerfertigem Beipack reduzieren. Keine generischen JST/Dupont ohne Rasterprüfung. |
| SYS-018 24-V-Verteilung, Sicherungen, Klemmen, Leitungen | 1 Satz | 4 Controller+Sensoren+LED; Last/Stromlaufplan, Aderquerschnitte und Sicherungswerte bestimmen. |
| SYS-020 Netzeinspeisung, Leitung, Sicherung und Zugentlastung | 1 Satz | 230 V-Anschluss an offenes Netzteil: Anschlussmodul, Netzleitung, Sicherungshalter und geschützter Kabelweg planen. |
| SYS-021 Schutzleiter, Ringkabelschuhe und Klemmenabdeckung | 1 Satz | Metallrahmen/Netzteil erden; Querschnitt, Anschlusspunkte und Prüfverfahren in Stromlaufplan dokumentieren. |
| SYS-022 Messkoax und instrumentenseitige Adapter | 4 Kanäle | Vorhan dene Messgeräte verwenden; BNC/SMA/MMCX und Impedanz gerätespezifisch. CAD-MM CX-Stecker 61/62 sind separat, hier nur Kabel und Instrumentadapter. |
| SYS-025 USB-UART-Adapter | 1 Stück | Software setzt Adapter voraus; Pegel, Isolation, Pinout und Zielversorgung prüfen; Laborausstattung ggf. gegenrechnen. |
| SYS-029 Profil-Nutensteine und Zusatzbefestigung | 1 Satz | Nut 6/Profilserie klären; 26Winkel plus Halter. CAD-Vierkantmuttern 29/30 und mitgelieferte Winkelsätze abziehen. |
| SYS-030 Scheiben, Sicherungselemente, Distanzteile | 1 Satz | Ergänzungsbedarf je Verschraubung/Idler; CAD-Normteile und Sensor-Beipack abziehen. Stückzahlen noch offen. |
| SYS-031 Lötzinn, Schrumpfschlauch, Binder, Labels, Kleber | 1 Satz | Verbrauchsmaterialbudget; vorhan dene Bestände später abziehen. Werkzeuge nicht enthalten. |
| SYS-032 Controller-Befestigung und Kühlung | 1 Satz | Abstandshalter, Isolierung, ggf.Lüfter; SKR/TMC-Beipack und thermische Auslegung prüfen. |
| SYS-038 Kalibrier-Kontaktleitungen und gemeinsame Messreferenz | 1 Satz | 4 SKR-Zentriereingänge P0_17 mit Pull-up/aktiv Low sowie Referenzkörper/Kontaktkreis verdrahten. Netzplan, Stecker, Länge und Bezugspotenzial mit Multiplexer klären; keine Verbindung ungeprüft festlegen. |
| SYS-058 Prüfstifte P75 Flachspitze zum Bestromen von Pads (Spitzenauswahl) | 10 Stück | Wunsch Luis (17.10.2026). Flachspitzen-Code uneinheitlich (Peaktest: F flach, A konkav, D2 Kuppe); kein Lagerangebot gefunden, Spitzenzeichnung beim Händler anfordern. |

## Reihenfolge zum Schließen der Lücken

1. Originalschaltpläne/BOM/Gerber für Multiplexer, Prüfspitzen und Zielversorgung beschaffen oder Neu-Entwicklungfestlegen; daraus Sensorinterface, Gegensteckerund Kabel ableiten.
2. NEMA14-Alternativlagen prüfen; eine vierachsige Probe mechanisch/elektrisch verifizieren. SKR1.3-Verfügbarkeit bzw.Firmwaremigration entscheiden.
3. Original-CPC/HIWIN-Paarungen und Motorlieferbarkeit anbieten lassen; keine Mischungungeprüfter Nachbauten.
4. Mikroskop bei 100 mm Arbeitsabstand und statische Kamera unter Linux prüfen; Halter danach festlegen.
5. Fertigungszeichnungen mit Werkstoffen/Passungen erstellen; Kalibrierboardgeometrie aufeine Softwareversionfestlegen.
6. Kabelwege und Kettenbelegung messen, Stromlaufplan abschließen, Beipack-Normteile abgleichen und Warenkörbe finalisieren.

Anfragen wurdennicht versandt.
