# Montagemodule

Schrittweiser Aufbau in logisch zusammengehörigen Modulen. Definition in [module.json](module.json), Teile mit Mengen in [montage.csv](montage.csv). Mengen sind CAD-Mengen im jeweiligen Fusion-Einbau; Status aus der [Teileliste](../Teileliste.md). In Fusion einblenden: `tools/fusion_show_module.py`.

| Modul | Positionen | Stück | bestellfähig | teilweise geklärt | Fertigung noch offen | Fertigung spezifiziert | nicht identifiziert | nicht benötigt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [M01 Grundgerüst](#modul-01) | 10 | 50 | 2 | 1 | 7 | 0 | 0 | 0 |
| [M02 X-Achse](#modul-02) | 33 | 434 | 18 | 2 | 13 | 0 | 0 | 0 |
| [M03 Y-Achse](#modul-03) | 27 | 168 | 15 | 2 | 10 | 0 | 0 | 0 |
| [M04 Z-Achse](#modul-04) | 20 | 100 | 12 | 2 | 6 | 0 | 0 | 0 |
| [M05 Schublade und Platinenhalter](#modul-05) | 15 | 53 | 6 | 1 | 7 | 0 | 1 | 0 |

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

<a id="modul-03"></a>

## M03 Y-Achse

4 Y-Riemenantriebe auf den X-Wagen und die 4 Y-Schlitten (2 normal, 2 gespiegelt) mit Gleitbuchsen auf den Ø10-Wellen und Riemenklemme. Ohne Z-Antrieb, Kamera, Endschalter und Energiekette.

*Am 17.10.2026 angelegt und per Fusion-Kontaktanalyse geprüft (y_slide (1):1, y_slide_mirrored (1):1 und Y-Antrieb 1 stellvertretend).*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-030](../Teileliste.md#cad-030) DIN 562 M4 Vierkantmutter | `din_562_m4_square_nut` | 8 von 12 | bestellfähig; 8 von 12 an den Abstandsstangen; 4 am Z-Endschalter-Auslöser. | Kaufteile |
| [CAD-035](../Teileliste.md#cad-035) DIN 912 M3×10 | `din_912_m3x10` | 8 | bestellfähig | Kaufteile |
| [CAD-038](../Teileliste.md#cad-038) DIN 912 M3×16 | `din_912_m3x16` | 4 | bestellfähig | Kaufteile |
| [CAD-038](../Teileliste.md#cad-038) DIN 912 M3×16 | `din_912_m3x16` | 8 | bestellfähig; Riemenklemme. | Kaufteile |
| [CAD-041](../Teileliste.md#cad-041) DIN 912 M3×30 | `din_912_m3x30` | 4 von 8 | bestellfähig; 4 von 8 an den Abstandsstangen; 4 halten den Kamerahalter. | Kaufteile |
| [CAD-044](../Teileliste.md#cad-044) DIN 912 M4×20 | `din_912_m4x20` | 4 | bestellfähig | Kaufteile |
| [CAD-045](../Teileliste.md#cad-045) DIN 912 M4×30 | `din_912_m4x30` | 4 | bestellfähig | Kaufteile |
| [CAD-045](../Teileliste.md#cad-045) DIN 912 M4×30 | `din_912_m4x30` | 16 | bestellfähig | Kaufteile |
| [CAD-056](../Teileliste.md#cad-056) Sechskantmutter DIN 934 M3 A2 | `iso_8673_nut_m3` | 4 | bestellfähig | Kaufteile |
| [CAD-056](../Teileliste.md#cad-056) Sechskantmutter DIN 934 M3 A2 | `iso_8673_nut_m3` | 8 von 24 | bestellfähig; 8 von 24 an der Riemenklemme; Rest Z-Antrieb, Endschalter, Kamera. | Kaufteile |
| [CAD-057](../Teileliste.md#cad-057) Sechskantmutter DIN 934 M4 A2 | `iso_8673_nut_m4` | 8 | bestellfähig | Kaufteile |
| [CAD-057](../Teileliste.md#cad-057) Sechskantmutter DIN 934 M4 A2 | `iso_8673_nut_m4` | 24 | bestellfähig | Kaufteile |
| [CAD-064](../Teileliste.md#cad-064) Nanotec ST4118M1804-A NEMA17 X/Y-Motor | `nanotec_nema_17_ST4118M1804-A` | 4 | bestellfähig | Kaufteile |
| [CAD-080](../Teileliste.md#cad-080) GleitbuchseØ10 innen / Ø19 außen / Länge 29 mm | `rod_slide_d10_l19` | 16 | bestellfähig | Kaufteile |
| [CAD-104](../Teileliste.md#cad-104) GT2-Riemen Y, 6 mm breit | `y_belt` | 4 | bestellfähig | Kaufteile |
| [CAD-077](../Teileliste.md#cad-077) GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | `pulley_gt2_z16_6mm` | 4 | teilweise geklärt | Kaufteile |
| [CAD-078](../Teileliste.md#cad-078) GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | `return_pulley_gt2_z16_6mm` | 4 | teilweise geklärt | Kaufteile |
| [CAD-001](../Teileliste.md#cad-001) Y-Riemenklemme (CAD-Name TR10x 2 GT2 Adapter) | `TR10x2_GT2_belt_adapter` | 4 | Fertigung noch offen; Klemmt den Y-Riemen am Schlitten (Fusion-Kontakt mit y_belt), keine Spindelmutter. | 3D-Druck intern |
| [CAD-002](../Teileliste.md#cad-002) Y-Riemenklemme, Deckel | `TR10x2_GT2_belt_adapter_cover` | 4 | Fertigung noch offen | 3D-Druck intern |
| [CAD-015](../Teileliste.md#cad-015) Grundgestell: NEMA 14 auf 17 Adapter | `base_nema_14_to_17_adapter` | 4 | Fertigung noch offen | 3D-Druck intern |
| [CAD-021](../Teileliste.md#cad-021) Riemen Spanner GT2 Basis | `belt_tightener_GT2_base` | 4 | Fertigung noch offen | 3D-Druck intern |
| [CAD-022](../Teileliste.md#cad-022) Riemen Spanner GT2 Flügel | `belt_tightener_GT2_wing` | 4 | Fertigung noch offen | 3D-Druck intern |
| [CAD-107](../Teileliste.md#cad-107) Y-Achse Schlitten | `y_slide` | 2 | Fertigung noch offen | 3D-Druck intern |
| [CAD-108](../Teileliste.md#cad-108) Y-Achse Schlitten Abstand Stange | `y_slide_distance_rod` | 8 | Fertigung noch offen | Weitere Fertigung |
| [CAD-110](../Teileliste.md#cad-110) Y-Achse Schlitten gespiegelt | `y_slide_mirrored` | 2 | Fertigung noch offen | 3D-Druck intern |
| [CAD-111](../Teileliste.md#cad-111) Y-Achse Schlitten gespiegelt oben | `y_slide_mirrored_top` | 2 | Fertigung noch offen | 3D-Druck intern |
| [CAD-112](../Teileliste.md#cad-112) Y-Achse Schlitten oben | `y_slide_top` | 2 | Fertigung noch offen | 3D-Druck intern |

**Bei der Prüfung aus dem Modul genommen**

- Z-Antrieb auf dem Y-Schlitten (NEMA14, 9-mm-Zahnscheiben, Z-Riemen, HIWIN-Wagen samt M3×8, M3×20 mit Distanzrohr): Modul Z-Achse.
- Kamerahalter, Mikroskop, optischer Endschalter mit M3×12 und Muttern, Energiekette: Optik bzw. Elektrik.
- CAD-001/002 heißen TR10x2-Adapter, sind laut Fusion aber die Klemme des Y-Riemens; Bezeichnung in der Teileliste angepasst.

**Offene Fragen**

- Gleitbuchsen RJ4JP-01-10 werden mit Sicherungsringen in der Nut gehalten; Ringe sind nicht im CAD. Prüfen, ob die gedruckten Schlitten die Buchsen formschlüssig halten.

<a id="modul-04"></a>

## M04 Z-Achse

Z-Antrieb auf den 4 Y-Schlitten (NEMA14, 9-mm-Zahnscheiben, Z-Riemen, HIWIN-Wagen) und die 4 Z-Schlitten (HIWIN-Schiene mit Riemenhalter, Endschalter-Auslöser und Prüfspitzen-Halter). Ohne Prüfspitzen-Elektronik und Kabelhalter.

*Am 17.10.2026 angelegt und per Fusion-Kontaktanalyse geprüft (z_slide:1, z_slide_long:1 und die Y-Schlitten aus M03).*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-029](../Teileliste.md#cad-029) DIN 562 M3 Vierkantmutter | `din_562_m3_square_nut` | 4 | bestellfähig; Motorbefestigung. | Kaufteile |
| [CAD-029](../Teileliste.md#cad-029) DIN 562 M3 Vierkantmutter | `din_562_m3_square_nut` | 4 | bestellfähig | Kaufteile |
| [CAD-030](../Teileliste.md#cad-030) DIN 562 M4 Vierkantmutter | `din_562_m4_square_nut` | 4 von 12 | bestellfähig; 4 von 12 halten den Endschalter-Auslöser. | Kaufteile |
| [CAD-035](../Teileliste.md#cad-035) DIN 912 M3×10 | `din_912_m3x10` | 16 | bestellfähig; Motorbefestigung am Y-Schlitten. | Kaufteile |
| [CAD-035](../Teileliste.md#cad-035) DIN 912 M3×10 | `din_912_m3x10` | 4 | bestellfähig | Kaufteile |
| [CAD-040](../Teileliste.md#cad-040) DIN 912 M3×20 | `din_912_m3x20` | 4 | bestellfähig; Achse der Z-Umlenkscheibe. | Kaufteile |
| [CAD-042](../Teileliste.md#cad-042) DIN 912 M3×8 | `din_912_m3x8` | 16 | bestellfähig; HIWIN-Wagen am Y-Schlitten. | Kaufteile |
| [CAD-042](../Teileliste.md#cad-042) DIN 912 M3×8 | `din_912_m3x8` | 4 | bestellfähig | Kaufteile |
| [CAD-053](../Teileliste.md#cad-053) HIWIN MGNR12R150HM, Z-Schiene 150 mm | `hiwin_rail_MGNR12R150HM` | 4 | bestellfähig | Kaufteile |
| [CAD-054](../Teileliste.md#cad-054) HIWIN MGN12CZ0HM Z-Führungswagen | `hiwin_slide_MGN12CZ0H` | 4 | bestellfähig | Kaufteile |
| [CAD-056](../Teileliste.md#cad-056) Sechskantmutter DIN 934 M3 A2 | `iso_8673_nut_m3` | 4 von 24 | bestellfähig; 4 von 24 an der Achse der Umlenkscheibe. | Kaufteile |
| [CAD-113](../Teileliste.md#cad-113) GT2-Riemen Z, 9 mm breit | `z_drive_belt` | 4 | bestellfähig | Kaufteile |
| [CAD-063](../Teileliste.md#cad-063) Nanotec ST3518M1004-A NEMA14 Z-Motor | `nanotec_nema_14_ST3518M1004-A` | 4 von 8 | teilweise geklärt; 4 von 8: je Y-Schlitten zwei CAD-Varianten derselben Einbaulage. | Kaufteile |
| [CAD-076](../Teileliste.md#cad-076) GT2-Zahnscheibe Z16 / 9 mm / Bohrung 5 mm | `pulley_gt2_9mm` | 8 | teilweise geklärt | Kaufteile |
| [CAD-109](../Teileliste.md#cad-109) Y-Achse Schlitten Abstand Rohr 2 mm | `y_slide_distance_tube_2mm` | 4 | Fertigung noch offen | Weitere Fertigung |
| [CAD-114](../Teileliste.md#cad-114) Z-Achse Antrieb Riemen Halter v 3 | `z_drive_belt_holder_v3` | 4 | Fertigung noch offen | 3D-Druck intern |
| [CAD-116](../Teileliste.md#cad-116) Z-Achse Prüfspitze Platine Halter | `z_probe_tip_pcb_holder` | 2 | Fertigung noch offen | 3D-Druck intern |
| [CAD-117](../Teileliste.md#cad-117) Z-Achse Prüfspitze Platine Halter lang | `z_probe_tip_pcb_holder_long` | 2 | Fertigung noch offen | 3D-Druck intern |
| [CAD-119](../Teileliste.md#cad-119) Z-Achse Schlitten Endschalter Auslöser | `z_slide_end_stop_trigger.psm` | 2 | Fertigung noch offen | Blech intern |
| [CAD-120](../Teileliste.md#cad-120) Z-Achse Schlitten Endschalter Auslöser gespiegelt | `z_slide_end_stop_trigger_mirrored.psm` | 2 | Fertigung noch offen | Blech intern |

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Zylinderschraube DIN 912 M3×8 A2 | 4 | CAD-042 | Am langen Z-Schlitten ist der Prüfspitzen-Halter im CAD nicht mit der Schiene verschraubt; am kurzen sind es 2 Schrauben. Annahme 2 je langem Schlitten, an der Geometrie bestätigen. |

**Bei der Prüfung aus dem Modul genommen**

- Prüfspitzen (Platine, Federkontakt, Hülse, MMCX-Stecker): Modul Prüfspitzen/Elektrik.
- Kabelhalter am langen Z-Schlitten: Elektrik.

**Offene Fragen**

- Die HIWIN-Schiene hat 6 Bohrungen, genutzt werden 2–3. Prüfen, ob weitere Schrauben vorgesehen sind.
- Z-Zahnscheibe CAD-076: exaktes Teil nicht lieferbar; Kandidat mit anderer Bauform braucht angepasste Halter.

<a id="modul-05"></a>

## M05 Schublade und Platinenhalter

Ausziehbare Schublade mit Teleskopschienen, Seitenprofilen, Bodenplatte und Griff sowie der verstellbare Platinenhalter für das Prüfobjekt.

*Am 17.10.2026 angelegt und per Fusion-Kontaktanalyse geprüft.*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-028](../Teileliste.md#cad-028) DIN 466 Rändelmutter hoch M4 | `din_466_knurled_nut_high_m4` | 8 | bestellfähig | Kaufteile |
| [CAD-033](../Teileliste.md#cad-033) DIN 7991 M6×14 | `din_7991_m6x14` | 6 | bestellfähig; Bodenplatte an den Profilen. | Kaufteile |
| [CAD-043](../Teileliste.md#cad-043) DIN 912 M4×10 | `din_912_m4x10` | 1 | bestellfähig | Kaufteile |
| [CAD-048](../Teileliste.md#cad-048) DIN 933 M4×20 | `din_933_m4x20` | 8 | bestellfähig | Kaufteile |
| [CAD-081](../Teileliste.md#cad-081) Anschraubwinkel 30 / Nut 6 | `screw_on_bracket_30_6` | 8 von 26 | bestellfähig; 8 von 26 verbinden die Schubladenprofile. | Kaufteile |
| [CAD-084](../Teileliste.md#cad-084) Teleskopschiene 350 mm, Vollauszug | `telescopic_bar_tsaa514613-350` | 2 | bestellfähig | Kaufteile |
| [CAD-051](../Teileliste.md#cad-051) Schubladengriff, Lochabstand 100 mm | `handle_l100_dold` | 1 | teilweise geklärt | Kaufteile |
| [CAD-011](../Teileliste.md#cad-011) Grundgestell: Schublade lang Seite | `base_drawer_long_side` | 2 | Fertigung noch offen | Weitere Fertigung |
| [CAD-067](../Teileliste.md#cad-067) Platine Halter Gleiter | `pcb_holder_glider` | 4 | Fertigung noch offen | 3D-Druck intern |
| [CAD-068](../Teileliste.md#cad-068) Platine Halter Führung Halter rund d 10 | `pcb_holder_guiding_holder_round_d10` | 4 | Fertigung noch offen | 3D-Druck intern |
| [CAD-069](../Teileliste.md#cad-069) Platine Halter Führung rund | `pcb_holder_guiding_round` | 2 | Fertigung noch offen | Weitere Fertigung |
| [CAD-070](../Teileliste.md#cad-070) Platine Halter rechteckig Stange | `pcb_holder_rect_rod` | 2 | Fertigung noch offen | Weitere Fertigung |
| [CAD-071](../Teileliste.md#cad-071) Platine Halter Stange kurz rund d 10 | `pcb_holder_rod_short_round_d10` | 2 | Fertigung noch offen | 3D-Druck intern |
| [CAD-072](../Teileliste.md#cad-072) Platine Halter Stange kurz rund d 10 gespiegelt | `pcb_holder_rod_short_round_d10_mirrored` | 2 | Fertigung noch offen | 3D-Druck intern |
| [CAD-010](../Teileliste.md#cad-010) Schubladen-Dummyplatte | `base_drawer_dummy_plate` | 1 | nicht identifiziert; Trägt den kompletten Platinenhalter (Fusion-Kontakt) und ist damit die reale Schubladen-Bodenplatte, kein reiner Platzhalter. | Ungeklärte Teile |

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Befestigung Teleskopschienen (Schrauben + Nutensteine I-Typ Nut 6) | offen | CAD-084, SYS-029 | Beide Schienen berühren Rahmen- und Schubladenprofile, im CAD gibt es aber keine Schrauben. Lochbild der HS-4613-350 und Schraubengröße festlegen. |
| Befestigung Griff (2 Schrauben, Gewinde laut Griffvariante) | 2 | CAD-051 | Griff sitzt am Schubladenprofil, im CAD ohne Schrauben. |
| Befestigung der Wellenhalter des Platinenhalters | offen | CAD-068 | 4 Halter sitzen auf Bodenplatte/Profil, nur einer hat eine M4×10. Je Halter mindestens 1–2 Schrauben ergänzen. |

**Bei der Prüfung aus dem Modul genommen**

- pcb_dummy: Prüfobjekt im CAD, kein Maschinenteil.

**Offene Fragen**

- CAD-010 Bodenplatte: Material und Dicke (CAD 12 mm) festlegen; Status von 'nicht identifiziert' auf Fertigungsteil ändern?
- Wo greifen die M4-Schrauben DIN 933 des Platinenhalters: Gewinde in der Bodenplatte oder Mutter darunter?
