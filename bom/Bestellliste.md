# Bestellliste für den PROBoter-Nachbau

**Arbeitsstand, keine Bestellfreigabe · 16.10.2026.** Zielbild ist der im
[Hardware-Blog](https://www.schutzwerk.com/en/blog/proboter-02/)
beschriebene Aufbau mit vier Prüfeinheiten. Die **Mengen in der vollständigen
[CAD-Teileliste](CAD-Teileliste.md) sind ausschließlich STEP-Modellzählungen**
und werden erst nach Klärung der [offenen Punkte](../docs/Offene-Punkte.md)
zu Bestellmengen. Preise, Lagerbestand, Versand und Bezugsquellen wurden
noch nicht tagesaktuell geprüft.

## Was derzeit eindeutig benannt ist

| Bauteil | CAD-Menge | Herkunft | Vor Bestellung |
|---|---:|---|---|
| [BIGTREETECH SKR V1.3](https://github.com/bigtreetech/BIGTREETECH-SKR-V1.3) Steuerplatine | 4 | STEP und [Firmware-README](../firmware/README.md) | Passende TMC2130-Steckmodule, Firmware und Beschaffbarkeit prüfen |
| [Mean Well RSP-200-24](https://www.meanwell.com/Upload/PDF/RSP-200/RSP-200-SPEC.PDF), 24-V-Netzteil | 1 | STEP | Gesamtleistung, Netzanschluss und Montage prüfen |
| [Nanotec ST4118M1804-A](https://www.nanotec.com/eu/de/produkte/363-st4118m1804-a), NEMA-17-Motor | 12 | STEP und Hersteller | Einbausituation und tatsächliche Motorbelegung prüfen |

**Diese drei Modelle sind identifiziert, ihre CAD-Mengen sind noch nicht als
vollständige Systemmengen bestätigt.** Für Nanotec ST3518M1004-A stehen
acht CAD-Vorkommen; das Modell liegt im
[Nanotec-Archiv](https://www.nanotec.com/eu/de/downloads/archiv) und ist
deshalb als **KLÄREN** markiert.

## Alle im CAD benannten Teile

Die [CAD-Teileliste](CAD-Teileliste.md) führt **jede der 120
Blattteil-Positionen einzeln** mit Menge, verständlicher Beschreibung und
Status auf. Die [CSV-Rohinventur](cad-inventory.csv) zeigt zusätzlich die
53 Unterbaugruppen-Vorkommen, die **nicht noch einmal** zu bestellen sind.

| Gruppe | Positionen | Wichtigste Aufgabe |
|---|---:|---|
| Elektronik, Kameras und Prüfkontakte | 11 | Sensor- und Kameraausführungen, Prüfspitzen-PCB und Steckverbinder spezifizieren |
| Antriebe und Linearführungen | 7 | Motorzahl, Führungsvarianten und Schienenlängen prüfen |
| Energieketten, Riemen und Kaufmechanik | 14 | Riemen- und Kettenlängen, Umlenkrollen und Halter spezifizieren |
| Normteile und Befestigung | 24 | Werkstoffe/Festigkeitsklassen und Liefermengen festlegen |
| CAD-Fertigungsteile | 61 | Einzelteile aus der STEP-Baugruppe ableiten; Material, Toleranz, Fertigungsverfahren und Zuschnitt festlegen |
| Platzhalter / Dummys | 3 | Durch echte Teile ersetzen oder aus der Beschaffung streichen |

Die rekursive Auswertung zählt **4 SKR-Boards, 8 NEMA-14-Motorvorkommen,
12 NEMA-17-Motorvorkommen, 4 Prüfspitzen-PCBs, 4 Z-Riemen und 4 USB-Mikroskope**.
Die erste Inventur hatte wiederverwendete Baugruppen nicht mehrfach aufgelöst
und dadurch Mengen unterschätzt. Die korrigierten Modellmengen müssen noch
gegen Einbausituation, mögliche Alternativteile und elektrische Belegung
geprüft werden. Sie sind keine freigegebenen Einkaufsstückzahlen.

### Bekannte Kaufteil-Familien mit Klärbedarf

| CAD-Positionen | CAD-Menge | Was noch fehlt |
|---|---:|---|
| `nanotec_nema_14_ST3518M1004-A` | 8 | Aktuelle Verfügbarkeit oder mechanisch/elektrisch passender Ersatz |
| `hiwin_rail_MGNR12R150HM`, `hiwin_slide_MGN12CZ0H` | je 4 | Exakte Ausführung und Paarung; Schienen je Probe prüfen |
| `cpc_MR12ML`, `x_guiding_cpc_MR12M` | 8 / 2 | Schienenlänge, Vorspannung und Genauigkeitsklasse |
| `drag_chain_0_24m_E2i_10_10_028_0_4` | 16 × 0,24 m | Gliederzahl und Endanschlüsse; rechnerisch 3,84 m ohne Verschnitt |
| `drag_chain_0_28m_E2i_10_20_028_0_igus` | 8 × 0,28 m | Gliederzahl und Endanschlüsse; rechnerisch 2,24 m ohne Verschnitt |
| `x_belt`, `y_belt`, `z_drive_belt` | 8 / 4 / 4 | GT2-Breite und konkrete Längen |
| `inductive_proximity_sensor_m8`, `optical_endstop` | 24 / 4 | Schaltart, Versorgung, Stecker und Kabellänge |
| `usb_microscope` | 4 | Tatsächliche Kameraart und Anzahl gegen Blogstand prüfen |
| `probe_tip_pcb`, `plug_sleeve_P75-2_W`, `z_pogo_pin` | 4 / 8 / 8 | Leiterplattenfertigung, passender Prüfkontakt und Stückzahl je Prüfeinheit |
| DIN-/ISO-Schrauben und Muttern | 24 Positionen | Normgröße steht in [CAD-Teileliste](CAD-Teileliste.md); Werkstoff und Festigkeitsklasse offen |

## Zusätzlich einzuplanen, aber nicht bestellfertig im CAD

| Bedarf | Vorläufige Menge | Status / Begründung |
|---|---:|---|
| TMC2130-Steckmodule für die SKR-Boards | **16 Kanäle laut Firmware** | **KLÄREN** · [Firmware](../firmware/Marlin/Configuration.h) konfiguriert X, X2, Y, Z je Board; Zuordnung zu den 20 CAD-Motorvorkommen und tatsächliche Verdrahtung sind ungeklärt |
| Reale Signal-Multiplexer-Platine einschließlich Bauteilen | 1 System | **BLOCKIERT** · Im STEP nur `signal_multiplexer_dummy`, keine Schaltung, Gerber oder Elektronik-BOM veröffentlicht |
| Prüfspitzenplatinen samt Bestückung | 4 im CAD | **BLOCKIERT** · `probe_tip_pcb` ist ein CAD-Körper ohne Fertigungsdaten |
| Statische Übersichtskamera mit Optik und Halter | 1 | **KLÄREN** · [Blog](https://www.schutzwerk.com/en/blog/proboter-02/) nennt diese Kamera, aber kein Modell |
| Weißer LED-Streifen mit Versorgung/Befestigung | Länge offen | **KLÄREN** · Im Blog beschrieben, keine bestellfähige CAD-Position |
| Kalibrier-Referenzplatte mit Messingzylindern | 1 Platte, 8 oder 12 Referenzpunkte | **KLÄREN** · Konstruktion und Befestigung aus Blog/Thesis ableiten |
| Kabelbaum, Motor-/Endschalter-/Kamera-/USB-Leitungen und Steckverbinder | offen | **KLÄREN** · Längen, Querschnitte, Stecker und Schleppkettenbelegung fehlen |
| Netzanschluss, Absicherung, Schutzleiterführung und 24-V-Verteilung | 1 System | **KLÄREN** · Stromlauf- und Verdrahtungsplan fehlen |
| Host-Rechner für Docker-Compose-Dienste | 1, sofern nicht vorhanden | **KLÄREN** · Systemanforderungen und GPU-Bedarf anhand der Software festlegen |
| Digitales Oszilloskop für automatische Signalanalyse | 1, falls diese Funktion gebaut wird | **OPTIONAL/KLÄREN** · [Blog Teil IV](https://www.schutzwerk.com/en/blog/proboter-04/) nennt es, aber kein verbindliches Modell |
| Druckmaterial, Profilzuschnitt und Bearbeitung der CAD-Sonderteile | nach Zeichnung | **KLÄREN** · 61 CAD-Positionen benötigen Fertigungsentscheidung |

## Bestellung erst nach Freigabe

1. Die Einbausituation für vier Prüfeinheiten geometrisch prüfen und den
   Antriebs-/Treiberplan festlegen.
2. Fehlende PCB- und Verdrahtungsdaten sowie die Einzelteilzeichnungen
   erstellen oder vom Originalprojekt erhalten.
3. Für jede `KLÄREN`- oder `FERTIGEN`-Zeile eine konkrete Bestellnummer bzw.
   freigegebene Fertigungszeichnung ergänzen und die CAD-Mengen aktualisieren.
4. Erst dann aktuelle Preise, Lagerbestände und Bestellmengen mit Reserve
   ermitteln. Historische Quellen nennen ca. 2.300 € für den Zwei-Proben-Stand
   von 2019 und ca. 5.000 € Rohmaterial für den späteren Prototyp; beides ist
   **kein** heutiger Angebotspreis.
