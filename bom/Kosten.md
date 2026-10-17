# Kosten und Kalkulationsgrenzen

**Preisstand 16.10.2026; EUR. Ein PROBoter mit vier Prüfeinheiten.**
Öffentliche Seiten bzw. Suchindexanzeigen sind Preisbeobachtungen, keine bindenden
Angebote. Bestand und Preis können gegenüber dem Index geändert sein. Vor einer
Bestellung den Artikel, die Mengenstaffel, die Rechnungsfreigabe und das Lieferdatum
im Shop bestätigen. Kein Warenkorb wurde bestellt.

## Drei getrennte Ergebnisse

| Umfang | netto | brutto |
| --- | --- | --- |
| 1. Beobachtete Webpreise × geplante Bestellpackungen | 3.626,97 € | 4.316,18 € |
| Davon Positionen mit Status bestellfähig | 2.928,73 € | 3.485,28 € |
| Davon übrige Material-/Kandidatenpreise mit offenen Prüfungen | 698,24 € | 830,90 € |
| Eigene Budgetschätzungen zusätzlich | 825,25 € | 982,03 € |
| 2. Vorläufiger Gesamtbedarf des bezifferten Umfangs | 4.452,22 € | 5.298,21 € |
| 3. Noch unbezifferte Positionen: 19 | nicht berechenbar | nicht berechenbar |

**Der Gesamtpreis eines funktionierenden Nachbaus bleibt offen.** Die Summe unter 2
deckt nur bezifferte Positionen ab. Entwicklung von Elektronik/Firmware, interne
Arbeitszeit, Maschinenkosten, Host-PC, Messgeräte und Werkzeuge sind ausgeschlossen.
Einzelne Budgetansätze können nach Konstruktion stark abweichen; sie sind weder
Preisobergrenzen noch Angebote. Es wurde kein pauschaler Gewinn-/Risikozuschlag aufgeschlagen.

## Rechenregeln

- Steuerbasis:19% deutsche Umsatzsteuer als Planannahme für die Lieferung nach DE.
  Keine Vorsteuerabzugsberechtigung oder innergemeinschaftliche Steuerbefreiung unterstellt.
  Bei einem EU-Lieferanten die tatsächliche Rechnungsbehandlung prüfen.
- Bruttopreise: Zeilenbrutto = Packungen × Packungspreis; netto = brutto/1,19.
  Nettopreise: Zeilennetto = Packungen × Packungspreis; brutto = netto×1,19.
  Auf Zeilenebene kaufmännisch auf Cent gerundet; Summen addieren diese Zeilen.
  Daher kann die Umrechnung der Gesamtsumme um wenige Cent abweichen.
- Packungen = aufgerundeter Bedarf/Packungsinhalt. Vier Treiber je Packung,
 10 m bei GT2-6 mm,5 m bei LED und 1 kg bei Filament sind dokumentiert.
  Normteil-Zehnerpackungen und Profil-Recheneinheiten sind **Planannahmen**,
  keine behaupteten Händler-Mindestmengen. Stückbedarf bleibt in Teileliste sichtbar.
- Internes Druckmaterial nach Vollvolumen und Zuschlag; Blech als eigener
  Budgettopf. CNC-Budget enthält Material bereits. Keine erneute Berechnung
  der einzelnen Druck-/Blechteile oder des CNC-Rohmaterials.
- Baugruppen nicht zusätzlich zu ihren Blattteilen kalkuliert.
  X/Y-Riemen teilen einen Kostenposten. Führungswagen und Schienen im Budget
  als abgestimmte Sätze. Multiplexer-Dummy ausgeschlossen; echte Platine und
  Bestückung getrennt und unbeziffert.
- Enthaltene optische Endstop-Kabel sowie Hub-Netzteil/-Kabel nicht doppelt
  kalkuliert.48M8-Sensormuttern zunächst offen, da möglicherweise Beipack.
  Kettenendstücke sind nur ein Budget, bis der Lieferumfang geklärt ist.
- Optionen/Vergleiche `ALT-*` und `OPT-*` sind aus Grundsummen ausgeschlossen.
  Ein Nachbauwagen ist keine bestätigte Alternative für eine Originalschiene.
