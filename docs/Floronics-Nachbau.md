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
| [`bom/CAD-Teileliste.md`](../bom/CAD-Teileliste.md) | Vollständige Inventur der 120 benannten CAD-Blattteile |
| [`bom/cad-inventory.csv`](../bom/cad-inventory.csv) | STEP-Rohinventur inklusive Unterbaugruppen |
| [`tools/`](../tools/) | Skripte zum erneuten Auslesen des STEP-Modells |

## Arbeitsstand und Herkunft

Die [Bestellliste](../bom/Bestellliste.md) ist noch nicht bestellfertig. Das
veröffentlichte STEP-Modell enthält 447 Einbauvorkommen, darunter 416
Blattteil-Vorkommen mit 120 verschiedenen Namen. Ihre Anzahl und Benennung
liefern keine geprüften Bestellnummern oder Fertigungszeichnungen. Mehrere
Mengen widersprechen dem beschriebenen Vier-Prüfspitzen-Aufbau; die
[offenen Punkte](Offene-Punkte.md) dokumentieren diese Abweichungen.

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
