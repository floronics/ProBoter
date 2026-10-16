# Offene Punkte vor dem Nachbau

**Stand: 16.10.2026.** `P0` blockiert eine verlässliche Komplettbestellung;
`P1` wird für Fertigung oder Inbetriebnahme benötigt. Die Mengen der
[CAD-Teileliste](../bom/CAD-Teileliste.md) bleiben bis zur Klärung
als Modellzählung gekennzeichnet.

| Prio | Frage / belegte Lücke | Nächste Prüfung |
|---|---|---|
| P0 | Vier Prüfeinheiten laut [Blog Teil II](https://www.schutzwerk.com/en/blog/proboter-02/) und [Firmware](../firmware/README.md), aber im STEP nur 6 Motoren, 2 `probe_tip_pcb`, 2 `z_drive_belt` und 4 Steuerplatinen. | Zielkonfiguration (zwei oder vier funktionierende Spitzen) festlegen; STEP-Baugruppenbaum je Einheit in CAD öffnen und Motoren, Z-Antriebe und Prüfspitzen abgleichen. |
| P0 | `signal_multiplexer_dummy` statt realer Multiplexer-Platine. | Schaltplan, PCB-Layout, Fertigungsdaten, Bestückung und elektrisches Interface beim Originalprojekt ermitteln oder neu konstruieren. |
| P0 | `probe_tip_pcb` ist nur ein CAD-Körper; keine Schaltpläne/Gerber für die Prüfspitzenplatinen. | Pinbelegung, Kontaktgeometrie, Fertigungsdaten und reale Stückzahl klären. |
| P0 | Für 61 individuell benannte CAD-Teile fehlen Einzelteilzeichnungen, Material, Toleranzen und Fertigungsverfahren. | Gesamt-STEP in einem CAD-System in Einzelteile zerlegen; Druck-, Fräs-, Laser- und Profilteile trennen; Zuschnittliste und Herstellzeichnungen erstellen. |
| P0 | Riemenlängen und teils Breiten/Bohrungen der GT2-Rollen sind nicht bestellfähig spezifiziert. | Aus STEP die Umlenkwege, Achsabstände und Wellenmaße prüfen; Riemenlängen mit Spannreserve berechnen. |
| P0 | Die [Firmware-Konfiguration](../firmware/Marlin/Configuration.h) nennt X/X2/Y/Z mit TMC2130, im STEP sind aber nur sechs Motoren. | Motor-/Treiberplan je Probe erstellen; Treibermodule (möglicherweise bis 16) erst danach bestellen. |
| P0 | `signal_multiplexer_dummy`, `pcb_dummy` und `base_drawer_dummy_plate` sind Platzhalternamen. | Für jeden entscheiden: echtes Teil ersetzen, nur Demonstrationskörper oder konstruktiv erforderlich. |
| P1 | Blog nennt eine bewegliche und eine statische Kamera; STEP nennt zwei USB-Mikroskope. | Kameramodelle, Optik, Halterung, Arbeitsabstand und Beleuchtung gegen Fotos/CAD verifizieren. |
| P1 | Statische Kamera, weißer LED-Streifen und Kalibrierplatte mit Messingreferenzen fehlen als bestellfähige CAD-Positionen. | Technische Spezifikation, Mengen und Befestigung festlegen. |
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
4. Erst danach Hersteller-/Distributornummern, aktuelle Preise und Lagerbestände
   in der [Bestellliste](../bom/Bestellliste.md) ergänzen.