- Fehlende Preise sind in CSV leere Zellen und in JSON/Code null/None, niemals 0.
  Nur RBS-Versand ist ausdrücklich 0, weil der geplante Sammelwarenkorb 99 EUR
  übersteigt. Die 150 EUR für sonstige Fracht sind eine eigene Budgetreserve.
  Rechnungsgebühr Schrauben.Expert zusätzlich 5 EUR brutto angenommen, Steuerbasis offen.

## Budget nach Lieferant

Nur die numerisch bezifferten Grundpositionen; darunter befinden sich Schätzungen.
Die bevorzugten Ansprechpartner für unbezifferte Zeilen stehen in der Bestellliste.

| Lieferant | Webpreise brutto | Schätzungen brutto | Summe beziffert brutto |
| --- | --- | --- | --- |
| AUTOMATION24 | 396,98 € | 0,00 € | 396,98 € |
| BEFFUCHS | 9,41 € | 5,95 € | 15,36 € |
| DAMEN | 370,09 € | 0,00 € | 370,09 € |
| DIGIKEY | 175,55 € | 0,00 € | 175,55 € |
| DOLD | 636,43 € | 365,00 € | 1.001,43 € |
| EISEN2000 | 113,65 € | 0,00 € | 113,65 € |
| IGUS | 172,70 € | 0,00 € | 172,70 € |
| MOTEDIS | 314,66 € | 0,00 € | 314,66 € |
| NANOTEC | 445,54 € | 0,00 € | 445,54 € |
| OFFEN | 0,00 € | 150,00 € | 150,00 € |
| RBS | 457,90 € | 30,00 € | 487,90 € |
| REICHELT | 219,38 € | 195,00 € | 414,38 € |
| RS | 876,79 € | 0,00 € | 876,79 € |
| SCHRAUBEN | 97,10 € | 29,00 € | 126,10 € |
| STEPPERONLINE | 0,00 € | 38,08 € | 38,08 € |
| TINYTRONICS | 30,00 € | 0,00 € | 30,00 € |
| TME | 0,00 € | 169,00 € | 169,00 € |

## Noch unbeziffert – Auswirkung auf die Vollständigkeit

