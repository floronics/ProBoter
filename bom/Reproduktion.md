# Datenfluss und Reproduktion

## Dateien

| Datei | Rolle |
|---|---|
| `cad-inventory.csv` | Rohzählung der STEP-Baugruppe, inklusive Baugruppen; keine Einkaufsmengen |
| `evidence/fusion-inventory.json` | Fusion-Export aller Einbaupfade, Sichtbarkeit, Transformationen, Hüllmaße, Volumen |
| `evidence/cad-geometry.csv` | 120 STEP-Blattpositionen mit stabilen CAD-IDs, Fusion-Abgleich und lokaler Geometrie |
| `evidence/cylindrical-features.json` | Zusätzliche zylindrische Flächen: Durchmesser, Achsen und Ursprünge in mm |
| `evidence/manifest.json` | SHA256 und Inventurzähler |
| `evidence/component-inventory.csv` | STEP-Blattteile je oberster Komponente (13 Einbauten) und direkter Unterbaugruppe |
| `data/offers.json` | Kuratierte Preisbeobachtungen, Hersteller, Artikelnummern, Varianten, Packungen und Grenzen |
| `../tools/build_procurement.py` | Explizite Zuordnungen, Mengenentscheidungen, Fertigungsvorschläge, Ergänzungen und eigene Budgetannahmen |
| `teileliste.csv` | Gesamte Planungsstückliste; STEP-/Fusion-/Planmengen getrennt |
| `teileliste-komponenten.csv` | Teile je Komponente K01–K13 laut CAD, K14 = Teile ohne CAD-Körper |
| `bestellliste.csv` | Kostenbesitzer, Bestellpackungen, Preise, Steuerbasis, Lieferstatus, Shoplinks und Vorbehalte |
| `kosten.json` | Reproduzierbare Summen und Liste der unbezifferten Positionen |

`CAD-xxx` bleiben an den aktuellen Inventurstand gebunden. Neu hinzukommende Teile
bekommen neue IDs; bestehende IDs nicht neu alphabetisch vergeben. Der Generator
übernimmt die IDs aus der Geometrie-CSV. Vor einer neuen CAD-Version die Zuordnung
bewusst migrieren. `SYS-xxx` sind ergänzte Systempositionen. `cost_id` verknüpft
jede benötigte Position mit genau einem Kostenposten; mehrere Teile können denselben
Material-/Satzposten nutzen. Optionen und begründete Ausschlüsse kosten nicht zusätzlich.

## Ausführen

Python 3, nur Standardbibliothek, im Repository:

```text
python tools/analyze_fusion_inventory.py
python tools/build_procurement.py
python -m unittest discover -s tools -p "test_*.py"
```

Der erste Befehl arbeitet auf dem bereits gespeicherten Fusion-Export.
Eine erneute STEP-Rohinventur ist über `python tools/extract_step_bom.py --help`
dokumentiert; der Originalstand muss dieselbe SHA256 im Manifest haben.
Die Komponentenzuordnung entsteht mit
`python tools/extract_step_bom.py hardware/3d_models/proboter.stp --output bom/cad-inventory.csv --components bom/evidence/component-inventory.csv`.
Der Generator ordnet die STEP-Einbauten über Name und Reihenfolge den Fusion-Pfaden zu
(drittes `x_slide` = `x_slide:3`).

Live-Fusion-Erfassung: unveränderten STEP-Import öffnen, dann die Funktion `run`
aus `tools/fusion_inventory.py` über Fusion MCP mit `readOnly:true` ausführen.
Exportpfad oben im Skript anpassen. CAD wird nicht verändert. Fusion-API verwendet
cm für Längen und cm³ für Volumen; Längen werden ×10 in mm umgerechnet. Die 12 fehlenden
NEMA17-Importkörper dürfen nicht aus der STEP-Bedarfsplanung verschwinden.
Für Zylinder-Messungen analog `tools/fusion_cylinders.py` ausführen.

Die Markdown-Dokumente `Bestellliste`, `Teileliste`, `Fertigung`, `Ungeklaert`
und `Kosten` sind generiert. Änderungen an Mengen/Zuordnungen in `build_procurement.py`,
an Webangeboten in `offers.json` vornehmen und neu generieren. `Lieferanten.md`,
`CAD-Pruefung.md` und diese Datei sind redaktionell gepflegt.

## Prüfkriterien

- Alle 120 CAD-IDs genau einmal; 1.066 STEP-Vorkommen erhalten.
- Benötigte Teile haben Kostenbesitzer und konkrete Klärangabe; keine Baugruppendoppelzählung.
- Bestellfähig nur mit genauer Variante und Bezugsquelle.
- Fehlende Preise bleiben leer/None; Alternativen nicht in Grundsumme.
- Packungsrundung, Nettopreise, Bruttorechnung und Materialpools geprüft.
- Dokumentlinks lokal prüfen; aktuelle Webverfügbarkeit ist kein Offline-Test.

Preisrecherche ist ein Datumsstand und wird beim Generieren nicht automatisch aktualisiert.
Ein neuer Lauf belegt keine erneute Shopprüfung. Fertigungsangebote, echte Materialtests,
Slicerläufe und eine vollständige elektrische Freigabe sind noch nicht erfolgt.

Ergebnisse der Prüfung: [Prüfbericht](Pruefbericht.md).
