# Floronics-Nachbau des PROBoters

Dieses Repository ist ein Fork von
[SCHUTZWERK/PROBoter](https://github.com/schutzwerk/PROBoter). Der Originalcode
und die Original-Hardwaredaten liegen direkt im Repository. Unsere Recherche
und Beschaffungsunterlagen sind als eigene Dateien ergänzt; die Herkunft der
Quellen steht in [Quellen.md](Quellen.md).

## Orientierung

| Pfad | Inhalt |
|---|---|
| [`hardware/`](../hardware/) | Originales CAD-Modell, Rendering und Hardware-Lizenz |
| [`firmware/`](../firmware/) | Originale Firmware für die Steuerplatinen |
| [`software/`](../software/) | Originale Dienste und Weboberfläche |
| [`image_data_sets/`](../image_data_sets/) | Hinweise und Git-LFS-Zeiger zu Datensätzen und Modellen |
| [`publications/`](../publications/) | Originale wissenschaftliche Veröffentlichungen |
| [`docs/Aufbau.md`](Aufbau.md) | Zusammenfassung des veröffentlichten Aufbaus |
| [`docs/Offene-Punkte.md`](Offene-Punkte.md) | Technische Klärpunkte vor der Bestellung |
| [`bom/Bestellliste.md`](../bom/Bestellliste.md) | Menschenlesbare Beschaffungsplanung |
| [`bom/Teileliste.md`](../bom/Teileliste.md) | 160 Positionen, gegliedert nach den 13 Fusion-Komponenten plus K14 für Teile ohne CAD-Körper |
| [`bom/Fertigung.md`](../bom/Fertigung.md) | 3D-Druck, Blech, CNC, weitere Fertigung und PCB getrennt |
| [`bom/Kosten.md`](../bom/Kosten.md) | Webpreise, eigene Schätzungen, Packungsrechnung und unbezifferte Bedarfe |
| [`bom/Lieferanten.md`](../bom/Lieferanten.md) | DE-/EU-Anbieter mit belegten Rechnungskaufbedingungen |
| [`bom/Reproduktion.md`](../bom/Reproduktion.md) | Datenfluss und reproduzierbare Prüfung |
| [`bom/CAD-Teileliste.md`](../bom/CAD-Teileliste.md) | Vollständige Inventur der 120 benannten CAD-Blattteile |
| [`bom/cad-inventory.csv`](../bom/cad-inventory.csv) | STEP-Rohinventur inklusive Unterbaugruppen |
| [`tools/`](../tools/) | Skripte zum erneuten Auslesen des STEP-Modells |

## Arbeitsstand und Herkunft

Die [Bestellliste](../bom/Bestellliste.md) enthält jetzt recherchierte Artikel,
Preise und Budgetansätze; eine vollständige Komplettbestellung bleibt wegen
der dokumentierten Elektronik-/Fertigungslücken offen. Das
veröffentlichte STEP-Modell enthält 447 Baugruppenbeziehungen. Nach rekursiver
Auflösung wiederverwendeter Baugruppen ergeben sich 1.066 Blattteil-Vorkommen
mit 120 verschiedenen Namen und 53 Unterbaugruppen-Vorkommen. Anzahl und Benennung
liefern keine geprüften Bestellnummern oder Fertigungszeichnungen. Mehrere
Zuordnungen müssen noch elektrisch und hinsichtlich Passungen geprüft werden. Der
[Fusion-Abgleich](../bom/CAD-Pruefung.md) ist durchgeführt: 12 NEMA17 fehlen im
Import, acht NEMA14-Vorkommen werden als vier alternative Paare untersucht.
Planung: 12 NEMA17 + 4 NEMA14, 16 Treiber; Z-Menge weiterhin Hypothese. Die
[offenen Punkte](Offene-Punkte.md) dokumentieren diese Aufgaben.

Der Fork bewahrt die Originalhistorie. Die Basis ist
[`b6184ad`](https://github.com/schutzwerk/PROBoter/commit/b6184ada8ddee74df746ce800c81038e8d482e1e)
auf `master`. Lokal zeigt `origin` auf Floronics und `upstream` auf
SCHUTZWERK. Änderungen am Original werden getrennt von unseren Ergänzungen
committet, damit der Bezug zu SCHUTZWERK nachvollziehbar bleibt.

Die Original-Lizenzen stehen in [`LICENSE`](../LICENSE),
[`hardware/LICENSE`](../hardware/LICENSE) und weiteren Unterordnern.
Eine Lizenz für eigene Floronics-Inhalte muss noch festgelegt werden; siehe
[offene Punkte](Offene-Punkte.md).

## CAD-Inventur aktualisieren

```powershell
python tools/extract_step_bom.py hardware/3d_models/proboter.stp --output bom/cad-inventory.csv
python tools/render_cad_inventory.py bom/cad-inventory.csv bom/CAD-Teileliste.md
```

Diese Inventur liest benannte STEP-Baugruppenvorkommen. Sie ersetzt keine
Fertigungszeichnungen, Schaltpläne oder technische Freigabe.
