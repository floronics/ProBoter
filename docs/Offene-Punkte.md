# Offene Punkte vor dem Nachbau

**Stand: 16.10.2026.** `P0` blockiert eine verlässliche Komplettbestellung;
`P1` wird für Fertigung oder Inbetriebnahme benötigt. Die Mengen der
[CAD-Teileliste](../bom/CAD-Teileliste.md) bleiben bis zur Klärung
als Modellzählung gekennzeichnet. Die aktuelle vollständige Positionsliste mit
Klärbedarf steht unter [bom/Ungeklaert.md](../bom/Ungeklaert.md).
Der [Kostenbericht](../bom/Kosten.md) nennt 24 unbezifferte Bestellpositionen;
alle weiteren Schätzungen sind ebenfalls als vorläufig gekennzeichnet.

| Prio | Frage / belegte Lücke | Nächste Prüfung |
|---|---|---|
| P0 | Fusion-Abgleich abgeschlossen: 12 NEMA17 fehlen im Import, 8 NEMA14 liegen paarweise nahezu am selben Ort. Planung: 12+4 Motoren. | Vier alternative Z-Motor-Einbaulagen und 16 Treiberkanäle am Aufbau bestätigen; rohe CAD-Zählungen erhalten. |
| P0 | `signal_multiplexer_dummy` statt realer Multiplexer-Platine. | Schaltplan, PCB-Layout, Fertigungsdaten, Bestückung und elektrisches Interface beim Originalprojekt ermitteln oder neu konstruieren. |
| P0 | `probe_tip_pcb` ist nur ein CAD-Körper; keine Schaltpläne/Gerber für die Prüfspitzenplatinen. | Pinbelegung, Kontaktgeometrie, Fertigungsdaten und reale Stückzahl klären. |
| P0 | Fertigungsgruppen und Hüllmaße sind erfasst; verbindliche Einzelteilzeichnungen, Werkstoffe und Passungen fehlen. | Vorschläge in [Fertigung](../bom/Fertigung.md) freigeben, Einzelteile exportieren und tolerierte Zeichnungen erstellen. |
| P0 | Riemenbreiten 6/9mm und Rollenbohrungen 5/3/5mm sind geometrisch erfasst; wirksame Riemenlängen und Endlos-/Meterware offen. | Umlenkwege und Einspannung prüfen; 20m/2m bleiben Mengenreserven, keine Zuschnittfreigabe. |
| P0 | Original-SKR1.3 und NEMA14 sind nicht mit gesichertem neuen EU-Lagerbestand belegt. | Originalbeschaffung oder Board-/Motorersatz samt Firmware-/Halteranpassung entscheiden. Vier SPI-Treiber je Board; keine Motorparallelisierung unterstellen. |
| P0 | Multiplexer-Dummy ersetzt durch reale offene PCB-Positionen; PCB-Dummy als Prüfobjekt ausgeschlossen. Schubladen-Dummyplatte offen. | Reale Schubladenplatte, Material und Befestigung festlegen. |
| P1 | Blog nennt eine bewegliche und eine statische Kamera; die rekursive STEP-Zählung ergibt vier USB-Mikroskope. | Kameramodelle, Optik, Halterung, Arbeitsabstand und tatsächliche Bestückung gegen Fotos/CAD verifizieren. |
| P1 | Kamera-/LED-Kandidaten recherchiert; Kalibrierung in 12 Messing- und 4 weiße Referenzen plus Hamming-Marker aufgeteilt. | Optik prüfen; Kalibrierkörper zeichnen, Gesamtlängen/Toleranzen festlegen und vermessen. LED nutzt SKR-Bettausgang, kein weiterer USB-Controller. |
| P1 | Sensoren sind nur `inductive_proximity_sensor_m8` bzw. `optical_endstop` benannt. | NPN/PNP, Spannung, Schaltabstand, Logik, Stecker und Kabellänge mit SKR-Eingängen abgleichen. |
| P1 | Netzanschluss, Absicherung, Erdung, Verteilung, Kabel, Stecker und Energieketten-Endanschlüsse sind nicht vollständig beschrieben. | Verdrahtungsplan und Leitungsliste erstellen; Netzteil- und 24-V-Leistungsbedarf prüfen. |
| P1 | Nanotec ST3518M1004-A ist nur im [Herstellerarchiv](https://www.nanotec.com/eu/de/downloads/archiv) auffindbar; SKR V1.3 ist ein älteres Board. | Originalteile und lieferbare Alternativen samt mechanischer/Firmware-Kompatibilität prüfen. |
| P1 | Bei HIWIN/CPC-Führungen fehlen teils Varianten und Schienenlängen, bei igus-Ketten die genaue Gliederzahl und Endverbinder. | Daten aus STEP-Geometrie und Hersteller-Konfigurator abgleichen. |
| P1 | Das veröffentlichte CAD-PDF rendert leer ([Upstream-Issue #2](https://github.com/schutzwerk/PROBoter/issues/2)). | STEP als maßgebliche Geometrie nutzen; eigene 2D-Ableitungen erzeugen. |
| P1 | 16 Git-LFS-Zeiger umfassen Datensätze und Modelle; `ic-pins.zip` gab beim Abruf 404. | Verfügbarkeit der benötigten Objekte einzeln prüfen oder Modelle/Datensätze neu erzeugen. |
| P1 | Originalteile haben verschiedene Lizenzen; für eigene Ergänzungen ist noch keine Lizenz festgelegt. | Lizenzentscheidung für Floronics-Inhalte treffen und Zuordnung zu GPLv3 bzw. CERN-OHL-W v2 dokumentieren. |

## Beschaffungsreihenfolge nach Klärung

1. Zielvariante und Motor-/Elektrikplan freigeben.
2. Fehlende Leiterplatten und Fertigungszeichnungen beschaffen oder erstellen.
3. CAD-Zuschnittliste, Standardteile, Kameras und Endschalter eindeutig spezifizieren.
4. Recherchierte Hersteller-/Distributornummern, Preise und Lagerbestände aus der
   [Bestellliste](../bom/Bestellliste.md) bei finalen Warenkörben aktualisieren;
   Rechnungskauf freischalten lassen und Beipack/Doppelzählungen abziehen.
