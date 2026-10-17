# Offene Teile und Klärungsbedarf

Die Liste enthältjede offene Position, auch teilweise bekannte Standardteile. Eine unbekannte Schaltung lässt sich nicht aus einer äußeren STEP-Hülle rekonstruieren.

## nicht identifiziert

| ID / Teil | Bedarf | Nächsterkonkreter Schritt |
| --- | --- | --- |
| CAD-010 Schubladen-Dummyplatte | 1 Stück | Schubladen-Dummy 564×410×12 mm: unklar, ob reale Platte benötigt und welches Material. Nicht stillschweigend ausschließen oder aus Stahl fertigen. |
| CAD-055 Induktiver Näherungsschalter M8, Bauhülle 60 mm | 24 Stück | 24 CAD-Vorkommen. MPN, Schaltabstand, NPN/PNP, NO/NC, Versorgung, Pegel und Kabellänge fehlen.24 V nicht direkt an SKR-Eingänge; Interface CAD-unabhängig SYS-019. |
| CAD-061 MMCX-Stecker gerade / Messleitung | 4 Stück | 4 CAD-Modelle enthalten Kabelansätze. Impedanz, Kabeltyp, Crimp/Lötanschluss, Gegenstecker und Länge unbekannt. |
| CAD-062 MMCX-Stecker gewinkelt / Messleitung | 4 Stück | 4 CAD-Modelle; Kabel-/Buchsenpaarung mit CAD-061/075 und Multiplexer offen. |
| CAD-073 Prüfkontakt-Hülse P75-2 W | 8 Stück | 8 Stück, CADØ1,2×25,4 mm. Hersteller und passender Federkontakt CAD-115 unklar; Kontaktpaar vollständig spezifizieren. |
| CAD-086 Bedientaster/-schalterØ19 mm | 1 Stück | Schaltfunktion rastend/tastend, Kontaktlast, Beleuchtung und Zuordnung zu Versorgung/Software unbekannt. |
| CAD-115 Federkontakt der Prüfspitze | 8 Stück | 8 Stück, CADØ1×16,6 mm. Spitzenform, Hub, Federkraft, Kontaktmaterial und Paarung mit P75-2-W unklar. |

## Fertigung noch offen

