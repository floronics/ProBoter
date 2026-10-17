# Montagemodule

Schrittweiser Aufbau in logisch zusammengehörigen Modulen. Definition in [module.json](module.json), Teile mit Mengen in [montage.csv](montage.csv). Mengen sind CAD-Mengen im jeweiligen Fusion-Einbau; Status aus der [Teileliste](../Teileliste.md). In Fusion einblenden: `tools/fusion_show_module.py`.

| Modul | Positionen | Stück | bestellfähig | teilweise geklärt | Fertigung noch offen | Fertigung spezifiziert | nicht identifiziert | nicht benötigt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [M01 Grundgerüst](#modul-01) | 10 | 50 | 2 | 1 | 7 | 0 | 0 | 0 |

<a id="modul-01"></a>

## M01 Grundgerüst

Tragender Rahmen ohne Elektrik, ohne Halter für elektrische Teile, ohne Achsen, Schublade und Verkleidung.

*Abgrenzung mit Luis am 17.10.2026 abgestimmt. Vollständigkeit am 17.10.2026 per Fusion-Kontaktanalyse geprüft (bom/evidence/fusion-measurements.json, tools/fusion_measurements.py).*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-034](../Teileliste.md#cad-034) DIN 7991 M6×20 | `din_7991_m6x20` | 8 von 22 | bestellfähig; 8 von 22 verbinden die Motorplatten mit den 60×30-Profilen; 8 halten die Adapterplatten (X-Antrieb), 6 die Kettenhalter. | Kaufteile |
| [CAD-081](../Teileliste.md#cad-081) Anschraubwinkel 30 / Nut 6 | `screw_on_bracket_30_6` | 18 von 26 | bestellfähig; 18 von 26 verbinden Rahmenprofile; 8 gehören zur Schublade. | Kaufteile |
| [CAD-052](../Teileliste.md#cad-052) Gelenkfuß M6 / Teller Ø40 mm | `hinged_M6_40_dold` | 4 | teilweise geklärt | Kaufteile |
| [CAD-003](../Teileliste.md#cad-003) Grundgestell: Rückseite Platte | `base_back_plate` | 1 | Fertigung noch offen | Blech intern |
| [CAD-012](../Teileliste.md#cad-012) Grundgestell: Rahmen lang Seite | `base_frame_long_side` | 3 | Fertigung noch offen | Weitere Fertigung |
| [CAD-013](../Teileliste.md#cad-013) Grundgestell: Rahmen kurz | `base_frame_short` | 8 | Fertigung noch offen | Weitere Fertigung |
| [CAD-014](../Teileliste.md#cad-014) Grundgestell: Rahmen Seite | `base_frame_side` | 2 | Fertigung noch offen | Weitere Fertigung |
| [CAD-020](../Teileliste.md#cad-020) Grundgestell: vertikal | `base_vertical` | 4 | Fertigung noch offen | Weitere Fertigung |
| [CAD-096](../Teileliste.md#cad-096) X-Achse Motor Platte | `x_motor_plate` | 1 | Fertigung noch offen | Blech intern |
| [CAD-097](../Teileliste.md#cad-097) X-Achse Motor Platte 2 | `x_motor_plate_2` | 1 | Fertigung noch offen | Blech intern |

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Nutenstein mit Steg I-Typ Nut 6, M6 (DOLD 62354-VK) | 8 | SYS-029 | Senkschrauben M6×20 der Motorplatten greifen in die Nut der 60×30-Profile; im CAD kein Gegenstück. |
| Zylinderschraube M4 + Nutenstein I-Typ Nut 6 M4 (DOLD 62347-VK) | 6 | SYS-029 | 6 Bohrungen Ø4,5 der Rückwand liegen auf den langen Profilen; im CAD keine Schrauben. Schraubenlänge aus 3 mm Blech + Nutenstein festlegen (M4×8 oder M4×10). |
| Befestigungssätze der Winkel | 18 | CAD-081 | Bereits enthalten: CAD-081 wird als Satz 62385-BS mit 2 Schrauben M6×12 und 2 Nutensteinen bestellt. |
| Gewinde M6 in Profil-Kernbohrung Ø5 | 4 | CAD-020 | Gelenkfüße sitzen in den unteren Enden der 4 Vertikalprofile; Kernbohrung Ø5 ist das M6-Kernloch. Bearbeitung, kein Kaufteil. |

**Bei der Prüfung aus dem Modul genommen**

- DIN 7991 M6×14 (6 Stück): befestigen die Schubladen-Dummyplatte, gehören zur Schublade.
- Adapterplatten CAD-016 bis CAD-019: tragen die X-Riemenantriebe (M3/M4-Schrauben aus x_belt_drive) und gehören zur X-Achse. Fertigungsverfahren weiter mit PRÜFEN-Vermerk.
- Muttern M8×1 an den Motorplatten (8 Stück): halten induktive Sensoren, gehören zur Elektrik.

**Offene Fragen**

- Abdeckungen oben/seitlich: aussteifend (dann Grundgerüst) oder reine Verkleidung?
- 4 weitere Ø4,5-Bohrungen der Rückwand treffen kein Profil; vermutlich für Netzteil oder Elektronik.
