# Montagemodule

Schrittweiser Aufbau in logisch zusammengehörigen Modulen. Definition in [module.json](module.json), Teile mit Mengen in [montage.csv](montage.csv). Mengen sind CAD-Mengen im jeweiligen Fusion-Einbau; Status aus der [Teileliste](../Teileliste.md). In Fusion einblenden: `tools/fusion_show_module.py`.

| Modul | Positionen | Stück | bestellfähig | teilweise geklärt | Fertigung noch offen | Fertigung spezifiziert | nicht identifiziert | nicht benötigt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [M01 Grundgerüst](#modul-01) | 15 | 86 | 3 | 1 | 11 | 0 | 0 | 0 |

<a id="modul-01"></a>

## M01 Grundgerüst

Tragender Rahmen ohne Elektrik, ohne Halter für elektrische Teile, ohne Achsen, Schublade und Verkleidung.

*Abgrenzung mit Luis am 17.10.2026 abgestimmt; Vollständigkeit noch nicht geprüft.*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-033](../Teileliste.md#cad-033) DIN 7991 M6×14 | `din_7991_m6x14` | 6 | bestellfähig | Kaufteile |
| [CAD-034](../Teileliste.md#cad-034) DIN 7991 M6×20 | `din_7991_m6x20` | 22 | bestellfähig | Kaufteile |
| [CAD-081](../Teileliste.md#cad-081) Anschraubwinkel 30 / Nut 6 | `screw_on_bracket_30_6` | 26 | bestellfähig | Kaufteile |
| [CAD-052](../Teileliste.md#cad-052) Gelenkfuß M6 / Teller Ø40 mm | `hinged_M6_40_dold` | 4 | teilweise geklärt | Kaufteile |
| [CAD-003](../Teileliste.md#cad-003) Grundgestell: Rückseite Platte | `base_back_plate` | 1 | Fertigung noch offen | Blech intern |
| [CAD-012](../Teileliste.md#cad-012) Grundgestell: Rahmen lang Seite | `base_frame_long_side` | 3 | Fertigung noch offen | Weitere Fertigung |
| [CAD-013](../Teileliste.md#cad-013) Grundgestell: Rahmen kurz | `base_frame_short` | 8 | Fertigung noch offen | Weitere Fertigung |
| [CAD-014](../Teileliste.md#cad-014) Grundgestell: Rahmen Seite | `base_frame_side` | 2 | Fertigung noch offen | Weitere Fertigung |
| [CAD-016](../Teileliste.md#cad-016) Grundgestell: Platte Adapter 1 | `base_plate_adapter_1` | 2 | Fertigung noch offen | CNC extern |
| [CAD-017](../Teileliste.md#cad-017) Grundgestell: Platte Adapter 2 | `base_plate_adapter_2` | 2 | Fertigung noch offen | CNC extern |
| [CAD-018](../Teileliste.md#cad-018) Grundgestell: Platte Adapter links | `base_plate_adapter_left` | 2 | Fertigung noch offen | CNC extern |
| [CAD-019](../Teileliste.md#cad-019) Grundgestell: Platte Adapter rechts | `base_plate_adapter_right` | 2 | Fertigung noch offen | CNC extern |
| [CAD-020](../Teileliste.md#cad-020) Grundgestell: vertikal | `base_vertical` | 4 | Fertigung noch offen | Weitere Fertigung |
| [CAD-096](../Teileliste.md#cad-096) X-Achse Motor Platte | `x_motor_plate` | 1 | Fertigung noch offen | Blech intern |
| [CAD-097](../Teileliste.md#cad-097) X-Achse Motor Platte 2 | `x_motor_plate_2` | 1 | Fertigung noch offen | Blech intern |

**Offene Fragen**

- Adapterplatten: Grundgerüst oder X-Achse (evtl. Motor-Adapterplatten)?
- Abdeckungen oben/seitlich: aussteifend (dann Grundgerüst) oder reine Verkleidung?
- Nutensteine für die 26 Winkel sind nicht im CAD (SYS-029).