| ID / Teil | Bedarf | Nächsterkonkreter Schritt |
| --- | --- | --- |
| CAD-003 Grundgestell: Rückseite Platte | 1 Stück | 650×270×3 mm, 54 Bohrungen Ø3,4, 10 Bohrungen Ø4,5, 1 Bohrung Ø8. 6 Ø4,5-Bohrungen sitzen auf den langen Profilen (M4 + Nutenstein, siehe M01). Zuschnitt und Bohrungen intern; Zeichnung aus CAD ableiten. |
| CAD-007 Grundgestell: Abdeckung lang Seite | 2 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-008 Grundgestell: Abdeckung oben | 2 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-009 Grundgestell: Schlepp Energiekette Halter | 4 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-016 Grundgestell: Platte Adapter 1 | 2 Stück | 10 mm Platte mit Stufen auf 5 mm und 90°-Senkungen; trägt die X-Riemenantriebe. Fräsen oder aus zwei 5-mm-Platten. Zeichnung aus CAD ableiten. |
| CAD-017 Grundgestell: Platte Adapter 2 | 2 Stück | 10 mm Platte mit Stufen auf 5 mm und 90°-Senkungen; trägt die X-Riemenantriebe. Fräsen oder aus zwei 5-mm-Platten. Zeichnung aus CAD ableiten. |
| CAD-018 Grundgestell: Platte Adapter links | 2 Stück | 10 mm Platte mit Stufen auf 5 mm und 90°-Senkungen; trägt die X-Riemenantriebe. Fräsen oder aus zwei 5-mm-Platten. Zeichnung aus CAD ableiten. |
| CAD-019 Grundgestell: Platte Adapter rechts | 2 Stück | 10 mm Platte mit Stufen auf 5 mm und 90°-Senkungen; trägt die X-Riemenantriebe. Fräsen oder aus zwei 5-mm-Platten. Zeichnung aus CAD ableiten. |
| CAD-024 Kabel Abdeckung | 4 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-026 Kamera Halter oben | 1 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-070 Platine Halter rechteckig Stange | 2 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-075 Prüfspitzen-PCB, unbestückt | 4 Stück | 4 Stück;26,67×10,96×1,6 mm Hülle. Schaltplan, Kupfer, Bohrungen, Gerber und Bestückungsdaten fehlen. Bestückung SYS-024 separat. |
| CAD-093 X-Achse Endschalter oben lang | 4 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-094 X-Achse Endschalter oben kurz | 4 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-096 X-Achse Motor Platte | 1 Stück | 5 mm Stahl, 550×135 mm. Fusion-Messung: 16 Kernlöcher Ø2,46 für M3-Gewinde (Riemenspanner), Senkungen für M6 und Ø22-Durchbrüche für die Motoren. Kontur und Bohrungen aus CAD; Gewinde und Senkungen intern. Zeichnung mit Lagetoleranzen der Führungsbohrungen fehlt. |
| CAD-097 X-Achse Motor Platte 2 | 1 Stück | 5 mm Stahl, 550×135 mm. Fusion-Messung: 16 Kernlöcher Ø2,46 für M3-Gewinde (Riemenspanner), Senkungen für M6 und Ø22-Durchbrüche für die Motoren. Kontur und Bohrungen aus CAD; Gewinde und Senkungen intern. Zeichnung mit Lagetoleranzen der Führungsbohrungen fehlt. |
| CAD-099 X-Achse Seite Platte | 4 Stück | 5 mm Seitenplatte des X-Wagens, im Original lasergeschnitten. Zeichnung aus CAD ableiten. |
| CAD-100 X-Achse Seite Platte beweglich | 4 Stück | 5 mm Seitenplatte des X-Wagens, im Original lasergeschnitten. Zeichnung aus CAD ableiten. |
| CAD-103 X-Achse Schlitten Versteifung Träger | 4 Stück | Profil 16×40, 436 mm, CAD-Querschnitt 446 mm², Kernbohrungen Ø2,46/Ø5. Kein passendes Nut-5-Profil gefunden (Recherche 17.10.2026); Kandidat norelem 16×40 Typ I hat Nut 8. Profil identifizieren. |
| SYS-003 Signal-Multiplexer, unbestückte Leiterplatte | 1 Stück | CAD-082 ist nur Platzhalter. Schaltplan/Gerber/Board-BOM fehlen; USB/9600Baud-Protokoll ist keine Schaltung. |
| SYS-004 Kalibrier-Referenzkörper / Platte | 1 Stück | Geometrie mit aktueller Software festlegen; Plattendicke 5,1 mm ist Konfigurationswert, keine validierte Zeichnung. |
| SYS-005 Innere Messing-Referenzzylinder | 4 Stück | Je 1×Ø7/8/9/10 mm nach Reference Board.inner_brass_pin_position_map; Raster 11,95×19,95 mm. Endfläche auf Bezugsebene; Gesamtlänge, Einbau, Toleranzen und Messprotokoll fehlen. |
| SYS-006 Kalibriermarker / matte Druckvorlage | 1 Satz | 4 Hamming-Marker mit IDs 1/3/6/12 laut Reference Board, je 18,2×18,2 mm, Raster 60×80 mm. Mtracker-Format verwenden, keine beliebigen Ar Uco-Marker. Maßstab 1:1 und reale Abstände vermessen. |
| SYS-019 Sensor-Pegelanpassung / Eingangsschutz | 24 Kanäle | Bedarf abhängig von M8-Ausgang; 24 V/3,3 V-Interface. Keine Schaltung/BOM vorhan den; nicht blind 24Module bestellen. |
| SYS-023 Signal-Multiplexer Bestückung | 1 Baugruppe | MCU, USB/Versorgung, Schalter/Relais, Schutz, Stecker, Passives und Montage nach noch fehlendem Schaltplan. Keine Stückzahlen erfinden. |
| SYS-024 Prüfspitzen-PCB Bestückung | 4 Baugruppen | CAD-MM CX/Federkontakte separat; zusätzliche Buchsen und Bauteile erst aus Schaltplan. Unbestückte Platine CAD-075 nicht erneut zählen. |
| SYS-026 Zielplatinen-Versorgungscontroller | 1 Baugruppe | Softwareziel /dev/proboter_target-power-controller; Schaltung, Firmware/Hardware und Kabel fehlen. Separat vom RSP-Netzteil. |
| SYS-037 Weiße äußere Kalibrierreferenzen | 4 Stück | Reference Board Config beschreibt vier äußere weiße Referenzpins. Raster 109,9×89,8 mm; Durchmesser, Höhe, Material und Umsetzung am gewählten Board fehlen. Nicht mit 12Messingpins gleichsetzen. |
| SYS-039 Erhöhte Messing-Referenzzylinder | 4 Stück | Ø7 mm laut Reference Board-Skizze; Code setzt vier Endflächen 6/8/10/12 mm über Bezugsebene auf Raster 59,6×39,9 mm. Gesamtlängen und Einstecktiefe sind nicht diese Höhen; Zeichnung und Toleranzen fehlen. |
| SYS-040 Äußere flache Messing-Referenzzylinder | 4 Stück | Ø7 mm laut Reference Board-Skizze; Mittelpunkte(±54,95;0) und(0;±44,9)mm. Endflächen auf Bezugsebene; Länge und Montage offen. Insgesamt 12Messingzylinder plus 4weiße Referenzen. |