| Bestellzeile | Benötigter Umfang | Warum Preis fehlt |
| --- | --- | --- |
| OPEN-CAD-010 | Schubladen-Dummyplatte | Schubladen-Dummy 564×410×12 mm: unklar, ob reale Platte benötigt und welches Material. Nicht stillschweigend ausschließen oder aus Stahl fertigen. |
| OPEN-CAD-061 | MMCX-Stecker gerade / Messleitung | 4 CAD-Modelle enthalten Kabelansätze. Impedanz, Kabeltyp, Crimp/Lötanschluss, Gegenstecker und Länge unbekannt. |
| OPEN-CAD-062 | MMCX-Stecker gewinkelt / Messleitung | 4 CAD-Modelle; Kabel-/Buchsenpaarung mit CAD-061/075 und Multiplexer offen. |
| OPEN-CAD-073 | Prüfkontakt-Hülse P75-2 W | 8 Stück, CADØ1,2×25,4 mm. Hersteller und passender Federkontakt CAD-115 unklar; Kontaktpaar vollständig spezifizieren. |
| OPEN-CAD-075 | Prüfspitzen-PCB, unbestückt | 4 Stück;26,67×10,96×1,6 mm Hülle. Schaltplan, Kupfer, Bohrungen, Gerber und Bestückungsdaten fehlen. Bestückung SYS-024 separat. |
| OPEN-CAD-115 | Federkontakt der Prüfspitze | 8 Stück, CADØ1×16,6 mm. Spitzenform, Hub, Federkraft, Kontaktmaterial und Paarung mit P75-2-W unklar. |
| OPEN-SYS-003 | Signal-Multiplexer, unbestückte Leiterplatte | CAD-082 ist nur Platzhalter. Schaltplan/Gerber/Board-BOM fehlen; USB/9600Baud-Protokoll ist keine Schaltung. |
| OPEN-SYS-005 | Innere Messing-Referenzzylinder | Je 1×Ø7/8/9/10 mm nach Reference Board.inner_brass_pin_position_map; Raster 11,95×19,95 mm. Endfläche auf Bezugsebene; Gesamtlänge, Einbau, Toleranzen und Messprotokoll fehlen. |
| OPEN-SYS-006 | Kalibriermarker / matte Druckvorlage | 4 Hamming-Marker mit IDs 1/3/6/12 laut Reference Board, je 18,2×18,2 mm, Raster 60×80 mm. Mtracker-Format verwenden, keine beliebigen Ar Uco-Marker. Maßstab 1:1 und reale Abstände vermessen. |
| OPEN-SYS-009 | LED-Anschluss an vorhan denen SKR-Ausgang | Configuration_adv.h:4396 setzt PROBOTER_LIGHT_CONTROL_PIN auf HEATER_BED_PIN; M376 steuert Helligkeit. Kein separater USB-LED-Controller nötig. Stecker/Leitungen, Strom und Flimmern prüfen; keine zusätzliche MOSFET-Platine pauschal kaufen. |
| OPEN-SYS-017 | Sensor-Gegenstecker und Kontakte | 24 induktiv+4 optisch; bei steckerfertigem Beipack reduzieren. Keine generischen JST/Dupont ohne Rasterprüfung. |
| OPEN-SYS-019 | Sensor-Pegelanpassung / Eingangsschutz | Bedarf abhängig von M8-Ausgang; 24 V/3,3 V-Interface. Keine Schaltung/BOM vorhan den; nicht blind 24Module bestellen. |
| OPEN-SYS-023 | Signal-Multiplexer Bestückung | MCU, USB/Versorgung, Schalter/Relais, Schutz, Stecker, Passives und Montage nach noch fehlendem Schaltplan. Keine Stückzahlen erfinden. |
| OPEN-SYS-024 | Prüfspitzen-PCB Bestückung | CAD-MM CX/Federkontakte separat; zusätzliche Buchsen und Bauteile erst aus Schaltplan. Unbestückte Platine CAD-075 nicht erneut zählen. |
| OPEN-SYS-026 | Zielplatinen-Versorgungscontroller | Softwareziel /dev/proboter_target-power-controller; Schaltung, Firmware/Hardware und Kabel fehlen. Separat vom RSP-Netzteil. |
| OPEN-SYS-037 | Weiße äußere Kalibrierreferenzen | Reference Board Config beschreibt vier äußere weiße Referenzpins. Raster 109,9×89,8 mm; Durchmesser, Höhe, Material und Umsetzung am gewählten Board fehlen. Nicht mit 12Messingpins gleichsetzen. |
| OPEN-SYS-038 | Kalibrier-Kontaktleitungen und gemeinsame Messreferenz | 4 SKR-Zentriereingänge P0_17 mit Pull-up/aktiv Low sowie Referenzkörper/Kontaktkreis verdrahten. Netzplan, Stecker, Länge und Bezugspotenzial mit Multiplexer klären; keine Verbindung ungeprüft festlegen. |
| OPEN-SYS-039 | Erhöhte Messing-Referenzzylinder | Ø7 mm laut Reference Board-Skizze; Code setzt vier Endflächen 6/8/10/12 mm über Bezugsebene auf Raster 59,6×39,9 mm. Gesamtlängen und Einstecktiefe sind nicht diese Höhen; Zeichnung und Toleranzen fehlen. |
| OPEN-SYS-040 | Äußere flache Messing-Referenzzylinder | Ø7 mm laut Reference Board-Skizze; Mittelpunkte(±54,95;0) und(0;±44,9)mm. Endflächen auf Bezugsebene; Länge und Montage offen. Insgesamt 12Messingzylinder plus 4weiße Referenzen. |

## Größte Kostenrisiken

Die fehlenden PCB-Entwürfe bestimmen Bestückung, Sensorinterface und Anschlussplan.
Ein Einkauf einzelner Platinenrohlinge löst diesen Entwicklungsbedarf nicht.
Originalmotoren und SKR1.3 können Beschaffungs- oder Umkonstruktionskosten verursachen.
Vier zusätzliche NEMA14 statt der Planmenge 4 würden imreinen Motorbudget weitere
238 EUR brutto erfordern; daraus folgt nochkein funktionierender Antriebsplan.
Kamerakandidaten können nach dem Optiktest entfallen oder einenanderen Halter benötigen.
Die historischen Projektkosten im Blog sind keine Preisgrundlage dieser Kalkulation.

Maschinenlesbar: [Bestell-CSV](bestellliste.csv), [Summen-JSON](kosten.json).
Rechenweg und Prüfung: [Reproduktion](Reproduktion.md).
