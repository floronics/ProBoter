# Montagemodule

Schrittweiser Aufbau in logisch zusammengehörigen Modulen. Definition in [module.json](module.json), Teile mit Mengen in [montage.csv](montage.csv). Mengen sind CAD-Mengen im jeweiligen Fusion-Einbau; Status aus der [Teileliste](../Teileliste.md). In Fusion einblenden: `tools/fusion_show_module.py`.

| Modul | Positionen | Stück | bestellfähig | teilweise geklärt | Fertigung noch offen | Fertigung spezifiziert | nicht identifiziert | nicht benötigt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [M01 Grundgerüst](#modul-01) | 12 | 62 | 9 | 0 | 3 | 0 | 0 | 0 |
| [M02 X-Achse](#modul-02) | 33 | 434 | 22 | 0 | 2 | 9 | 0 | 0 |
| [M03 Y-Achse](#modul-03) | 27 | 168 | 17 | 0 | 0 | 10 | 0 | 0 |
| [M04 Z-Achse](#modul-04) | 20 | 100 | 14 | 0 | 0 | 6 | 0 | 0 |
| [M05 Schublade und Platinenhalter](#modul-05) | 21 | 96 | 15 | 0 | 1 | 4 | 1 | 0 |
| [M06 Kabelführung](#modul-06) | 21 | 310 | 10 | 3 | 0 | 8 | 0 | 0 |
| [M07 Elektrik und Sensorik](#modul-07) | 24 | 150 | 11 | 1 | 0 | 12 | 0 | 0 |
| [M08 Optik](#modul-08) | 8 | 22 | 4 | 0 | 0 | 4 | 0 | 0 |
| [M09 Prüfspitzen](#modul-09) | 8 | 49 | 2 | 4 | 1 | 1 | 0 | 0 |
| [M10 Verkleidung](#modul-10) | 4 | 40 | 4 | 0 | 0 | 0 | 0 | 0 |
| [M12 Beleuchtung](#modul-12) | 3 | 3.9 | 2 | 1 | 0 | 0 | 0 | 0 |
| [M13 Kalibrierung](#modul-13) | 6 | 21 | 0 | 0 | 0 | 6 | 0 | 0 |

<a id="modul-01"></a>

## M01 Grundgerüst

Tragender Rahmen ohne Elektrik, ohne Halter für elektrische Teile, ohne Achsen, Schublade und Verkleidung.

*Abgrenzung mit Luis am 17.10.2026 abgestimmt. Vollständigkeit am 17.10.2026 per Fusion-Kontaktanalyse geprüft (bom/evidence/fusion-measurements.json, tools/fusion_measurements.py).*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-012](../Teileliste.md#cad-012) Grundgestell: Rahmen lang Seite | `base_frame_long_side` | 3 | bestellfähig | Weitere Fertigung |
| [CAD-013](../Teileliste.md#cad-013) Grundgestell: Rahmen kurz | `base_frame_short` | 8 | bestellfähig | Weitere Fertigung |
| [CAD-014](../Teileliste.md#cad-014) Grundgestell: Rahmen Seite | `base_frame_side` | 2 | bestellfähig | Weitere Fertigung |
| [CAD-020](../Teileliste.md#cad-020) Grundgestell: vertikal | `base_vertical` | 4 | bestellfähig | Weitere Fertigung |
| [CAD-034](../Teileliste.md#cad-034) DIN 7991 M6×20 | `din_7991_m6x20` | 8 von 22 | bestellfähig; 8 von 22 verbinden die Motorplatten mit den 60×30-Profilen; 8 halten die Adapterplatten (X-Antrieb), 6 die Kettenhalter. | Kaufteile |
| [CAD-052](../Teileliste.md#cad-052) Gelenkfuß M6×20 / Teller Ø40 mm | `hinged_M6_40_dold` | 4 | bestellfähig | Kaufteile |
| [CAD-081](../Teileliste.md#cad-081) Anschraubwinkel 30 / Nut 6 | `screw_on_bracket_30_6` | 18 von 26 | bestellfähig; 18 von 26 verbinden Rahmenprofile; 8 gehören zur Schublade. | Kaufteile |
| [SYS-042](../Teileliste.md#sys-042) Nutenstein I-Typ Nut 6, M4, Rückwand | nicht im CAD | 6 | bestellfähig | Kaufteile |
| [SYS-043](../Teileliste.md#sys-043) Zylinderschraube DIN 912 M4×10 A2, Rückwand | nicht im CAD | 6 | bestellfähig | Kaufteile |
| [CAD-003](../Teileliste.md#cad-003) Grundgestell: Rückseite Platte | `base_back_plate` | 1 | Fertigung noch offen | Blech intern |
| [CAD-096](../Teileliste.md#cad-096) X-Achse Motor Platte | `x_motor_plate` | 1 | Fertigung noch offen | Blech intern |
| [CAD-097](../Teileliste.md#cad-097) X-Achse Motor Platte 2 | `x_motor_plate_2` | 1 | Fertigung noch offen | Blech intern |

**Werkstattfertigung**

- CAD-003 Rückwand, CAD-096 und CAD-097 Motorplatten: Fertigung in der eigenen Werkstatt aus Blech oder Aluminium (Entscheidung 17.10.2026).

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Befestigungssätze der Winkel | 18 | CAD-081 | Bereits enthalten: CAD-081 wird als Satz 62385-BS mit 2 Schrauben M6×12 und 2 Nutensteinen bestellt. |
| Gewinde M6 in Profil-Kernbohrung Ø5 | 4 | CAD-020 | Gelenkfüße sitzen in den unteren Enden der 4 Vertikalprofile; Kernbohrung Ø5 ist das M6-Kernloch. Bearbeitung, kein Kaufteil. |

**Bei der Prüfung aus dem Modul genommen**

- DIN 7991 M6×14 (6 Stück): befestigen die Schubladen-Dummyplatte, gehören zur Schublade.
- Adapterplatten CAD-016 bis CAD-019: tragen die X-Riemenantriebe (M3/M4-Schrauben aus x_belt_drive) und gehören zur X-Achse. Fertigungsverfahren weiter mit PRÜFEN-Vermerk.
- Muttern M8×1 an den Motorplatten (8 Stück): halten induktive Sensoren, gehören zur Elektrik.

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
| [CAD-077](../Teileliste.md#cad-077) GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | `pulley_gt2_z16_6mm` | 8 | bestellfähig | Kaufteile |
| [CAD-078](../Teileliste.md#cad-078) GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | `return_pulley_gt2_z16_6mm` | 16 | bestellfähig | Kaufteile |
| [CAD-079](../Teileliste.md#cad-079) SHF10 Flanschhalter fürØ10 mm Welle | `rod_holder_flange_d10_dold` | 16 | bestellfähig | Kaufteile |
| [CAD-087](../Teileliste.md#cad-087) GT2-Riemen X, 6 mm breit | `x_belt` | 8 | bestellfähig | Kaufteile |
| [CAD-095](../Teileliste.md#cad-095) CPC MR12M Führungsschiene 600 mm | `x_guiding_cpc_MR12M` | 2 | bestellfähig | Kaufteile |
| [CAD-098](../Teileliste.md#cad-098) X-Achse rund Schiene | `x_round_rail` | 8 | bestellfähig | Weitere Fertigung |
| [CAD-103](../Teileliste.md#cad-103) X-Achse Schlitten Versteifung Träger | `x_slide_stiffener_beam` | 4 | bestellfähig | Weitere Fertigung |
| [CAD-099](../Teileliste.md#cad-099) X-Achse Seite Platte | `x_side_plate` | 4 | Fertigung noch offen | Blech intern |
| [CAD-100](../Teileliste.md#cad-100) X-Achse Seite Platte beweglich | `x_side_plate_moving` | 4 | Fertigung noch offen | Blech intern |
| [CAD-015](../Teileliste.md#cad-015) Grundgestell: NEMA 14 auf 17 Adapter | `base_nema_14_to_17_adapter` | 8 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-016](../Teileliste.md#cad-016) Grundgestell: Platte Adapter 1 | `base_plate_adapter_1` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-017](../Teileliste.md#cad-017) Grundgestell: Platte Adapter 2 | `base_plate_adapter_2` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-018](../Teileliste.md#cad-018) Grundgestell: Platte Adapter links | `base_plate_adapter_left` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-019](../Teileliste.md#cad-019) Grundgestell: Platte Adapter rechts | `base_plate_adapter_right` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-021](../Teileliste.md#cad-021) Riemen Spanner GT2 Basis | `belt_tightener_GT2_base` | 16 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-022](../Teileliste.md#cad-022) Riemen Spanner GT2 Flügel | `belt_tightener_GT2_wing` | 16 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-088](../Teileliste.md#cad-088) X-Achse Riemen Halter | `x_belt_holder` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-089](../Teileliste.md#cad-089) X-Achse Riemen Halter 1 | `x_belt_holder_1` | 12 | Fertigung spezifiziert | 3D-Druck intern |

**Werkstattfertigung**

- CAD-016 bis CAD-019 Adapterplatten und CAD-099/100 Seitenplatten der X-Wagen: eigene Werkstatt (Entscheidung 17.10.2026).
- 3D-Druckteile (NEMA-Adapter, Spanner, Riemenhalter): PETG intern, Geometrie aus CAD.

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Gewinde M3 in den Motorplatten (Bohrungen Ø2,46) | 32 | CAD-096/097 | M3×10 der Riemenspanner haben keine Mutter; die Platten haben je 16 Kernlöcher Ø2,46 für M3. Bearbeitung, kein Kaufteil. |
| Gewinde M3 in den Adapterplatten | 32 | CAD-016–019 | Für die M3×18 der NEMA-Adapter; Werkstattbearbeitung (Entscheidung 17.10.2026). |
| Gewinde M5 in den Seitenplatten der X-Wagen | 36 | CAD-099/100 | Für M5×10/M5×14 an Flanschhaltern und Versteifung; Werkstattbearbeitung (Entscheidung 17.10.2026). |

**Bei der Prüfung aus dem Modul genommen**

- Induktive Sensoren, M8×1-Muttern, Endschalterhalter und -adapter, Kabelhalter: Elektrik.
- Energieketten und Kettenadapter am Wagen: eigenes Modul Kabelführung.
- Y-Riemenantrieb auf dem Wagen (y_belt_drive) und die 4 M3×10 direkt am Wagen: Modul Y-Achse.

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
| [CAD-077](../Teileliste.md#cad-077) GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | `pulley_gt2_z16_6mm` | 4 | bestellfähig | Kaufteile |
| [CAD-078](../Teileliste.md#cad-078) GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | `return_pulley_gt2_z16_6mm` | 4 | bestellfähig | Kaufteile |
| [CAD-080](../Teileliste.md#cad-080) GleitbuchseØ10 innen / Ø19 außen / Länge 29 mm | `rod_slide_d10_l19` | 16 | bestellfähig | Kaufteile |
| [CAD-104](../Teileliste.md#cad-104) GT2-Riemen Y, 6 mm breit | `y_belt` | 4 | bestellfähig | Kaufteile |
| [CAD-001](../Teileliste.md#cad-001) Y-Riemenklemme (CAD-Name TR10x 2 GT2 Adapter) | `TR10x2_GT2_belt_adapter` | 4 | Fertigung spezifiziert; Klemmt den Y-Riemen am Schlitten (Fusion-Kontakt mit y_belt), keine Spindelmutter. | 3D-Druck intern |
| [CAD-002](../Teileliste.md#cad-002) Y-Riemenklemme, Deckel | `TR10x2_GT2_belt_adapter_cover` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-015](../Teileliste.md#cad-015) Grundgestell: NEMA 14 auf 17 Adapter | `base_nema_14_to_17_adapter` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-021](../Teileliste.md#cad-021) Riemen Spanner GT2 Basis | `belt_tightener_GT2_base` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-022](../Teileliste.md#cad-022) Riemen Spanner GT2 Flügel | `belt_tightener_GT2_wing` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-107](../Teileliste.md#cad-107) Y-Achse Schlitten | `y_slide` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-108](../Teileliste.md#cad-108) Y-Achse Schlitten Abstand Stange | `y_slide_distance_rod` | 8 | Fertigung spezifiziert | Weitere Fertigung |
| [CAD-110](../Teileliste.md#cad-110) Y-Achse Schlitten gespiegelt | `y_slide_mirrored` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-111](../Teileliste.md#cad-111) Y-Achse Schlitten gespiegelt oben | `y_slide_mirrored_top` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-112](../Teileliste.md#cad-112) Y-Achse Schlitten oben | `y_slide_top` | 2 | Fertigung spezifiziert | 3D-Druck intern |

**Werkstattfertigung**

- CAD-108 Abstandsstangen: Ø4-h6-Silberstahl ablängen (70 mm) und anfasen (Entscheidung 17.10.2026).

**Bei der Prüfung aus dem Modul genommen**

- Z-Antrieb auf dem Y-Schlitten (NEMA14, 9-mm-Zahnscheiben, Z-Riemen, HIWIN-Wagen samt M3×8, M3×20 mit Distanzrohr): Modul Z-Achse.
- Kamerahalter, Mikroskop, optischer Endschalter mit M3×12 und Muttern, Energiekette: Optik bzw. Elektrik.
- CAD-001/002 heißen TR10x2-Adapter, sind laut Fusion aber die Klemme des Y-Riemens; Bezeichnung in der Teileliste angepasst.
- Sicherungsringe der Gleitbuchsen: nicht nötig. Fusion-Messung zeigt, dass Y-Schlitten und Deckel die Ø19-Buchsen mit den M4×30 klemmen.

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
| [CAD-063](../Teileliste.md#cad-063) NEMA14 Z-Motor, ERSATZ: STEPPERONLINE 14HS13-0804S statt Nanotec ST3518M1004-A | `nanotec_nema_14_ST3518M1004-A` | 4 von 8 | bestellfähig; 4 von 8: je Y-Schlitten zwei CAD-Varianten derselben Einbaulage. | Kaufteile |
| [CAD-076](../Teileliste.md#cad-076) GT2-Zahnscheibe Z16 / 9 mm / Bohrung 5 mm, ANPASSUNG | `pulley_gt2_9mm` | 8 | bestellfähig | Kaufteile |
| [CAD-113](../Teileliste.md#cad-113) GT2-Riemen Z, 9 mm breit | `z_drive_belt` | 4 | bestellfähig | Kaufteile |
| [CAD-109](../Teileliste.md#cad-109) Y-Achse Schlitten Abstand Rohr 2 mm | `y_slide_distance_tube_2mm` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-114](../Teileliste.md#cad-114) Z-Achse Antrieb Riemen Halter v 3 | `z_drive_belt_holder_v3` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-116](../Teileliste.md#cad-116) Z-Achse Prüfspitze Platine Halter | `z_probe_tip_pcb_holder` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-117](../Teileliste.md#cad-117) Z-Achse Prüfspitze Platine Halter lang | `z_probe_tip_pcb_holder_long` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-119](../Teileliste.md#cad-119) Z-Achse Schlitten Endschalter Auslöser | `z_slide_end_stop_trigger.psm` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-120](../Teileliste.md#cad-120) Z-Achse Schlitten Endschalter Auslöser gespiegelt | `z_slide_end_stop_trigger_mirrored.psm` | 2 | Fertigung spezifiziert | 3D-Druck intern |

**Werkstattfertigung**

- ERSATZ: NEMA14 Z-Motor STEPPERONLINE 14HS13-0804S statt Original Nanotec ST3518M1004-A (Entscheidung Luis 17.10.2026). Motorstrom auf 0,8 A begrenzen.
- ANPASSUNG: Z-Zahnscheibe RBS12867 (Ø13×19,5) statt Original Ø18×11; Y-Schlitten-Druckteil und Umlenkachse anpassen.
- Endschalter-Auslöser CAD-119/120 als PETG-Druckteil statt Blech.
- Distanzhülsen CAD-109 (Ø3/Ø4,8 × 3 mm) als PETG-Druckteil.

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Zylinderschraube DIN 912 M3×8 A2 | 4 | CAD-042 | Am langen Z-Schlitten ist der Prüfspitzen-Halter im CAD nicht mit der Schiene verschraubt; am kurzen sind es 2 Schrauben. Annahme 2 je langem Schlitten, an der Geometrie bestätigen. |

**Bei der Prüfung aus dem Modul genommen**

- Prüfspitzen (Platine, Federkontakt, Hülse, MMCX-Stecker): Modul Prüfspitzen/Elektrik.
- Kabelhalter am langen Z-Schlitten: Elektrik.

**Offene Fragen**

- Gelochte HIWIN-Schiene: 6 Bohrungen, genutzt 2–3. Prüfen, ob weitere Schrauben vorgesehen sind.

<a id="modul-05"></a>

## M05 Schublade und Platinenhalter

Ausziehbare Schublade mit Teleskopschienen, Seitenprofilen, Bodenplatte und Griff sowie der verstellbare Platinenhalter für das Prüfobjekt.

*Am 17.10.2026 angelegt und per Fusion-Kontaktanalyse geprüft.*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-011](../Teileliste.md#cad-011) Grundgestell: Schublade lang Seite | `base_drawer_long_side` | 2 | bestellfähig | Weitere Fertigung |
| [CAD-028](../Teileliste.md#cad-028) DIN 466 Rändelmutter hoch M4 | `din_466_knurled_nut_high_m4` | 8 | bestellfähig | Kaufteile |
| [CAD-033](../Teileliste.md#cad-033) DIN 7991 M6×14 | `din_7991_m6x14` | 6 | bestellfähig; Bodenplatte an den Profilen. | Kaufteile |
| [CAD-043](../Teileliste.md#cad-043) DIN 912 M4×10 | `din_912_m4x10` | 1 | bestellfähig | Kaufteile |
| [CAD-048](../Teileliste.md#cad-048) DIN 933 M4×20 | `din_933_m4x20` | 8 | bestellfähig | Kaufteile |
| [CAD-051](../Teileliste.md#cad-051) Schubladengriff DOLD A-75873, Lochabstand 100 mm | `handle_l100_dold` | 1 | bestellfähig | Kaufteile |
| [CAD-069](../Teileliste.md#cad-069) Platine Halter Führung rund | `pcb_holder_guiding_round` | 2 | bestellfähig | Weitere Fertigung |
| [CAD-081](../Teileliste.md#cad-081) Anschraubwinkel 30 / Nut 6 | `screw_on_bracket_30_6` | 8 von 26 | bestellfähig; 8 von 26 verbinden die Schubladenprofile. | Kaufteile |
| [CAD-084](../Teileliste.md#cad-084) Teleskopschiene 350 mm, Vollauszug | `telescopic_bar_tsaa514613-350` | 2 | bestellfähig | Kaufteile |
| [SYS-044](../Teileliste.md#sys-044) Nutenstein I-Typ Nut 6, M5, Griff | nicht im CAD | 2 | bestellfähig | Kaufteile |
| [SYS-045](../Teileliste.md#sys-045) Zylinderschraube DIN 912 M5×35 A2, Griff | nicht im CAD | 2 | bestellfähig | Kaufteile |
| [SYS-046](../Teileliste.md#sys-046) Zylinderschraube DIN 912 M4×10 A2, Wellenhalter | nicht im CAD | 7 | bestellfähig | Kaufteile |
| [SYS-047](../Teileliste.md#sys-047) Nutenstein I-Typ Nut 6, M4, Wellenhalter | nicht im CAD | 8 | bestellfähig | Kaufteile |
| [SYS-048](../Teileliste.md#sys-048) Linsenkopfschraube ISO 7380-1 M4×8 A2, Teleskopschienen | nicht im CAD | 12 | bestellfähig | Kaufteile |
| [SYS-049](../Teileliste.md#sys-049) Nutenstein I-Typ Nut 6, M4, Teleskopschienen | nicht im CAD | 12 | bestellfähig | Kaufteile |
| [CAD-070](../Teileliste.md#cad-070) Platine Halter rechteckig Stange | `pcb_holder_rect_rod` | 2 | Fertigung noch offen | Weitere Fertigung |
| [CAD-067](../Teileliste.md#cad-067) Platine Halter Gleiter | `pcb_holder_glider` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-068](../Teileliste.md#cad-068) Platine Halter Führung Halter rund d 10 | `pcb_holder_guiding_holder_round_d10` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-071](../Teileliste.md#cad-071) Platine Halter Stange kurz rund d 10 | `pcb_holder_rod_short_round_d10` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-072](../Teileliste.md#cad-072) Platine Halter Stange kurz rund d 10 gespiegelt | `pcb_holder_rod_short_round_d10_mirrored` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-010](../Teileliste.md#cad-010) Schubladen-Dummyplatte | `base_drawer_dummy_plate` | 1 | nicht identifiziert; Trägt den kompletten Platinenhalter (Fusion-Kontakt) und ist damit die reale Schubladen-Bodenplatte, kein reiner Platzhalter. | Ungeklärte Teile |

**Bei der Prüfung aus dem Modul genommen**

- pcb_dummy: Prüfobjekt im CAD, kein Maschinenteil.

**Offene Fragen**

- CAD-010 Bodenplatte: Material und Dicke (CAD 12 mm) – von Luis bewusst offen gelassen.
- SYS-045 und SYS-048: Schraubenartikel noch verifizieren; Teleskop-Befestigung ist eine Annahme.

<a id="modul-06"></a>

## M06 Kabelführung

Energieketten mit Haltern und Adaptern sowie Kabelhalter und Kabelabdeckungen. Mechanische Führung der Leitungen, ohne die Leitungen selbst (Elektrik).

*Am 17.10.2026 aus den noch nicht zugeordneten CAD-Teilen gebildet; Kontaktanalyse aus M01–M04 übernommen.*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-034](../Teileliste.md#cad-034) DIN 7991 M6×20 | `din_7991_m6x20` | 6 von 22 | bestellfähig; 6 von 22 halten die Kettenhalter an den Motorplatten. | Kaufteile |
| [CAD-049](../Teileliste.md#cad-049) igus E2i.10.10.028.0, 16 kurze Abschnitte | `drag_chain_0_24m_E2i_10_10_028_0_4` | 16 | bestellfähig | Kaufteile |
| [CAD-050](../Teileliste.md#cad-050) igus E2i.10.20.028.0, 8 lange Abschnitte | `drag_chain_0_28m_E2i_10_20_028_0_igus` | 8 | bestellfähig | Kaufteile |
| [SYS-050](../Teileliste.md#sys-050) Zylinderschraube DIN 912 M3×8 A2, Kabelhalter M3 | nicht im CAD | 4 | bestellfähig | Kaufteile |
| [SYS-051](../Teileliste.md#sys-051) Zylinderschraube DIN 912 M3×10 A2, igus-Kettenanschlüsse | nicht im CAD | 106 | bestellfähig | Kaufteile |
| [SYS-052](../Teileliste.md#sys-052) Zylinderschraube DIN 912 M3×12 A2, Z-Kabelhalter | nicht im CAD | 6 | bestellfähig | Kaufteile |
| [SYS-053](../Teileliste.md#sys-053) Sechskantmutter DIN 934 M3 A2, Kabelführung | nicht im CAD | 111 | bestellfähig | Kaufteile |
| [SYS-054](../Teileliste.md#sys-054) Linsenkopfschraube ISO 7380-1 M4×8 A2, Kabelführung | nicht im CAD | 11 | bestellfähig | Kaufteile |
| [SYS-055](../Teileliste.md#sys-055) Nutenstein I-Typ Nut 6, M4, Kabelhalter | nicht im CAD | 3 | bestellfähig | Kaufteile |
| [SYS-056](../Teileliste.md#sys-056) Zylinderschraube DIN 912 M5×10 A2, Kabelhalter M5 | nicht im CAD | 6 | bestellfähig | Kaufteile |
| [CAD-009](../Teileliste.md#cad-009) Grundgestell: Schlepp Energiekette Halter | `base_drag_chain_holder` | 4 | teilweise geklärt | Weitere Fertigung |
| [SYS-073](../Teileliste.md#sys-073) Energiekette Schublade igus E2C.10.10.028.0, 0,5 m | nicht im CAD | 2 | teilweise geklärt | Kaufteile |
| [SYS-074](../Teileliste.md#sys-074) Anschlusssatz igus E2.100.10.56PZ.A1, Schubladenkette | nicht im CAD | 2 | teilweise geklärt | Kaufteile |
| [CAD-004](../Teileliste.md#cad-004) Grundgestell: Kabel Halter M3 flach | `base_cable_holder_m3_flat` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-005](../Teileliste.md#cad-005) Grundgestell: Kabel Halter M4 | `base_cable_holder_m4` | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-006](../Teileliste.md#cad-006) Grundgestell: Kabel Halter M5 flach | `base_cable_holder_m5_flat` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-024](../Teileliste.md#cad-024) Kabel Abdeckung | `cable_cover` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-090](../Teileliste.md#cad-090) X-Achse Schlepp Energiekette Adapter | `x_drag_chain_adapter` | 8 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-118](../Teileliste.md#cad-118) Z-Achse Schlitten Kabel Halter | `z_slide_cable_holder` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [SYS-064](../Teileliste.md#sys-064) Schleppkettenhalter Schublade, gestellseitig, Druck | nicht im CAD | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [SYS-065](../Teileliste.md#sys-065) Schleppkettenhalter Schublade, schubladenseitig, Druck | nicht im CAD | 1 | Fertigung spezifiziert | 3D-Druck intern |

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Energieketten-Anschlusselemente | 24 | SYS-027, SYS-028 | Im CAD als Körper der Ketten enthalten, als Sätze separat bestellt (bereits in der Teileliste). |

**Offene Fragen**

- Kettenhalter CAD-009: Kandidat DOLD 80x16S (60886-Z) ist 13 % leichter als das CAD-Profil und hat laut Produktseite einen M8-Kern statt Ø5. Vor Bestellung an der DOLD-Zeichnung prüfen.
- Schrauben der igus-Anschlüsse, Z-Kabelhalter und Kettenadapter sind ANNAHMEN; beim Aufbau prüfen.

<a id="modul-07"></a>

## M07 Elektrik und Sensorik

Netzteil, Steuerplatinen, Bedientaster, Multiplexer-Halter, induktive Sensoren und optische Endschalter mit ihren Haltern und Schrauben; dazu die Systemteile ohne CAD-Körper (Treiber, Kabel, Verteilung, Schutzleiter).

*Am 17.10.2026 aus den verbleibenden CAD-Teilen gebildet; Schrauben-Zuordnung aus der Kontaktanalyse von M02–M04.*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-023](../Teileliste.md#cad-023) Steuerplatine, ERSATZ: BIGTREETECH SKR 1.4 Turbo statt SKR V1.3 | `bigtreetech_skr_v1_3` | 4 | bestellfähig | Kaufteile |
| [CAD-035](../Teileliste.md#cad-035) DIN 912 M3×10 | `din_912_m3x10` | 16 | bestellfähig; Endschalter-Adapter und Flanschhalter am X-Wagen. | Kaufteile |
| [CAD-036](../Teileliste.md#cad-036) DIN 912 M3×12 | `din_912_m3x12` | 8 | bestellfähig; Optische Endschalter. | Kaufteile |
| [CAD-055](../Teileliste.md#cad-055) Induktiver Näherungsschalter ELCO NI4-M08-ON6L-Q8 (AUSWAHL, Original unbekannt) | `inductive_proximity_sensor_m8` | 24 | bestellfähig | Kaufteile |
| [CAD-056](../Teileliste.md#cad-056) Sechskantmutter DIN 934 M3 A2 | `iso_8673_nut_m3` | 8 von 24 | bestellfähig; 8 von 24 an den optischen Endschaltern. | Kaufteile |
| [CAD-059](../Teileliste.md#cad-059) Mean Well MHS012 Montagewinkel | `mean_well_MHS-012_mounting_bracket` | 4 | bestellfähig | Kaufteile |
| [CAD-060](../Teileliste.md#cad-060) Mean Well RSP-200-24 Netzteil,24 V/8,4 A | `mean_well_RSP-200-24` | 1 | bestellfähig | Kaufteile |
| [CAD-065](../Teileliste.md#cad-065) Optischer Endschalter 11×35 mm | `optical_endstop` | 4 | bestellfähig | Kaufteile |
| [CAD-086](../Teileliste.md#cad-086) Netzschalter Ø19 ONPOW LAS1 A-ZG24, rastend | `vandalism_switch_d19` | 1 | bestellfähig | Kaufteile |
| [CAD-093](../Teileliste.md#cad-093) X-Achse Endschalter oben lang | `x_end_stop_top_long` | 4 | bestellfähig | Weitere Fertigung |
| [CAD-094](../Teileliste.md#cad-094) X-Achse Endschalter oben kurz | `x_end_stop_top_short` | 4 | bestellfähig | Weitere Fertigung |
| [CAD-058](../Teileliste.md#cad-058) ISO 8673 Mutter M8 | `iso_8673_nut_m8` | 48 | teilweise geklärt | Kaufteile |
| [CAD-074](../Teileliste.md#cad-074) Stromversorgung Schalter Halter | `power_switch_holder` | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-083](../Teileliste.md#cad-083) Signal-Multiplexer Halter | `signal_multiplexer_holder` | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-091](../Teileliste.md#cad-091) X-Achse Endschalter Halter Seite kurz | `x_end_stop_holder_side_short` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-092](../Teileliste.md#cad-092) X-Achse Endschalter Halter oben lang | `x_end_stop_holder_top_long` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-101](../Teileliste.md#cad-101) X-Achse Schlitten induktiv Endschalter Adapter | `x_slide_inductive_endstop_adapter` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-102](../Teileliste.md#cad-102) X-Achse Schlitten induktiv Endschalter Adapter gespiegelt | `x_slide_inductive_endstop_adapter_mirrored` | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [SYS-066](../Teileliste.md#sys-066) Netzbuchsenhalter Schublade, Druck | nicht im CAD | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [SYS-067](../Teileliste.md#sys-067) Gehäuse Zielplatinen-Versorgungsschalter, Druck | nicht im CAD | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [SYS-068](../Teileliste.md#sys-068) Deckel Zielplatinen-Versorgungsschalter, Druck | nicht im CAD | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [SYS-069](../Teileliste.md#sys-069) Gehäuse Kleinnetzteil, Druck | nicht im CAD | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [SYS-070](../Teileliste.md#sys-070) Deckel Kleinnetzteil, Druck | nicht im CAD | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [SYS-071](../Teileliste.md#sys-071) Raspberry-Pi-4-Halter, Druck | nicht im CAD | 1 | Fertigung spezifiziert | 3D-Druck intern |

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Systemteile Elektrik ohne CAD | siehe Teileliste | SYS-001, 009–021, 025, 038 | Treiber, LED-Anschluss, USB, Motor- und Sensorleitungen, Stecker, 24-V-Verteilung, Netzanschluss, Schutzleiter, UART, Kalibrierleitungen. |
| Befestigung Netzteil-Winkel und SKR-Platinen | offen | SYS-032 | Im CAD keine Schrauben/Abstandshalter; 4 freie Ø4,5-Bohrungen der Rückwand passen vermutlich zum Netzteil. |

**Bei der Prüfung aus dem Modul genommen**

- signal_multiplexer_dummy: Platzhalter; die echte Platine ist SYS-003/023 und noch nicht entworfen.

**Offene Fragen**

- Induktive Sensoren CAD-055: Typ (NPN/PNP, Schaltabstand, Spannung) weiter nicht identifiziert.
- Bedientaster CAD-086: Funktion weiter nicht identifiziert.

<a id="modul-08"></a>

## M08 Optik

Bewegliches USB-Mikroskop mit Haltern an den Y-Schlitten und die Übersichtskamera mit Halter am Grundgestell.

*Am 17.10.2026 angelegt; Schrauben aus der Kontaktanalyse der Y-Schlitten.*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-037](../Teileliste.md#cad-037) DIN 912 M3×14 | `din_912_m3x14` | 4 | bestellfähig | Kaufteile |
| [CAD-041](../Teileliste.md#cad-041) DIN 912 M3×30 | `din_912_m3x30` | 4 von 8 | bestellfähig; 4 von 8 halten den Kamerahalter. | Kaufteile |
| [CAD-056](../Teileliste.md#cad-056) Sechskantmutter DIN 934 M3 A2 | `iso_8673_nut_m3` | 4 von 24 | bestellfähig; 4 von 24 am Kamerahalter. | Kaufteile |
| [CAD-085](../Teileliste.md#cad-085) Bewegliches USB-Mikroskop Toolcraft 2 MP (AUSWAHL, ANPASSUNG) | `usb_microscope` | 4 | bestellfähig; CAD zeigt 4, geplant ist 1 (3 optional). | Kaufteile |
| [CAD-025](../Teileliste.md#cad-025) Kamera Halter | `camera_holder` | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-026](../Teileliste.md#cad-026) Kamera Halter oben | `camera_holder_top` | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-105](../Teileliste.md#cad-105) Y-Achse Kamera Halter | `y_camera_holder` | 2 | Fertigung spezifiziert | 3D-Druck intern |
| [CAD-106](../Teileliste.md#cad-106) Y-Achse Kamera Halter kompakt | `y_camera_holder_compact` | 2 | Fertigung spezifiziert | 3D-Druck intern |

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Übersichtskamera und Beleuchtung | siehe Teileliste | SYS-002, SYS-007, SYS-008, SYS-033 | Kamera, LED-Streifen und LED-Profile ohne CAD-Körper. |
| Befestigung Kamerahalter am Grundgestell | offen | SYS-029 | Im CAD keine Schrauben für camera_holder. |

**Offene Fragen**

- Mikroskop- und Kameramodell des Originals unbekannt; Halter müssen zum gewählten Modell passen.

<a id="modul-09"></a>

## M09 Prüfspitzen

Die 4 Prüfspitzen an den Z-Schlitten: Platine, Federkontakt, Kontakthülse und MMCX-Messstecker.

*Am 17.10.2026 angelegt.*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-115](../Teileliste.md#cad-115) Federkontakt P75-B1 (Nadelspitze, wie CAD) | `z_pogo_pin` | 8 | bestellfähig | Kaufteile |
| [SYS-057](../Teileliste.md#sys-057) Prüfstifte P75-E2 Kegelspitze (Spitzenauswahl) | nicht im CAD | 10 | bestellfähig | Kaufteile |
| [CAD-061](../Teileliste.md#cad-061) MMCX-Stecker gerade mit RG316, offenes Ende | `mmcx_male_end` | 4 | teilweise geklärt | Kaufteile |
| [CAD-062](../Teileliste.md#cad-062) MMCX-Stecker gewinkelt mit RG316, offenes Ende | `mmcx_male_end_with_angle` | 4 | teilweise geklärt | Kaufteile |
| [CAD-073](../Teileliste.md#cad-073) Aufnahmehülse R75 mit Drahtende (CAD: P75-2_W) | `plug_sleeve_P75-2_W` | 8 | teilweise geklärt | Kaufteile |
| [SYS-058](../Teileliste.md#sys-058) Prüfstifte P75 Flachspitze zum Bestromen von Pads (Spitzenauswahl) | nicht im CAD | 10 | teilweise geklärt | Kaufteile |
| [CAD-075](../Teileliste.md#cad-075) Prüfspitzen-PCB, unbestückt | `probe_tip_pcb` | 4 | Fertigung noch offen | PCB extern |
| [SYS-072](../Teileliste.md#sys-072) Halter Höhennivellier-Taster (Hilfsmittel), Druck | nicht im CAD | 1 | Fertigung spezifiziert | 3D-Druck intern |

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Bestückung, Messkoax, Multiplexer | siehe Teileliste | SYS-003, SYS-022, SYS-023, SYS-024 | Ohne Schaltplan nicht spezifizierbar. |

**Offene Fragen**

- Prüfspitzen-Platine CAD-075: Anfrage bei SCHUTZWERK ist raus (Luis), Antwort offen.
- Aufnahmehülse R75 mit Drahtende: Bezugsquelle mit Preis fehlt.
- Flachspitze P75: Code und Bezugsquelle fehlen; Spitzenzeichnung beim Händler anfordern.
- MMCX-RG316: Kabellänge (1–1,5 m) und Gegenseite am Messgerät festlegen.

<a id="modul-10"></a>

## M10 Verkleidung

Abdeckungen oben und seitlich; laut Luis keine tragende Funktion.

*Am 17.10.2026 angelegt.*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [CAD-007](../Teileliste.md#cad-007) Grundgestell: Abdeckung lang Seite | `base_cover_long_side` | 2 | bestellfähig | Kaufteile |
| [CAD-008](../Teileliste.md#cad-008) Grundgestell: Abdeckung oben | `base_cover_top` | 2 | bestellfähig | Kaufteile |
| [SYS-059](../Teileliste.md#sys-059) Zylinderschraube DIN 912 M5×10 A2, Abdeckungen | nicht im CAD | 18 | bestellfähig | Kaufteile |
| [SYS-060](../Teileliste.md#sys-060) Nutenstein I-Typ Nut 6, M5, Abdeckungen | nicht im CAD | 18 | bestellfähig | Kaufteile |

**Offene Fragen**

- Acrylglas-Preis nur im Konfigurator von plattenzuschnitt24 ablesbar (Schätzung 31 EUR).

<a id="modul-12"></a>

## M12 Beleuchtung

LED-Beleuchtung rundum oben innen am Rahmen, geschaltet und gedimmt über den Heizbett-Ausgang der Licht-Steuerplatine (Einheit 3, M376).

*Am 18.10.2026 angelegt; keine CAD-Teile.*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [SYS-007](../Teileliste.md#sys-007) Weißer 24-V-LED-Streifen LUXULA LX700101 | nicht im CAD | 1.9 | bestellfähig | Kaufteile |
| [SYS-008](../Teileliste.md#sys-008) LED-Aluprofile Barthelme BARdolino mit Diffusor, Kappen, Klammern | nicht im CAD | 1 | bestellfähig | Kaufteile |
| [SYS-009](../Teileliste.md#sys-009) LED-Anschluss an den Heizbett-Ausgang der Licht-Steuerplatine | nicht im CAD | 1 | teilweise geklärt | Kaufteile |

**Offene Fragen**

- Befestigung der BARdolino-Klammern am 30er-Profil (Schraube + Nutenstein) festlegen.
- Anschlussleitung von der SKR zu den 4 Profilstücken (2-adrig, ca. 0,5 mm²) bei M11 Verkabelung mitplanen.

<a id="modul-13"></a>

## M13 Kalibrierung

Gedruckte Kalibrierplatte v4 (SCHUTZWERK-Original) mit Messing-Referenzstiften, gedruckten weißen Außenstiften und Hamming-Markereinlagen; Maße aus calibration_plate.asm und der Software (cli.py, reference_board.py).

*Am 18.10.2026 angelegt; am 26.10.2026 auf die gedruckte SCHUTZWERK-Platte umgestellt.*

| ID / Teil | CAD-Name | Stück | Status | Beschaffungsart |
| --- | --- | --- | --- | --- |
| [SYS-005](../Teileliste.md#sys-005) Innere Messing-Referenzzylinder Ø7/8/9/10 | nicht im CAD | 4 | Fertigung spezifiziert | Weitere Fertigung |
| [SYS-039](../Teileliste.md#sys-039) Erhöhte Messing-Referenzzylinder | nicht im CAD | 4 | Fertigung spezifiziert | Weitere Fertigung |
| [SYS-040](../Teileliste.md#sys-040) Äußere flache Messing-Referenzzylinder Ø7 | nicht im CAD | 4 | Fertigung spezifiziert | Weitere Fertigung |
| [SYS-061](../Teileliste.md#sys-061) Kalibrierplatte Version 4, Druck | nicht im CAD | 1 | Fertigung spezifiziert | 3D-Druck intern |
| [SYS-062](../Teileliste.md#sys-062) Kalibrier-Markereinlagen IDs 1/3/6/12, Druck | nicht im CAD | 4 | Fertigung spezifiziert | 3D-Druck intern |
| [SYS-063](../Teileliste.md#sys-063) Kalibrierstifte, Druck | nicht im CAD | 4 | Fertigung spezifiziert | 3D-Druck intern |

**Zusätzlich nötig, nicht im CAD**

| Teil | Stück | Bezug | Grund |
| --- | --- | --- | --- |
| Messing-Rundstab Ø7, Ø8, Ø9, Ø10 | je ca. 100 mm | SYS-005/039/040 | Rohmaterial für die Werkstatt; noch kein Artikel ausgewählt. |

**Bei der Prüfung aus dem Modul genommen**

- SYS-004 Alu-Platte, SYS-006 gravierte Marker und SYS-037 weiße POM-Referenzen: ersetzt durch die SCHUTZWERK-Druckteile SYS-061/062/063 (Entscheidung Luis 26.10.2026).

**Offene Fragen**

- Plattendicke 17 mm gegen Softwareparameter (cli.py: 5,1 mm) prüfen.
- Messing-Rohmaterial noch nicht ausgewählt.

## Abdeckung

Alle CAD-Vorkommen sind einem Modul zugeordnet außer: NEMA14 Z-Motor, ERSATZ: STEPPERONLINE 14HS13-0804S statt Nanotec ST3518M1004-A (4); Prüfobjekt-Platzhalter im CAD (1); Multiplexer-Platzhalter im CAD (1). Das sind CAD-Platzhalter bzw. doppelte Motor-Einbaulagen.
