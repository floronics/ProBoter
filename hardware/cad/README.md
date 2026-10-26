# PROBoter Solid-Edge-CAD (SCHUTZWERK-Original)

Originaldateien von SCHUTZWERK im Solid-Edge-Format (`.asm` Baugruppe, `.par` Teil, `.psm` Blechteil, `.dft` Zeichnung).
Gesamtbaugruppe: `probotor.asm`. Die STEP-Ausleitung liegt in [../3d_models/proboter.stp](../3d_models/proboter.stp).

| Ordner | Bedeutung |
|---|---|
| `printed_parts` | Druckteile, selbst drucken (PETG) |
| `mechanical_parts` | Werkstatt- und Zuschnittteile. Motorhalteplatten (`x_motor_plate*`) und Seitenplatten (`x_side_plate*`) werden selbst gefräst, `*_raw` sind die Rohteile |
| `standard_parts` | Kaufteile (Normteile, Motoren, Führungen, Elektronik) |
| `pcbs` | Prüfspitzen-Platine (nur Körper, keine Fertigungsdaten) |

Teileliste mit Abgleich gegen die Gesamt-Teileliste: [bom/SolidEdge-Teileliste.md](../../bom/SolidEdge-Teileliste.md).