## teilweise geklärt

| ID / Teil | Bedarf | Nächsterkonkreter Schritt |
| --- | --- | --- |
| CAD-023 BIGTREETECH SKR V1.3 Steuerplatine | 4 Stück | Original laut CAD, Firmware und Masterarbeit. Neu in DE/EU nicht gefunden (Recherche 17.10.2026). Kandidat SKR 1.4 Turbo (RBS13645) passt auf fast dieselben Löcher, braucht aber Marlin-Pinanpassung; nicht freigegeben. |
| CAD-058 ISO 8673 Mutter M8 | 53 Stück | Norm und Maße mit CAD abgeglichen; Artikel 24122 08 1. A4 statt A2; H 6,5 statt 6,8. Datenblatt nennt Linksgewinde, vermutlich Datenfehler: vor Bestellung klären. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026). ISO 8673 M8×1 passt zu den M8×1-Gewinden der induktiven Sensoren. Sensoren liefern meist 2 Muttern mit; dann nur Reserve kaufen. |
| CAD-085 Bewegliches USB-Mikroskop | 1 Stück | Plan 1 laut Hardware-Blog,4CAD. Weitere 3 optional. Originalmodell unbekannt; Kandidat muss 100 mm Arbeitsabstand/ca 30×40 mm Bildfeld und Linux-UVC erfüllen. |
| SYS-001 TMC2130 SPI Treibermodule | 16 Stück | 4 je SKR für X/X2/Y/Z. RBS13024: 4 Treiber mit Kühlkörpern und Kabel, SPI-Pins laut Fotos vorgelötet. Revision nicht angegeben; SPI-Modus laut Datenblatt per Lötbrücke CFG4/CFG5 prüfen. |
| SYS-002 Stationäre Übersichtskamera | 1 Stück | 1080p-Softwarekonfiguration; Optik, Blickfeld und Halterpassung offen. |
| SYS-007 Weißer 24-V-LED-Streifen | 2 m | 2 m vorläufig;5 m-Rolle. Weiß 4500K vorgeschlagen; Leistung, Flimmern und Lichtverteilung testen. |
| SYS-008 LED-Aluprofile, Diffusoren, Kappen, Halter | 2 m | 8 mm-Streifen aufnehmen, Wärmeabfuhr und Befestigung; genaue Aufteilung/Menge offen. Keine Doppelrechnung als Band. |
| SYS-009 LED-Anschluss an vorhan denen SKR-Ausgang | 1 Satz | Configuration_adv.h:4396 setzt PROBOTER_LIGHT_CONTROL_PIN auf HEATER_BED_PIN; M376 steuert Helligkeit. Kein separater USB-LED-Controller nötig. Stecker/Leitungen, Strom und Flimmern prüfen; keine zusätzliche MOSFET-Platine pauschal kaufen. |
| SYS-010 USB-Hub 7Port aktiv | 1 Stück | Steuergeräte am Hub; zwei separate Kamera-Hostports vorausgesetzt. Netzteil und Hubkabel enthalten. |
| SYS-011 USB-Kabel für 4 SKR | 4 Stück | Host USB-A auf Board USB-B bestätigen; Länge vorläufig 2 m je Board, Ports/Verlegung prüfen. |
| SYS-012 USB-Kabel für MUX/UART/Zielversorgung | 3 Stück | 3 Verbindungen aus Softwarekonfiguration, Geräteseite und enthaltene Kabel offen; nur nach Geräteauswahl kaufen. |
| SYS-013 Bewegliche Kameraleitung / USB-Verlängerung | 1 Stück | Schleppkettengeeignete Leitung/Länge/Stecker offen; Kamera-Beipack gegenrechnen. |
| SYS-014 Motorleitungen 4adrig | 32 m | Plan 16×2 m; Schleppkettenradius, Querschnitt/Strom, Aderfarben und reale Wege offen. |
| SYS-015 Motor-Gegenstecker und Crimpkontakte | 32 Satz | Plan 2 Enden je 16 Motoren. Board-/Motorhersteller-Raster und Kontaktzahl prüfen; beiliegende Kabel abziehen. |
| SYS-016 Sensorleitungen / Verlängerungen | 24 Stück | Für 24 induktive Sensoren; enthaltene Anschlussleitungen zuerst prüfen. Optische 1 m-Kabel sind bei O-009 enthalten. |
| SYS-017 Sensor-Gegenstecker und Kontakte | 28 Satz | 24 induktiv+4 optisch; bei steckerfertigem Beipack reduzieren. Keine generischen JST/Dupont ohne Rasterprüfung. |
| SYS-018 24-V-Verteilung, Sicherungen, Klemmen, Leitungen | 1 Satz | 4 Controller+Sensoren+LED; Last/Stromlaufplan, Aderquerschnitte und Sicherungswerte bestimmen. |
| SYS-020 Netzeinspeisung, Leitung, Sicherung und Zugentlastung | 1 Satz | 230 V-Anschluss an offenes Netzteil: Anschlussmodul, Netzleitung, Sicherungshalter und geschützter Kabelweg planen. |
| SYS-021 Schutzleiter, Ringkabelschuhe und Klemmenabdeckung | 1 Satz | Metallrahmen/Netzteil erden; Querschnitt, Anschlusspunkte und Prüfverfahren in Stromlaufplan dokumentieren. |
| SYS-022 Messkoax und instrumentenseitige Adapter | 4 Kanäle | Vorhan dene Messgeräte verwenden; BNC/SMA/MMCX und Impedanz gerätespezifisch. CAD-MM CX-Stecker 61/62 sind separat, hier nur Kabel und Instrumentadapter. |
| SYS-025 USB-UART-Adapter | 1 Stück | Software setzt Adapter voraus; Pegel, Isolation, Pinout und Zielversorgung prüfen; Laborausstattung ggf. gegenrechnen. |
| SYS-027 Energieketten-Endanschlüsse schmal | 16 Sätze | igus E2.100.10.34PZ, beidseitig schwenkbar mit Zugentlastung; Breite 17,4 = Anschlusskörper im CAD (Fusion-Messung). |
| SYS-028 Energieketten-Endanschlüsse breit | 8 Sätze | igus E2.100.20.34PZ; Breite 27,4 = Anschlusskörper im CAD (Fusion-Messung). |
| SYS-029 Profil-Nutensteine und Zusatzbefestigung | 1 Satz | Nut 6/Profilserie klären; 26Winkel plus Halter. CAD-Vierkantmuttern 29/30 und mitgelieferte Winkelsätze abziehen. |
| SYS-030 Scheiben, Sicherungselemente, Distanzteile | 1 Satz | Ergänzungsbedarf je Verschraubung/Idler; CAD-Normteile und Sensor-Beipack abziehen. Stückzahlen noch offen. |
| SYS-031 Lötzinn, Schrumpfschlauch, Binder, Labels, Kleber | 1 Satz | Verbrauchsmaterialbudget; vorhan dene Bestände später abziehen. Werkzeuge nicht enthalten. |
| SYS-032 Controller-Befestigung und Kühlung | 1 Satz | Abstandshalter, Isolierung, ggf.Lüfter; SKR/TMC-Beipack und thermische Auslegung prüfen. |
| SYS-038 Kalibrier-Kontaktleitungen und gemeinsame Messreferenz | 1 Satz | 4 SKR-Zentriereingänge P0_17 mit Pull-up/aktiv Low sowie Referenzkörper/Kontaktkreis verdrahten. Netzplan, Stecker, Länge und Bezugspotenzial mit Multiplexer klären; keine Verbindung ungeprüft festlegen. |
| SYS-045 Zylinderschraube DIN 912 M5×35 A2, Griff | 2 Stück | Länge aus 29 mm Griffbein plus Nutenstein; Artikel noch nicht verifiziert. |
| SYS-048 Flachkopfschraube M4×8 A2, Teleskopschienen | 12 Stück | ANNAHME (Luis 17.10.2026): je Schiene 3 Schrauben zum Rahmen und 3 zur Schublade; im CAD keine Befestigung. Kopfhöhe muss in den Auszug passen; Artikel noch nicht verifiziert. |

## Reihenfolge zum Schließen der Lücken

1. Originalschaltpläne/BOM/Gerber für Multiplexer, Prüfspitzen und Zielversorgung beschaffen oder Neu-Entwicklungfestlegen; daraus Sensorinterface, Gegensteckerund Kabel ableiten.
2. NEMA14-Alternativlagen prüfen; eine vierachsige Probe mechanisch/elektrisch verifizieren. SKR1.3-Verfügbarkeit bzw.Firmwaremigration entscheiden.
3. Original-CPC/HIWIN-Paarungen und Motorlieferbarkeit anbieten lassen; keine Mischungungeprüfter Nachbauten.
4. Mikroskop bei 100 mm Arbeitsabstand und statische Kamera unter Linux prüfen; Halter danach festlegen.
5. Fertigungszeichnungen mit Werkstoffen/Passungen erstellen; Kalibrierboardgeometrie aufeine Softwareversionfestlegen.
6. Kabelwege und Kettenbelegung messen, Stromlaufplan abschließen, Beipack-Normteile abgleichen und Warenkörbe finalisieren.

Anfragen wurdennicht versandt.
