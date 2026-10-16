# CAD-Prüfung über Fusion MCP

Stand: 16.10.2026. Quelle: unveränderter STEP-Import im geöffneten Fusion-Dokument `proboter`.

## Nachvollziehbare Rohdaten

- [Alle Einbaupfade, Transformationen, Körper, Volumina und Hüllmaße](evidence/fusion-inventory.json)
- [Abgleich aller 120 STEP-Teilnamen mit Fusion](evidence/cad-geometry.csv)
- [Prüfsummen und Zähler](evidence/manifest.json)
- Erfassung: `tools/fusion_inventory.py` über Fusion MCP mit `readOnly: true`; Auswertung: `tools/analyze_fusion_inventory.py`.

Fusion liefert 1.054 Blattvorkommen und 53 Baugruppenvorkommen, STEP 1.066 Blattvorkommen und ebenfalls 53 Baugruppenvorkommen. Die Differenz sind **sämtliche zwölf NEMA-17-Motoren**. Sie bleiben in der Teileliste; ihr Fehlen im Import beweist nicht, dass sie beim Bau entfallen.

## Mengenentscheidungen und Widersprüche

| Thema | Beobachtung | Konsequenz |
|---|---|---|
| X/Y-Antriebe | STEP: acht X-Antriebe und vier Y-Antriebe mit ST4118M1804-A; Fusion enthält die jeweiligen Motorhalter, aber keine NEMA-17-Motorkörper | Arbeitsmenge zwölf NEMA-17, Quelle STEP + Firmware/Blog; fehlende Importgeometrie markieren |
| Z-Antriebe | Je Y-Schlitten zwei NEMA-14-Vorkommen mit nahezu gleichem Ursprung (ca. 1,6 mm Abstand), unterschiedlich orientiert; ein Z-Riemen je Prüfeinheit | **Vier NEMA-14 als Planungshypothese**, acht CAD-Vorkommen erhalten; alternative Einbaulagen vor Fertigung prüfen |
| Treiber | Firmware konfiguriert X, X2, Y, Z je SKR | 16 Treibermodule für vier Boards; passt zur Planung 12 NEMA-17 + 4 NEMA-14 |
| Kameras | Vier USB-Mikroskope im CAD; Hardware-Blog beschreibt nur eines bestückt und eine stationäre Kamera | Grundausstattung: ein bewegliches Mikroskop + eine Übersichtskamera; drei weitere bewegliche Kameras separat als Option |
| Sensoren | 24 M8-Sensorkörper und vier optische Endschalter auch in Fusion vorhanden | CAD-Mengen erhalten; elektrische Spezifikation und Zuordnung offen |
| Energieketten | 16 kurze und acht lange Baukörper; jeweils mehrere Körper pro Kettenkomponente | Nicht einzelne Körper als weitere Ketten zählen; Anzahl weiterhin CAD-Bedarf, Einbauprüfung erforderlich |

Die Z-Motor-Reduktion ist eine **begründete Hypothese**, keine nachgewiesene Original-BOM. Es werden keine Motoren, Modelle oder Einbauvarianten gelöscht.

## Direkt messbare Eckdaten

| Teil | Messung in lokalen Bauteilachsen |
|---|---|
| CPC X-Schiene | 600 × 12 × 7,5 mm; zwei Vorkommen |
| HIWIN Z-Schiene | 150 × 12 × 8 mm; vier Vorkommen |
| Runde X-Führung | Ø10 × 450 mm; acht Vorkommen |
| PCB-Halter-Führungsstange | Ø10 × 356,8 mm; zwei Vorkommen |
| Prüfspitzen-PCB | Hüllmaß 26,67 × 10,96 × 1,6 mm; vier Vorkommen |
| X-/Y-Riemen | Modellbreite jeweils 6 mm |
| Z-Riemen | Modellbreite 9 mm |
| Rückplatte | 650 × 270 × 3 mm |
| Hauptprofile | 30×30 und 60×30 mm; Zuschnittlängen in Geometrietabelle |

Hüllmaße sind keine technischen Zeichnungen: Rundungen, Einbauorientierung und überstehende Features können Maße beeinflussen. Riemen-Hülllängen sind insbesondere keine Bestelllängen. Im STEP-Import gesetzte Standardmaterialien werden nicht als Werkstoffnachweis verwendet.

## Reproduzieren

1. Dieselbe STEP-Datei in Fusion öffnen, ohne Teile zu verändern.
2. `tools/fusion_inventory.py` mit dem Fusion-MCP-Skriptwerkzeug im Lesemodus ausführen. Der Exportpfad steht oben im Skript und ist bei einem anderen Arbeitsplatz anzupassen.
3. `python tools/analyze_fusion_inventory.py` ausführen.
4. Abweichungen und Prüfsummen prüfen; Bestellmengen bleiben gesonderte, begründete Entscheidungen.
