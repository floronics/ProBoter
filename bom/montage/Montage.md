# Montagemodule

Schrittweiser Aufbau in logisch zusammengehörigen Modulen. Definition in [module.json](module.json), Teile mit Mengen in [montage.csv](montage.csv). Mengen sind CAD-Mengen im jeweiligen Fusion-Einbau; Status aus der [Teileliste](../Teileliste.md). In Fusion einblenden: `tools/fusion_show_module.py`.

| Modul | Positionen | Stück | bestellfähig | teilweise geklärt | Fertigung noch offen | Fertigung spezifiziert | nicht identifiziert | nicht benötigt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [M01 Grundgerüst](#modul-01) | 10 | 50 | 2 | 1 | 7 | 0 | 0 | 0 |
| [M02 X-Achse](#modul-02) | 33 | 434 | 18 | 2 | 13 | 0 | 0 | 0 |

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

<a id="modul-02"></a>

## M02 X-Achse

X-Führungen und 8 X-Riemenantriebe auf den Motorplatten sowie die 4 X-Wagen als Tragstruktur der Prüfeinheiten. Motoren als Antrieb enthalten; Sensoren, Endschalterhalter, Kabelhalter, Energieketten und der Y-Antrieb auf dem Wagen gehören in eigene Module.

*Am 17.10.2026 angelegt und per Fusion-Kontaktanalyse geprüft (X-Wagen 1 und X-Antrieb 1 stellvertretend, alle Einbauten gleich).*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-027](../Teileliste.md#cad-027) CPC MR12ML Führungswagen | `cpc_MR12ML` | 8 | bestellfähig | Kaufteile |
| [CAD-031](../Teileliste.md#cad-031) DIN 7991 M3×8 | `din_7991_m3x8` | 32 | bestellfähig | Kaufteile |
| [CAD-032](../Teileliste.md#cad-032) DIN 7991 M6×12 | `din_7991_m6x12` | 16 | bestellfähig | Kaufteile |
| [CAD-034](../Teileliste.md#cad-034) DIN 7991 M6×20 | `din_7991_m6x20` | 8 von 22 | bestellfähig; 8 von 22 befestigen die Adapterplatten an den Motorplatten. | Kaufteile |
| [CAD-035](../Teileliste.md#cad-035) DIN 912 M3×10 | `din_912_m3x10` | 32 | bestellfähig | Kaufteile |
| [CAD-038](../Teileliste.md#cad-038) DIN 912 M3×16 | `din_912_m3x16` | 16 | bestellfähig | Kaufteile |
| [CAD-039](../Teileliste.md#cad-039) DIN 912 M3×18 | `din_912_m3x18` | 32 | bestellfähig | Kaufteile |
| [CAD-042](../Teileliste.md#cad-042) DIN 912 M3×8 | `din_912_m3x8` | 32 | bestellfähig | Kaufteile |
| [CAD-044](../Teileliste.md#cad-044) DIN 912 M4×20 | `din_912_m4x20` | 16 | bestellfähig | Kaufteile |
| [CAD-045](../Teileliste.md#cad-045) DIN 912 M4×30 | `din_912_m4x30` | 16 | bestellfähig | Kaufteile |
| [CAD-046](../Teileliste.md#cad-046) DIN 912 M5×10 | `din_912_m5x10` | 32 | bestellfähig | Kaufteile |
| [CAD-047](../Teileliste.md#cad-047) DIN 912 M5×14 | `din_912_m5x14` | 4 | bestellfähig | Kaufteile |
| [CAD-056](../Teileliste.md#cad-056) Sechskantmutter DIN 934 M3 A2 | `iso_8673_nut_m3` | 16 | bestellfähig | Kaufteile |
| [CAD-057](../Teileliste.md#cad-057) Sechskantmutter DIN 934 M4 A2 | `iso_8673_nut_m4` | 32 | bestellfähig | Kaufteile |
| [CAD-064](../Teileliste.md#cad-064) Nanotec ST4118M1804-A NEMA17 X/Y-Motor | `nanotec_nema_17_ST4118M1804-A` | 8 | bestellfähig | Kaufteile |
| [CAD-079](../Teileliste.md#cad-079) SHF10 Flanschhalter fürØ10 mm Welle | `rod_holder_flange_d10_dold` | 16 | bestellfähig | Kaufteile |
| [CAD-087](../Teileliste.md#cad-087) GT2-Riemen X, 6 mm breit | `x_belt` | 8 | bestellfähig | Kaufteile |
| [CAD-095](../Teileliste.md#cad-095) CPC MR12M Führungsschiene 600 mm | `x_guiding_cpc_MR12M` | 2 | bestellfähig | Kaufteile |
| [CAD-077](../Teileliste.md#cad-077) GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | `pulley_gt2_z16_6mm` | 8 | teilweise geklärt | Kaufteile |
| [CAD-078](../Teileliste.md#cad-078) GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | `return_pulley_gt2_z16_6mm` | 16 | teilweise geklärt | Kaufteile |
| [CAD-015](../Teileliste.md#cad-015) Grundgestell: NEMA 14 auf 17 Adapter | `base_nema_14_to_17_adapter` | 8 | Fertigung noch offen | 3D-Druck intern |
| [CAD-016](../Teileliste.md#cad-016) Grundgestell: Platte Adapter 1 | `base_plate_adapter_1` | 2 | Fertigung noch offen | CNC extern |
| [CAD-017](../Teileliste.md#cad-017) Grundgestell: Platte Adapter 2 | `base_plate_adapter_2` | 2 | Fertigung noch offen | CNC extern |
| [CAD-018](../Teileliste.md#cad-018) Grundgestell: Platte Adapter links | `base_plate_adapter_left` | 2 | Fertigung noch offen | CNC extern |
| [CAD-019](../Teileliste.md#cad-019) Grundgestell: Platte Adapter rechts | `base_plate_adapter_right` | 2 | Fertigung noch offen | CNC extern |
| [CAD-021](../Teileliste.md#cad-021) Riemen Spanner GT2 Basis | `belt_tightener_GT2_base` | 16 | Fertigung noch offen | 3D-Druck intern |
| [CAD-022](../Teileliste.md#cad-022) Riemen Spanner GT2 Flügel | `belt_tightener_GT2_wing` | 16 | Fertigung noch offen | 3D-Druck intern |
| [CAD-088](../Teileliste.md#cad-088) X-Achse Riemen Halter | `x_belt_holder` | 4 | Fertigung noch offen | 3D-Druck intern |
| [CAD-089](../Teileliste.md#cad-089) X-Achse Riemen Halter 1 | `x_belt_holder_1` | 12 | Fertigung noch offen | 3D-Druck intern |
| [CAD-098](../Teileliste.md#cad-098) X-Achse rund Schiene | `x_round_rail` | 8 | Fertigung noch offen | Weitere Fertigung |
| [CAD-099](../Teileliste.md#cad-099) X-Achse Seite Platte | `x_side_plate` | 4 | Fertigung noch offen | Blech intern |
| [CAD-100](../Teileliste.md#cad-100) X-Achse Seite Platte beweglich | `x_side_plate_moving` | 4 | Fertigung noch offen | Blech intern |
| [CAD-103](../Teileliste.md#cad-103) X-Achse Schlitten Versteifung Träger | `x_slide_stiffener_beam` | 4 | Fertigung noch offen | Weitere Fertigung |

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Gewinde M3 in den Motorplatten (Bohrungen Ø2,46) | 32 | CAD-096/097 | M3×10 der Riemenspanner haben keine Mutter; die Platten haben je 16 Kernlöcher Ø2,46 für M3. Bearbeitung, kein Kaufteil. |
| Gewinde M5 in den Wagen-Seitenplatten bzw. Muttern M5 | 36 | CAD-099/100 | M5×10/M5×14 an Flanschhaltern und Versteifung haben im CAD keine Mutter. Ob die 5-mm-Platten Gewinde bekommen, an der Geometrie prüfen. |

**Bei der Prüfung aus dem Modul genommen**

- Induktive Sensoren, M8×1-Muttern, Endschalterhalter und -adapter, Kabelhalter: Elektrik.
- Energieketten und Kettenadapter am Wagen: eigenes Modul Kabelführung.
- Y-Riemenantrieb auf dem Wagen (y_belt_drive) und die 4 M3×10 direkt am Wagen: Modul Y-Achse.

**Offene Fragen**

- M3×18 (32) zwischen NEMA-Adapter, Motorplatte und Adapterplatte: im CAD keine Mutter und kein Gewinde (Adapterplatte nur Ø3,4). Mutter M3 oder Gewinde in der Adapterplatte klären.
- Senkschrauben M6×12 am Wagen greifen in den Versteifungsträger 40×16: Gewinde im Träger oder Nutenstein klären.
