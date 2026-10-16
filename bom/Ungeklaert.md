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
| SYS-035 Z-Antriebsriemenscheibe / integrierter Adapter | 4 Stück | 16Zähne laut Firmware,9 mm Z-Riemen. Prüfen, ob CAD-001/002 das Antriebsrad bereits integriert; gegebenenfalls kein separater Kauf. |

## Fertigung noch offen

| ID / Teil | Bedarf | Nächsterkonkreter Schritt |
| --- | --- | --- |
| CAD-001 TR10x 2 GT2 Riemen Adapter | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-002 TR10x 2 GT2 Riemen Adapter Abdeckung | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-003 Grundgestell: Rückseite Platte | 1 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-004 Grundgestell: Kabel Halter M3 flach | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-005 Grundgestell: Kabel Halter M4 | 1 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-006 Grundgestell: Kabel Halter M5 flach | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-007 Grundgestell: Abdeckung lang Seite | 2 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-008 Grundgestell: Abdeckung oben | 2 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-009 Grundgestell: Schlepp Energiekette Halter | 4 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-011 Grundgestell: Schublade lang Seite | 2 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-012 Grundgestell: Rahmen lang Seite | 3 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-013 Grundgestell: Rahmen kurz | 8 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-014 Grundgestell: Rahmen Seite | 2 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-015 Grundgestell: NEMA 14 auf 17 Adapter | 12 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-016 Grundgestell: Platte Adapter 1 | 2 Stück | 10 mm Plattenhülle. Material, Nullpunkte, Loch-/Gewindetabelle, Passungen, Ebenheit und Oberflächen festlegen; STEP allein reicht nicht zur Funktionsfreigabe. |
| CAD-017 Grundgestell: Platte Adapter 2 | 2 Stück | 10 mm Plattenhülle. Material, Nullpunkte, Loch-/Gewindetabelle, Passungen, Ebenheit und Oberflächen festlegen; STEP allein reicht nicht zur Funktionsfreigabe. |
| CAD-018 Grundgestell: Platte Adapter links | 2 Stück | 10 mm Plattenhülle. Material, Nullpunkte, Loch-/Gewindetabelle, Passungen, Ebenheit und Oberflächen festlegen; STEP allein reicht nicht zur Funktionsfreigabe. |
| CAD-019 Grundgestell: Platte Adapter rechts | 2 Stück | 10 mm Plattenhülle. Material, Nullpunkte, Loch-/Gewindetabelle, Passungen, Ebenheit und Oberflächen festlegen; STEP allein reicht nicht zur Funktionsfreigabe. |
| CAD-020 Grundgestell: vertikal | 4 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-021 Riemen Spanner GT2 Basis | 20 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-022 Riemen Spanner GT2 Flügel | 20 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-024 Kabel Abdeckung | 4 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-025 Kamera Halter | 1 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-026 Kamera Halter oben | 1 Stück | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen. |
| CAD-067 Platine Halter Gleiter | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-068 Platine Halter Führung Halter rund d 10 | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-069 Platine Halter Führung rund | 2 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-070 Platine Halter rechteckig Stange | 2 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-071 Platine Halter Stange kurz rund d 10 | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-072 Platine Halter Stange kurz rund d 10 gespiegelt | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-074 Stromversorgung Schalter Halter | 1 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-075 Prüfspitzen-PCB, unbestückt | 4 Stück | 4 Stück;26,67×10,96×1,6 mm Hülle. Schaltplan, Kupfer, Bohrungen, Gerber und Bestückungsdaten fehlen. Bestückung SYS-024 separat. |
| CAD-083 Signal-Multiplexer Halter | 1 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-088 X-Achse Riemen Halter | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-089 X-Achse Riemen Halter 1 | 12 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-090 X-Achse Schlepp Energiekette Adapter | 8 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-091 X-Achse Endschalter Halter Seite kurz | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-092 X-Achse Endschalter Halter oben lang | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-093 X-Achse Endschalter oben lang | 4 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-094 X-Achse Endschalter oben kurz | 4 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-096 X-Achse Motor Platte | 1 Stück | 5 mm geometrische Dicke; Kontur und Bohrungen aus CAD, Gewinde/Senkungen und Bezugs-/Lagetoleranzen fehlen. Entgraten vor Montage. |
| CAD-097 X-Achse Motor Platte 2 | 1 Stück | 5 mm geometrische Dicke; Kontur und Bohrungen aus CAD, Gewinde/Senkungen und Bezugs-/Lagetoleranzen fehlen. Entgraten vor Montage. |
| CAD-098 X-Achse rund Schiene | 8 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-099 X-Achse Seite Platte | 4 Stück | 5 mm geometrische Dicke; Kontur und Bohrungen aus CAD, Gewinde/Senkungen und Bezugs-/Lagetoleranzen fehlen. Entgraten vor Montage. |
| CAD-100 X-Achse Seite Platte beweglich | 4 Stück | 5 mm geometrische Dicke; Kontur und Bohrungen aus CAD, Gewinde/Senkungen und Bezugs-/Lagetoleranzen fehlen. Entgraten vor Montage. |
| CAD-101 X-Achse Schlitten induktiv Endschalter Adapter | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-102 X-Achse Schlitten induktiv Endschalter Adapter gespiegelt | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-103 X-Achse Schlitten Versteifung Träger | 4 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-105 Y-Achse Kamera Halter | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-106 Y-Achse Kamera Halter kompakt | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-107 Y-Achse Schlitten | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-108 Y-Achse Schlitten Abstand Stange | 8 Stück | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen. |
| CAD-109 Y-Achse Schlitten Abstand Rohr 2 mm | 4 Stück | Name nennt 2 mm, CAD zeigt 3 mm Dicke. Innendurchmesser, Material und benötigte Distanz vor Fertigung klären. |
| CAD-110 Y-Achse Schlitten gespiegelt | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-111 Y-Achse Schlitten gespiegelt oben | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-112 Y-Achse Schlitten oben | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-114 Z-Achse Antrieb Riemen Halter v 3 | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-116 Z-Achse Prüfspitze Platine Halter | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-117 Z-Achse Prüfspitze Platine Halter lang | 2 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-118 Z-Achse Schlitten Kabel Halter | 4 Stück | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf. |
| CAD-119 Z-Achse Schlitten Endschalter Auslöser | 2 Stück | CAD .psm und dünner Körper sprechen für Blech; Dicke, Biegung und Sensor-Triggerwirkung nachweisen. Hüllmaß ist keine Abwicklung. |
| CAD-120 Z-Achse Schlitten Endschalter Auslöser gespiegelt | 2 Stück | CAD .psm und dünner Körper sprechen für Blech; Dicke, Biegung und Sensor-Triggerwirkung nachweisen. Hüllmaß ist keine Abwicklung. |
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
| CAD-023 BIGTREETECH SKR V1.3 Steuerplatine | 4 Stück | Originalmodell laut CAD/Firmware; kein belastbarer neuer EU-Lagerbestand gefunden. Ersatzboard benötigt Firmware-/Pin- und Halteranpassung. |
| CAD-027 CPC MR12ML Führungswagen | 8 Stück | 8 Wagen für 2×600-mm-Schienen. Aktueller Katalog 47,8 mm Länge, CAD47,6 mm; Vorspannung, Genauigkeit und Paarung klären. |
| CAD-028 DIN 466 Rändelmutter hoch M4 | 8 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-029 DIN 562 M3 Vierkantmutter | 8 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-030 DIN 562 M4 Vierkantmutter | 12 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-031 DIN 7991 M3×8 | 32 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-032 DIN 7991 M6×12 | 16 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-033 DIN 7991 M6×14 | 6 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-034 DIN 7991 M6×20 | 22 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-035 DIN 912 M3×10 | 76 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-036 DIN 912 M3×12 | 8 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-037 DIN 912 M3×14 | 4 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-038 DIN 912 M3×16 | 28 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-039 DIN 912 M3×18 | 32 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-040 DIN 912 M3×20 | 4 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-041 DIN 912 M3×30 | 8 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-042 DIN 912 M3×8 | 52 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-043 DIN 912 M4×10 | 1 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-044 DIN 912 M4×20 | 20 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-045 DIN 912 M4×30 | 36 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-046 DIN 912 M5×10 | 32 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-047 DIN 912 M5×14 | 4 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-048 DIN 933 M4×20 | 8 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. |
| CAD-049 igus E2i.10.10.028.0, 16 kurze Abschnitte | 16 Stück | Nominell 16×0,24 m=3,84 m. Gliederraster, Verfahrweg und Endstücke prüfen;1 m-Einkaufseinheiten sind keine 16 ganzen Ketten. |
| CAD-050 igus E2i.10.20.028.0, 8 lange Abschnitte | 8 Stück | Nominell 8×0,28 m=2,24 m. Drei 1 m-Einheiten ergeben rechnerisch 9 Abschnitte; Teilung und Endstücke bestätigen. |
| CAD-051 Schubladengriff, Lochabstand vermutlich 100 mm | 1 Stück | CAD113×20×49 mm; Lochabstand, Gewinde und genaue DOLD-Artikelnummer bestimmen. |
| CAD-052 Gelenkfuß M6 / TellerØ40 mm | 4 Stück | CAD40×40×30,4 mm; Gewindelänge, Schwenkbereich und Traglast festlegen. |
| CAD-053 HIWIN MGNR12R150HM, Z-Schiene 150 mm | 4 Stück | Originalname; aktuelle Suffixe, Endlochabstände und Paarung mit CAD-054 bestätigen. |
| CAD-054 HIWIN MGN12CZ0H Z-Führungswagen | 4 Stück | Originalname; vier passende Wagen zu CAD-053, keine ungeprüfte Mischung mit Nachbauten. |
| CAD-056 ISO 8673 Mutter M3 | 44 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. ISO8673 bezeichnet Feingewinde ab M8 (ISO8673:2012/2023). Namen M3/M4 widersprechen dem Normumfang. Tatsächliche Steigung gegen Schrauben/Sensor prüfen; nicht ungeprüft Regelgewinde bestellen. |
| CAD-057 ISO 8673 Mutter M4 | 64 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. ISO8673 bezeichnet Feingewinde ab M8 (ISO8673:2012/2023). Namen M3/M4 widersprechen dem Normumfang. Tatsächliche Steigung gegen Schrauben/Sensor prüfen; nicht ungeprüft Regelgewinde bestellen. |
| CAD-058 ISO 8673 Mutter M8 | 48 Stück | Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen. ISO8673 bezeichnet Feingewinde ab M8 (ISO8673:2012/2023). Namen M3/M4 widersprechen dem Normumfang. Tatsächliche Steigung gegen Schrauben/Sensor prüfen; nicht ungeprüft Regelgewinde bestellen. 48M8-Muttern könnten als 2je Sensor bereits enthalten sein; Kosten nicht doppelt ansetzen. |
| CAD-059 Mean Well MHS012 Montagewinkel | 4 Stück | 4 Winkel,19×16×15 mm. TME identifiziert;0,09 EUR aus italienischer Indexseite nicht als bestätigter DE-Preis übernommen. |
| CAD-063 Nanotec ST3518M1004-A NEMA14 Z-Motor | 4 Stück | Plan 4 statt 8 CAD: paarweise überlagerte Einbaulagen, je Probe ein Z-Antrieb. Hypothese vor Bau prüfen. Archivmodell, Ersatzpassung offen. |
| CAD-064 Nanotec ST4118M1804-A NEMA17 X/Y-Motor | 12 Stück | 12 laut STEP:8 X +4 Y. Alle 12 im Fusion-Import fehlend. Hersteller nennt Modell; Anschluss und aktuelle Verfügbarkeit bestätigen. |
| CAD-065 Optischer Endschalter 11×35 mm | 4 Stück | 4 Stück, Kandidat mit 1 m-Kabel. Lochabstand 28 mm, Schlitzlage, Pinout, Versorgung und Schaltpegel abgleichen. |
| CAD-076 Umlenkrolle 9 mm / außenØ18 / BohrungØ5 | 8 Stück | CAD-Zylinder belegenØ5 undØ18, Breite 11 mm. DOLD64396 Kandidat; Lager, Lauffläche und axiale Passung prüfen. |
| CAD-077 GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | 12 Stück | 12 X/Y-Antriebe. Bore 5 durch CAD-Zylinder bestätigt; Bundlänge 14,1 mm und Madenschrauben prüfen. |
| CAD-078 GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | 20 Stück | 20 Stück, CADØ13×8,5 mm mitØ3-Bohrung. Lager-/Distanzscheiben und Artikel 46132 axial abgleichen. |
| CAD-080 GleitbuchseØ10 innen / Ø19 außen / Länge 29 mm | 16 Stück | CAD-Name l 19 irreführend:19 ist Außendurchmesser, Länge 29 mm. igus RJ4JP-01-10 Kandidat; Werkstoff, Spiel und zulässige Welle prüfen. |
| CAD-081 Anschraubwinkel 30 / Nut 6 | 26 Stück | 26 Stück; CAD28×28×28 mm. Profilserie I/B, Schraubenset und Lochbild offen. |
| CAD-084 Teleskopschiene TSAA514613-350 | 2 Stück | 2 Einzelschienen im CAD, nicht 2 Paare.350×45,5×12,7 mm; Hersteller, Auszug, Rastung und Last klären. |
| CAD-085 Bewegliches USB-Mikroskop | 1 Stück | Plan 1 laut Hardware-Blog,4CAD. Weitere 3 optional. Originalmodell unbekannt; Kandidat muss 100 mm Arbeitsabstand/ca 30×40 mm Bildfeld und Linux-UVC erfüllen. |
| CAD-087 GT2-Riemen X,6 mm breit | 8 Stück | 8 Verläufe.710,3 mm Hülllänge ist NICHT Riemenlänge. Vorläufig gemeinsamer 20 m-Ansatz für X/Y; offene/geschlossene Bauform klären. |
| CAD-095 CPC MR12M Führungsschiene 600 mm | 2 Stück | 2 Stück 600×12×7,5 mm. Endlochabstand, Genauigkeit, Material und passende 8 Wagen bestimmen. |
| CAD-104 GT2-Riemen Y,6 mm breit | 4 Stück | 4 Verläufe.503,3 mm Hülllänge ist NICHT Riemenlänge; Einkauf gemeinsam mit CAD-087, nicht doppelt rechnen. |
| CAD-113 GT2-Riemen Z,9 mm breit | 4 Stück | 4 Verläufe;119,3 mm Hülllänge ist NICHT Riemenlänge.2 m Budgetvorschlag; Gates LL2GT RF9 mm Bezugsfamilie, Ausführung prüfen. |
| SYS-001 TMC2130 SPI Treibermodule | 16 Stück | 4 je SKR für X/X2/Y/Z; Kühlkörper/Jumper im Lieferumfang prüfen. |
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
| SYS-027 Energieketten-Endanschlüsse schmal | 16 Paare | Je kurzer Kette 1 bewegliches+1 festes Ende. E2i.10.10 passende MPN ermitteln; Lieferumfang und CAD-Dreikörpermodell prüfen. |
| SYS-028 Energieketten-Endanschlüsse breit | 8 Paare | Je langer Kette 1 Paar passend E2i.10.20; keine Endstücke doppelt kaufen, falls enthalten. |
| SYS-029 Profil-Nutensteine und Zusatzbefestigung | 1 Satz | Nut 6/Profilserie klären; 26Winkel plus Halter. CAD-Vierkantmuttern 29/30 und mitgelieferte Winkelsätze abziehen. |
| SYS-030 Scheiben, Sicherungselemente, Distanzteile | 1 Satz | Ergänzungsbedarf je Verschraubung/Idler; CAD-Normteile und Sensor-Beipack abziehen. Stückzahlen noch offen. |
| SYS-031 Lötzinn, Schrumpfschlauch, Binder, Labels, Kleber | 1 Satz | Verbrauchsmaterialbudget; vorhan dene Bestände später abziehen. Werkzeuge nicht enthalten. |
| SYS-032 Controller-Befestigung und Kühlung | 1 Satz | Abstandshalter, Isolierung, ggf.Lüfter; SKR/TMC-Beipack und thermische Auslegung prüfen. |
| SYS-038 Kalibrier-Kontaktleitungen und gemeinsame Messreferenz | 1 Satz | 4 SKR-Zentriereingänge P0_17 mit Pull-up/aktiv Low sowie Referenzkörper/Kontaktkreis verdrahten. Netzplan, Stecker, Länge und Bezugspotenzial mit Multiplexer klären; keine Verbindung ungeprüft festlegen. |

## Reihenfolge zum Schließen der Lücken

1. Originalschaltpläne/BOM/Gerber für Multiplexer, Prüfspitzen und Zielversorgung beschaffen oder Neu-Entwicklungfestlegen; daraus Sensorinterface, Gegensteckerund Kabel ableiten.
2. NEMA14-Alternativlagen prüfen; eine vierachsige Probe mechanisch/elektrisch verifizieren. SKR1.3-Verfügbarkeit bzw.Firmwaremigration entscheiden.
3. Original-CPC/HIWIN-Paarungen und Motorlieferbarkeit anbieten lassen; keine Mischungungeprüfter Nachbauten.
4. Mikroskop bei 100 mm Arbeitsabstand und statische Kamera unter Linux prüfen; Halter danach festlegen.
5. Fertigungszeichnungen mit Werkstoffen/Passungen erstellen; Kalibrierboardgeometrie aufeine Softwareversionfestlegen.
6. Kabelwege und Kettenbelegung messen, Stromlaufplan abschließen, Beipack-Normteile abgleichen und Warenkörbe finalisieren.

Anfragen wurdennicht versandt.
