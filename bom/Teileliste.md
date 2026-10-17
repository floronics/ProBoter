# Teileliste für einen PROBoter mit vier Prüfeinheiten

Stand16.10.2026. **Planungsstückliste mit expliziten Lücken, keine bestätigte Original-BOM.**

CAD/Fusion-Mengen bleiben unverändert; die Planmenge ist eine getrennte Entscheidung. Alle Maße in mm. `CAD-xxx` sind stabile IDs dieses Inventurstandes; `SYS-xxx` ergänzen Systembedarf. Änderungen von IDs nur mit Migration. [Bestellübersicht](Bestellliste.md) · [Fertigung](Fertigung.md) · [CSV](teileliste.csv) · [CAD-Beweise](CAD-Pruefung.md).

**Status:** bestellfähig = Modell und Bezugsquelle eindeutig (Liefertermin trotzdem prüfen); teilweise geklärt = Familie bekannt, mindestens eine Passungs-/Mengenfrage offen; Fertigung spezifiziert = Material, Zeichnung und Verfahren freigegeben; Fertigung noch offen = mindestens eine dieser Angaben fehlt; nicht identifiziert = erforderliche genaueIdentität unbekannt; nicht benötigt = begründeter Ausschluss. Aktuell erreicht kein Sonderteil den Status Fertigung spezifiziert.

# Teile nach Komponente

Die 13 übergeordneten Komponenten sind die obersten Einbauten im Fusion-Modell; K14 sammelt die Teile ohne CAD-Körper. Teile aus Unterbaugruppen bleiben bei ihrer Komponente, die Unterbaugruppe steht in der zweiten Spalte. Die Stückzahlen sind STEP-Mengen je Komponente; die Planmenge gilt für die ganze Maschine und steht in den Details. [CSV je Komponente](teileliste-komponenten.csv)

| Komponente | Inhalt | Positionen | Stück laut CAD |
| --- | --- | --- | --- |
| [K01 base:1](#komp-01) | Grundgestell mit X-Antrieben, Platinen- und Kamerahalter | 63 | 454 |
| [K02 x_slide:1](#komp-02) | X-Wagen einer Prüfeinheit | 36 | 82 |
| [K03 x_slide:2](#komp-03) | X-Wagen einer Prüfeinheit | 36 | 82 |
| [K04 x_slide:3](#komp-04) | X-Wagen einer Prüfeinheit | 36 | 82 |
| [K05 x_slide:4](#komp-05) | X-Wagen einer Prüfeinheit | 36 | 82 |
| [K06 y_slide (1):1](#komp-06) | Y-Schlitten | 26 | 56 |
| [K07 y_slide (1):2](#komp-07) | Y-Schlitten | 26 | 56 |
| [K08 y_slide_mirrored (1):1](#komp-08) | Y-Schlitten, gespiegelt | 26 | 56 |
| [K09 y_slide_mirrored (1):2](#komp-09) | Y-Schlitten, gespiegelt | 26 | 56 |
| [K10 z_slide:1](#komp-10) | Z-Achse | 11 | 15 |
| [K11 z_slide:2](#komp-11) | Z-Achse | 11 | 15 |
| [K12 z_slide_long:1](#komp-12) | Z-Achse, lange Ausführung | 11 | 15 |
| [K13 z_slide_long:2](#komp-13) | Z-Achse, lange Ausführung | 11 | 15 |
| [K14 Nicht im CAD-Modell](#komp-14) | Systemteile ohne CAD-Körper | 56 | – |

<a id="komp-01"></a>

## K01 base:1 – Grundgestell mit X-Antrieben, Platinen- und Kamerahalter

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-003](#cad-003) Grundgestell: Rückseite Platte | direkt | `base_back_plate` | 1 | Fertigung noch offen |
| [CAD-004](#cad-004) Grundgestell: Kabel Halter M3 flach | direkt | `base_cable_holder_m3_flat` | 2 | Fertigung spezifiziert |
| [CAD-005](#cad-005) Grundgestell: Kabel Halter M4 | direkt | `base_cable_holder_m4` | 1 | Fertigung spezifiziert |
| [CAD-007](#cad-007) Grundgestell: Abdeckung lang Seite | direkt | `base_cover_long_side` | 2 | Fertigung noch offen |
| [CAD-008](#cad-008) Grundgestell: Abdeckung oben | direkt | `base_cover_top` | 2 | Fertigung noch offen |
| [CAD-009](#cad-009) Grundgestell: Schlepp Energiekette Halter | direkt | `base_drag_chain_holder` | 4 | teilweise geklärt |
| [CAD-010](#cad-010) Schubladen-Dummyplatte | direkt | `base_drawer_dummy_plate` | 1 | nicht identifiziert |
| [CAD-011](#cad-011) Grundgestell: Schublade lang Seite | direkt | `base_drawer_long_side` | 2 | bestellfähig |
| [CAD-012](#cad-012) Grundgestell: Rahmen lang Seite | direkt | `base_frame_long_side` | 3 | bestellfähig |
| [CAD-013](#cad-013) Grundgestell: Rahmen kurz | direkt | `base_frame_short` | 8 | bestellfähig |
| [CAD-014](#cad-014) Grundgestell: Rahmen Seite | direkt | `base_frame_side` | 2 | bestellfähig |
| [CAD-018](#cad-018) Grundgestell: Platte Adapter links | direkt | `base_plate_adapter_left` | 2 | Fertigung noch offen |
| [CAD-019](#cad-019) Grundgestell: Platte Adapter rechts | direkt | `base_plate_adapter_right` | 2 | Fertigung noch offen |
| [CAD-020](#cad-020) Grundgestell: vertikal | direkt | `base_vertical` | 4 | bestellfähig |
| [CAD-023](#cad-023) BIGTREETECH SKR V1.3 Steuerplatine | direkt | `bigtreetech_skr_v1_3` | 4 | teilweise geklärt |
| [CAD-024](#cad-024) Kabel Abdeckung | direkt | `cable_cover` | 4 | Fertigung spezifiziert |
| [CAD-033](#cad-033) DIN 7991 M6×14 | direkt | `din_7991_m6x14` | 6 | bestellfähig; Plan gesamt 8 statt 6 |
| [CAD-034](#cad-034) DIN 7991 M6×20 | direkt | `din_7991_m6x20` | 22 | bestellfähig; Plan gesamt 25 statt 22 |
| [CAD-050](#cad-050) igus E2i.10.20.028.0, 8 lange Abschnitte | direkt | `drag_chain_0_28m_E2i_10_20_028_0_igus` | 8 | bestellfähig |
| [CAD-051](#cad-051) Schubladengriff DOLD A-75873, Lochabstand 100 mm | direkt | `handle_l100_dold` | 1 | bestellfähig |
| [CAD-052](#cad-052) Gelenkfuß M6×20 / Teller Ø40 mm | direkt | `hinged_M6_40_dold` | 4 | bestellfähig |
| [CAD-055](#cad-055) Induktiver Näherungsschalter M8, Bauhülle 60 mm | direkt | `inductive_proximity_sensor_m8` | 8 | nicht identifiziert |
| [CAD-058](#cad-058) ISO 8673 Mutter M8 | direkt | `iso_8673_nut_m8` | 8 | teilweise geklärt; Plan gesamt 53 statt 48 |
| [CAD-059](#cad-059) Mean Well MHS012 Montagewinkel | direkt | `mean_well_MHS-012_mounting_bracket` | 4 | bestellfähig |
| [CAD-060](#cad-060) Mean Well RSP-200-24 Netzteil,24 V/8,4 A | direkt | `mean_well_RSP-200-24` | 1 | bestellfähig |
| [CAD-066](#cad-066) Prüfobjekt-Platzhalter im CAD | direkt | `pcb_dummy` | 1 | nicht benötigt; Plan gesamt 0 statt 1 |
| [CAD-074](#cad-074) Stromversorgung Schalter Halter | direkt | `power_switch_holder` | 1 | Fertigung spezifiziert |
| [CAD-081](#cad-081) Anschraubwinkel 30 / Nut 6 | direkt | `screw_on_bracket_30_6` | 26 | bestellfähig |
| [CAD-082](#cad-082) Multiplexer-Platzhalter im CAD | direkt | `signal_multiplexer_dummy` | 1 | nicht benötigt; Plan gesamt 0 statt 1 |
| [CAD-083](#cad-083) Signal-Multiplexer Halter | direkt | `signal_multiplexer_holder` | 1 | Fertigung spezifiziert |
| [CAD-084](#cad-084) Teleskopschiene 350 mm, Vollauszug | direkt | `telescopic_bar_tsaa514613-350` | 2 | bestellfähig |
| [CAD-086](#cad-086) Bedientaster/-schalterØ19 mm | direkt | `vandalism_switch_d19` | 1 | nicht identifiziert |
| [CAD-095](#cad-095) CPC MR12M Führungsschiene 600 mm | direkt | `x_guiding_cpc_MR12M` | 2 | bestellfähig |
| [CAD-096](#cad-096) X-Achse Motor Platte | direkt | `x_motor_plate` | 1 | Fertigung noch offen |
| [CAD-097](#cad-097) X-Achse Motor Platte 2 | direkt | `x_motor_plate_2` | 1 | Fertigung noch offen |
| [CAD-016](#cad-016) Grundgestell: Platte Adapter 1 | `base_plate_adapter` | `base_plate_adapter_1` | 2 | Fertigung noch offen |
| [CAD-017](#cad-017) Grundgestell: Platte Adapter 2 | `base_plate_adapter` | `base_plate_adapter_2` | 2 | Fertigung noch offen |
| [CAD-025](#cad-025) Kamera Halter | `camera_holder` | `camera_holder` | 1 | Fertigung spezifiziert |
| [CAD-026](#cad-026) Kamera Halter oben | `camera_holder` | `camera_holder_top` | 1 | Fertigung noch offen |
| [CAD-028](#cad-028) DIN 466 Rändelmutter hoch M4 | `pcb_holder` | `din_466_knurled_nut_high_m4` | 8 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-043](#cad-043) DIN 912 M4×10 | `pcb_holder` | `din_912_m4x10` | 1 | bestellfähig; Plan gesamt 3 statt 1 |
| [CAD-048](#cad-048) DIN 933 M4×20 | `pcb_holder` | `din_933_m4x20` | 8 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-067](#cad-067) Platine Halter Gleiter | `pcb_holder` | `pcb_holder_glider` | 4 | Fertigung spezifiziert |
| [CAD-068](#cad-068) Platine Halter Führung Halter rund d 10 | `pcb_holder` | `pcb_holder_guiding_holder_round_d10` | 4 | Fertigung spezifiziert |
| [CAD-069](#cad-069) Platine Halter Führung rund | `pcb_holder` | `pcb_holder_guiding_round` | 2 | bestellfähig |
| [CAD-070](#cad-070) Platine Halter rechteckig Stange | `pcb_holder` | `pcb_holder_rect_rod` | 2 | Fertigung noch offen |
| [CAD-071](#cad-071) Platine Halter Stange kurz rund d 10 | `pcb_holder` | `pcb_holder_rod_short_round_d10` | 2 | Fertigung spezifiziert |
| [CAD-072](#cad-072) Platine Halter Stange kurz rund d 10 gespiegelt | `pcb_holder` | `pcb_holder_rod_short_round_d10_mirrored` | 2 | Fertigung spezifiziert |
| [CAD-015](#cad-015) Grundgestell: NEMA 14 auf 17 Adapter | `x_belt_drive` | `base_nema_14_to_17_adapter` | 8 | Fertigung spezifiziert |
| [CAD-021](#cad-021) Riemen Spanner GT2 Basis | `x_belt_drive` | `belt_tightener_GT2_base` | 16 | Fertigung spezifiziert |
| [CAD-022](#cad-022) Riemen Spanner GT2 Flügel | `x_belt_drive` | `belt_tightener_GT2_wing` | 16 | Fertigung spezifiziert |
| [CAD-035](#cad-035) DIN 912 M3×10 | `x_belt_drive` | `din_912_m3x10` | 32 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-038](#cad-038) DIN 912 M3×16 | `x_belt_drive` | `din_912_m3x16` | 16 | bestellfähig; Plan gesamt 31 statt 28 |
| [CAD-039](#cad-039) DIN 912 M3×18 | `x_belt_drive` | `din_912_m3x18` | 32 | bestellfähig; Plan gesamt 36 statt 32 |
| [CAD-042](#cad-042) DIN 912 M3×8 | `x_belt_drive` | `din_912_m3x8` | 32 | bestellfähig; Plan gesamt 58 statt 52 |
| [CAD-044](#cad-044) DIN 912 M4×20 | `x_belt_drive` | `din_912_m4x20` | 16 | bestellfähig; Plan gesamt 22 statt 20 |
| [CAD-045](#cad-045) DIN 912 M4×30 | `x_belt_drive` | `din_912_m4x30` | 16 | bestellfähig; Plan gesamt 40 statt 36 |
| [CAD-056](#cad-056) Sechskantmutter DIN 934 M3 A2 | `x_belt_drive` | `iso_8673_nut_m3` | 16 | bestellfähig; Plan gesamt 49 statt 44 |
| [CAD-057](#cad-057) Sechskantmutter DIN 934 M4 A2 | `x_belt_drive` | `iso_8673_nut_m4` | 32 | bestellfähig; Plan gesamt 71 statt 64 |
| [CAD-064](#cad-064) Nanotec ST4118M1804-A NEMA17 X/Y-Motor | `x_belt_drive` | `nanotec_nema_17_ST4118M1804-A` | 8 | bestellfähig; fehlt im Fusion-Import |
| [CAD-077](#cad-077) GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | `x_belt_drive` | `pulley_gt2_z16_6mm` | 8 | bestellfähig |
| [CAD-078](#cad-078) GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | `x_belt_drive` | `return_pulley_gt2_z16_6mm` | 16 | bestellfähig |
| [CAD-087](#cad-087) GT2-Riemen X, 6 mm breit | `x_belt_drive` | `x_belt` | 8 | bestellfähig |

<a id="komp-02"></a>

## K02 x_slide:1 – X-Wagen einer Prüfeinheit

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-006](#cad-006) Grundgestell: Kabel Halter M5 flach | direkt | `base_cable_holder_m5_flat` | 1 | Fertigung spezifiziert |
| [CAD-027](#cad-027) CPC MR12ML Führungswagen | direkt | `cpc_MR12ML` | 2 | bestellfähig |
| [CAD-031](#cad-031) DIN 7991 M3×8 | direkt | `din_7991_m3x8` | 8 | bestellfähig; Plan gesamt 36 statt 32 |
| [CAD-032](#cad-032) DIN 7991 M6×12 | direkt | `din_7991_m6x12` | 4 | bestellfähig; Plan gesamt 18 statt 16 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 4 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-046](#cad-046) DIN 912 M5×10 | direkt | `din_912_m5x10` | 8 | bestellfähig; Plan gesamt 36 statt 32 |
| [CAD-047](#cad-047) DIN 912 M5×14 | direkt | `din_912_m5x14` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-049](#cad-049) igus E2i.10.10.028.0, 16 kurze Abschnitte | direkt | `drag_chain_0_24m_E2i_10_10_028_0_4` | 4 | bestellfähig |
| [CAD-055](#cad-055) Induktiver Näherungsschalter M8, Bauhülle 60 mm | direkt | `inductive_proximity_sensor_m8` | 4 | nicht identifiziert |
| [CAD-058](#cad-058) ISO 8673 Mutter M8 | direkt | `iso_8673_nut_m8` | 10 | teilweise geklärt; Plan gesamt 53 statt 48 |
| [CAD-079](#cad-079) SHF10 Flanschhalter fürØ10 mm Welle | direkt | `rod_holder_flange_d10_dold` | 4 | bestellfähig |
| [CAD-088](#cad-088) X-Achse Riemen Halter | direkt | `x_belt_holder` | 1 | Fertigung spezifiziert |
| [CAD-089](#cad-089) X-Achse Riemen Halter 1 | direkt | `x_belt_holder_1` | 3 | Fertigung spezifiziert |
| [CAD-090](#cad-090) X-Achse Schlepp Energiekette Adapter | direkt | `x_drag_chain_adapter` | 2 | Fertigung spezifiziert |
| [CAD-091](#cad-091) X-Achse Endschalter Halter Seite kurz | direkt | `x_end_stop_holder_side_short` | 1 | Fertigung spezifiziert |
| [CAD-092](#cad-092) X-Achse Endschalter Halter oben lang | direkt | `x_end_stop_holder_top_long` | 1 | Fertigung spezifiziert |
| [CAD-093](#cad-093) X-Achse Endschalter oben lang | direkt | `x_end_stop_top_long` | 1 | Fertigung noch offen |
| [CAD-094](#cad-094) X-Achse Endschalter oben kurz | direkt | `x_end_stop_top_short` | 1 | Fertigung noch offen |
| [CAD-098](#cad-098) X-Achse rund Schiene | direkt | `x_round_rail` | 2 | bestellfähig |
| [CAD-099](#cad-099) X-Achse Seite Platte | direkt | `x_side_plate` | 1 | Fertigung noch offen |
| [CAD-100](#cad-100) X-Achse Seite Platte beweglich | direkt | `x_side_plate_moving` | 1 | Fertigung noch offen |
| [CAD-101](#cad-101) X-Achse Schlitten induktiv Endschalter Adapter | direkt | `x_slide_inductive_endstop_adapter` | 1 | Fertigung spezifiziert |
| [CAD-102](#cad-102) X-Achse Schlitten induktiv Endschalter Adapter gespiegelt | direkt | `x_slide_inductive_endstop_adapter_mirrored` | 1 | Fertigung spezifiziert |
| [CAD-103](#cad-103) X-Achse Schlitten Versteifung Träger | direkt | `x_slide_stiffener_beam` | 1 | bestellfähig |
| [CAD-015](#cad-015) Grundgestell: NEMA 14 auf 17 Adapter | `y_belt_drive` | `base_nema_14_to_17_adapter` | 1 | Fertigung spezifiziert |
| [CAD-021](#cad-021) Riemen Spanner GT2 Basis | `y_belt_drive` | `belt_tightener_GT2_base` | 1 | Fertigung spezifiziert |
| [CAD-022](#cad-022) Riemen Spanner GT2 Flügel | `y_belt_drive` | `belt_tightener_GT2_wing` | 1 | Fertigung spezifiziert |
| [CAD-035](#cad-035) DIN 912 M3×10 | `y_belt_drive` | `din_912_m3x10` | 2 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-038](#cad-038) DIN 912 M3×16 | `y_belt_drive` | `din_912_m3x16` | 1 | bestellfähig; Plan gesamt 31 statt 28 |
| [CAD-044](#cad-044) DIN 912 M4×20 | `y_belt_drive` | `din_912_m4x20` | 1 | bestellfähig; Plan gesamt 22 statt 20 |
| [CAD-045](#cad-045) DIN 912 M4×30 | `y_belt_drive` | `din_912_m4x30` | 1 | bestellfähig; Plan gesamt 40 statt 36 |
| [CAD-056](#cad-056) Sechskantmutter DIN 934 M3 A2 | `y_belt_drive` | `iso_8673_nut_m3` | 1 | bestellfähig; Plan gesamt 49 statt 44 |
| [CAD-057](#cad-057) Sechskantmutter DIN 934 M4 A2 | `y_belt_drive` | `iso_8673_nut_m4` | 2 | bestellfähig; Plan gesamt 71 statt 64 |
| [CAD-064](#cad-064) Nanotec ST4118M1804-A NEMA17 X/Y-Motor | `y_belt_drive` | `nanotec_nema_17_ST4118M1804-A` | 1 | bestellfähig; fehlt im Fusion-Import |
| [CAD-077](#cad-077) GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | `y_belt_drive` | `pulley_gt2_z16_6mm` | 1 | bestellfähig |
| [CAD-078](#cad-078) GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | `y_belt_drive` | `return_pulley_gt2_z16_6mm` | 1 | bestellfähig |
| [CAD-104](#cad-104) GT2-Riemen Y, 6 mm breit | `y_belt_drive` | `y_belt` | 1 | bestellfähig |

<a id="komp-03"></a>

## K03 x_slide:2 – X-Wagen einer Prüfeinheit

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-006](#cad-006) Grundgestell: Kabel Halter M5 flach | direkt | `base_cable_holder_m5_flat` | 1 | Fertigung spezifiziert |
| [CAD-027](#cad-027) CPC MR12ML Führungswagen | direkt | `cpc_MR12ML` | 2 | bestellfähig |
| [CAD-031](#cad-031) DIN 7991 M3×8 | direkt | `din_7991_m3x8` | 8 | bestellfähig; Plan gesamt 36 statt 32 |
| [CAD-032](#cad-032) DIN 7991 M6×12 | direkt | `din_7991_m6x12` | 4 | bestellfähig; Plan gesamt 18 statt 16 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 4 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-046](#cad-046) DIN 912 M5×10 | direkt | `din_912_m5x10` | 8 | bestellfähig; Plan gesamt 36 statt 32 |
| [CAD-047](#cad-047) DIN 912 M5×14 | direkt | `din_912_m5x14` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-049](#cad-049) igus E2i.10.10.028.0, 16 kurze Abschnitte | direkt | `drag_chain_0_24m_E2i_10_10_028_0_4` | 4 | bestellfähig |
| [CAD-055](#cad-055) Induktiver Näherungsschalter M8, Bauhülle 60 mm | direkt | `inductive_proximity_sensor_m8` | 4 | nicht identifiziert |
| [CAD-058](#cad-058) ISO 8673 Mutter M8 | direkt | `iso_8673_nut_m8` | 10 | teilweise geklärt; Plan gesamt 53 statt 48 |
| [CAD-079](#cad-079) SHF10 Flanschhalter fürØ10 mm Welle | direkt | `rod_holder_flange_d10_dold` | 4 | bestellfähig |
| [CAD-088](#cad-088) X-Achse Riemen Halter | direkt | `x_belt_holder` | 1 | Fertigung spezifiziert |
| [CAD-089](#cad-089) X-Achse Riemen Halter 1 | direkt | `x_belt_holder_1` | 3 | Fertigung spezifiziert |
| [CAD-090](#cad-090) X-Achse Schlepp Energiekette Adapter | direkt | `x_drag_chain_adapter` | 2 | Fertigung spezifiziert |
| [CAD-091](#cad-091) X-Achse Endschalter Halter Seite kurz | direkt | `x_end_stop_holder_side_short` | 1 | Fertigung spezifiziert |
| [CAD-092](#cad-092) X-Achse Endschalter Halter oben lang | direkt | `x_end_stop_holder_top_long` | 1 | Fertigung spezifiziert |
| [CAD-093](#cad-093) X-Achse Endschalter oben lang | direkt | `x_end_stop_top_long` | 1 | Fertigung noch offen |
| [CAD-094](#cad-094) X-Achse Endschalter oben kurz | direkt | `x_end_stop_top_short` | 1 | Fertigung noch offen |
| [CAD-098](#cad-098) X-Achse rund Schiene | direkt | `x_round_rail` | 2 | bestellfähig |
| [CAD-099](#cad-099) X-Achse Seite Platte | direkt | `x_side_plate` | 1 | Fertigung noch offen |
| [CAD-100](#cad-100) X-Achse Seite Platte beweglich | direkt | `x_side_plate_moving` | 1 | Fertigung noch offen |
| [CAD-101](#cad-101) X-Achse Schlitten induktiv Endschalter Adapter | direkt | `x_slide_inductive_endstop_adapter` | 1 | Fertigung spezifiziert |
| [CAD-102](#cad-102) X-Achse Schlitten induktiv Endschalter Adapter gespiegelt | direkt | `x_slide_inductive_endstop_adapter_mirrored` | 1 | Fertigung spezifiziert |
| [CAD-103](#cad-103) X-Achse Schlitten Versteifung Träger | direkt | `x_slide_stiffener_beam` | 1 | bestellfähig |
| [CAD-015](#cad-015) Grundgestell: NEMA 14 auf 17 Adapter | `y_belt_drive` | `base_nema_14_to_17_adapter` | 1 | Fertigung spezifiziert |
| [CAD-021](#cad-021) Riemen Spanner GT2 Basis | `y_belt_drive` | `belt_tightener_GT2_base` | 1 | Fertigung spezifiziert |
| [CAD-022](#cad-022) Riemen Spanner GT2 Flügel | `y_belt_drive` | `belt_tightener_GT2_wing` | 1 | Fertigung spezifiziert |
| [CAD-035](#cad-035) DIN 912 M3×10 | `y_belt_drive` | `din_912_m3x10` | 2 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-038](#cad-038) DIN 912 M3×16 | `y_belt_drive` | `din_912_m3x16` | 1 | bestellfähig; Plan gesamt 31 statt 28 |
| [CAD-044](#cad-044) DIN 912 M4×20 | `y_belt_drive` | `din_912_m4x20` | 1 | bestellfähig; Plan gesamt 22 statt 20 |
| [CAD-045](#cad-045) DIN 912 M4×30 | `y_belt_drive` | `din_912_m4x30` | 1 | bestellfähig; Plan gesamt 40 statt 36 |
| [CAD-056](#cad-056) Sechskantmutter DIN 934 M3 A2 | `y_belt_drive` | `iso_8673_nut_m3` | 1 | bestellfähig; Plan gesamt 49 statt 44 |
| [CAD-057](#cad-057) Sechskantmutter DIN 934 M4 A2 | `y_belt_drive` | `iso_8673_nut_m4` | 2 | bestellfähig; Plan gesamt 71 statt 64 |
| [CAD-064](#cad-064) Nanotec ST4118M1804-A NEMA17 X/Y-Motor | `y_belt_drive` | `nanotec_nema_17_ST4118M1804-A` | 1 | bestellfähig; fehlt im Fusion-Import |
| [CAD-077](#cad-077) GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | `y_belt_drive` | `pulley_gt2_z16_6mm` | 1 | bestellfähig |
| [CAD-078](#cad-078) GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | `y_belt_drive` | `return_pulley_gt2_z16_6mm` | 1 | bestellfähig |
| [CAD-104](#cad-104) GT2-Riemen Y, 6 mm breit | `y_belt_drive` | `y_belt` | 1 | bestellfähig |

<a id="komp-04"></a>

## K04 x_slide:3 – X-Wagen einer Prüfeinheit

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-006](#cad-006) Grundgestell: Kabel Halter M5 flach | direkt | `base_cable_holder_m5_flat` | 1 | Fertigung spezifiziert |
| [CAD-027](#cad-027) CPC MR12ML Führungswagen | direkt | `cpc_MR12ML` | 2 | bestellfähig |
| [CAD-031](#cad-031) DIN 7991 M3×8 | direkt | `din_7991_m3x8` | 8 | bestellfähig; Plan gesamt 36 statt 32 |
| [CAD-032](#cad-032) DIN 7991 M6×12 | direkt | `din_7991_m6x12` | 4 | bestellfähig; Plan gesamt 18 statt 16 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 4 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-046](#cad-046) DIN 912 M5×10 | direkt | `din_912_m5x10` | 8 | bestellfähig; Plan gesamt 36 statt 32 |
| [CAD-047](#cad-047) DIN 912 M5×14 | direkt | `din_912_m5x14` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-049](#cad-049) igus E2i.10.10.028.0, 16 kurze Abschnitte | direkt | `drag_chain_0_24m_E2i_10_10_028_0_4` | 4 | bestellfähig |
| [CAD-055](#cad-055) Induktiver Näherungsschalter M8, Bauhülle 60 mm | direkt | `inductive_proximity_sensor_m8` | 4 | nicht identifiziert |
| [CAD-058](#cad-058) ISO 8673 Mutter M8 | direkt | `iso_8673_nut_m8` | 10 | teilweise geklärt; Plan gesamt 53 statt 48 |
| [CAD-079](#cad-079) SHF10 Flanschhalter fürØ10 mm Welle | direkt | `rod_holder_flange_d10_dold` | 4 | bestellfähig |
| [CAD-088](#cad-088) X-Achse Riemen Halter | direkt | `x_belt_holder` | 1 | Fertigung spezifiziert |
| [CAD-089](#cad-089) X-Achse Riemen Halter 1 | direkt | `x_belt_holder_1` | 3 | Fertigung spezifiziert |
| [CAD-090](#cad-090) X-Achse Schlepp Energiekette Adapter | direkt | `x_drag_chain_adapter` | 2 | Fertigung spezifiziert |
| [CAD-091](#cad-091) X-Achse Endschalter Halter Seite kurz | direkt | `x_end_stop_holder_side_short` | 1 | Fertigung spezifiziert |
| [CAD-092](#cad-092) X-Achse Endschalter Halter oben lang | direkt | `x_end_stop_holder_top_long` | 1 | Fertigung spezifiziert |
| [CAD-093](#cad-093) X-Achse Endschalter oben lang | direkt | `x_end_stop_top_long` | 1 | Fertigung noch offen |
| [CAD-094](#cad-094) X-Achse Endschalter oben kurz | direkt | `x_end_stop_top_short` | 1 | Fertigung noch offen |
| [CAD-098](#cad-098) X-Achse rund Schiene | direkt | `x_round_rail` | 2 | bestellfähig |
| [CAD-099](#cad-099) X-Achse Seite Platte | direkt | `x_side_plate` | 1 | Fertigung noch offen |
| [CAD-100](#cad-100) X-Achse Seite Platte beweglich | direkt | `x_side_plate_moving` | 1 | Fertigung noch offen |
| [CAD-101](#cad-101) X-Achse Schlitten induktiv Endschalter Adapter | direkt | `x_slide_inductive_endstop_adapter` | 1 | Fertigung spezifiziert |
| [CAD-102](#cad-102) X-Achse Schlitten induktiv Endschalter Adapter gespiegelt | direkt | `x_slide_inductive_endstop_adapter_mirrored` | 1 | Fertigung spezifiziert |
| [CAD-103](#cad-103) X-Achse Schlitten Versteifung Träger | direkt | `x_slide_stiffener_beam` | 1 | bestellfähig |
| [CAD-015](#cad-015) Grundgestell: NEMA 14 auf 17 Adapter | `y_belt_drive` | `base_nema_14_to_17_adapter` | 1 | Fertigung spezifiziert |
| [CAD-021](#cad-021) Riemen Spanner GT2 Basis | `y_belt_drive` | `belt_tightener_GT2_base` | 1 | Fertigung spezifiziert |
| [CAD-022](#cad-022) Riemen Spanner GT2 Flügel | `y_belt_drive` | `belt_tightener_GT2_wing` | 1 | Fertigung spezifiziert |
| [CAD-035](#cad-035) DIN 912 M3×10 | `y_belt_drive` | `din_912_m3x10` | 2 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-038](#cad-038) DIN 912 M3×16 | `y_belt_drive` | `din_912_m3x16` | 1 | bestellfähig; Plan gesamt 31 statt 28 |
| [CAD-044](#cad-044) DIN 912 M4×20 | `y_belt_drive` | `din_912_m4x20` | 1 | bestellfähig; Plan gesamt 22 statt 20 |
| [CAD-045](#cad-045) DIN 912 M4×30 | `y_belt_drive` | `din_912_m4x30` | 1 | bestellfähig; Plan gesamt 40 statt 36 |
| [CAD-056](#cad-056) Sechskantmutter DIN 934 M3 A2 | `y_belt_drive` | `iso_8673_nut_m3` | 1 | bestellfähig; Plan gesamt 49 statt 44 |
| [CAD-057](#cad-057) Sechskantmutter DIN 934 M4 A2 | `y_belt_drive` | `iso_8673_nut_m4` | 2 | bestellfähig; Plan gesamt 71 statt 64 |
| [CAD-064](#cad-064) Nanotec ST4118M1804-A NEMA17 X/Y-Motor | `y_belt_drive` | `nanotec_nema_17_ST4118M1804-A` | 1 | bestellfähig; fehlt im Fusion-Import |
| [CAD-077](#cad-077) GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | `y_belt_drive` | `pulley_gt2_z16_6mm` | 1 | bestellfähig |
| [CAD-078](#cad-078) GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | `y_belt_drive` | `return_pulley_gt2_z16_6mm` | 1 | bestellfähig |
| [CAD-104](#cad-104) GT2-Riemen Y, 6 mm breit | `y_belt_drive` | `y_belt` | 1 | bestellfähig |

<a id="komp-05"></a>

## K05 x_slide:4 – X-Wagen einer Prüfeinheit

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-006](#cad-006) Grundgestell: Kabel Halter M5 flach | direkt | `base_cable_holder_m5_flat` | 1 | Fertigung spezifiziert |
| [CAD-027](#cad-027) CPC MR12ML Führungswagen | direkt | `cpc_MR12ML` | 2 | bestellfähig |
| [CAD-031](#cad-031) DIN 7991 M3×8 | direkt | `din_7991_m3x8` | 8 | bestellfähig; Plan gesamt 36 statt 32 |
| [CAD-032](#cad-032) DIN 7991 M6×12 | direkt | `din_7991_m6x12` | 4 | bestellfähig; Plan gesamt 18 statt 16 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 4 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-046](#cad-046) DIN 912 M5×10 | direkt | `din_912_m5x10` | 8 | bestellfähig; Plan gesamt 36 statt 32 |
| [CAD-047](#cad-047) DIN 912 M5×14 | direkt | `din_912_m5x14` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-049](#cad-049) igus E2i.10.10.028.0, 16 kurze Abschnitte | direkt | `drag_chain_0_24m_E2i_10_10_028_0_4` | 4 | bestellfähig |
| [CAD-055](#cad-055) Induktiver Näherungsschalter M8, Bauhülle 60 mm | direkt | `inductive_proximity_sensor_m8` | 4 | nicht identifiziert |
| [CAD-058](#cad-058) ISO 8673 Mutter M8 | direkt | `iso_8673_nut_m8` | 10 | teilweise geklärt; Plan gesamt 53 statt 48 |
| [CAD-079](#cad-079) SHF10 Flanschhalter fürØ10 mm Welle | direkt | `rod_holder_flange_d10_dold` | 4 | bestellfähig |
| [CAD-088](#cad-088) X-Achse Riemen Halter | direkt | `x_belt_holder` | 1 | Fertigung spezifiziert |
| [CAD-089](#cad-089) X-Achse Riemen Halter 1 | direkt | `x_belt_holder_1` | 3 | Fertigung spezifiziert |
| [CAD-090](#cad-090) X-Achse Schlepp Energiekette Adapter | direkt | `x_drag_chain_adapter` | 2 | Fertigung spezifiziert |
| [CAD-091](#cad-091) X-Achse Endschalter Halter Seite kurz | direkt | `x_end_stop_holder_side_short` | 1 | Fertigung spezifiziert |
| [CAD-092](#cad-092) X-Achse Endschalter Halter oben lang | direkt | `x_end_stop_holder_top_long` | 1 | Fertigung spezifiziert |
| [CAD-093](#cad-093) X-Achse Endschalter oben lang | direkt | `x_end_stop_top_long` | 1 | Fertigung noch offen |
| [CAD-094](#cad-094) X-Achse Endschalter oben kurz | direkt | `x_end_stop_top_short` | 1 | Fertigung noch offen |
| [CAD-098](#cad-098) X-Achse rund Schiene | direkt | `x_round_rail` | 2 | bestellfähig |
| [CAD-099](#cad-099) X-Achse Seite Platte | direkt | `x_side_plate` | 1 | Fertigung noch offen |
| [CAD-100](#cad-100) X-Achse Seite Platte beweglich | direkt | `x_side_plate_moving` | 1 | Fertigung noch offen |
| [CAD-101](#cad-101) X-Achse Schlitten induktiv Endschalter Adapter | direkt | `x_slide_inductive_endstop_adapter` | 1 | Fertigung spezifiziert |
| [CAD-102](#cad-102) X-Achse Schlitten induktiv Endschalter Adapter gespiegelt | direkt | `x_slide_inductive_endstop_adapter_mirrored` | 1 | Fertigung spezifiziert |
| [CAD-103](#cad-103) X-Achse Schlitten Versteifung Träger | direkt | `x_slide_stiffener_beam` | 1 | bestellfähig |
| [CAD-015](#cad-015) Grundgestell: NEMA 14 auf 17 Adapter | `y_belt_drive` | `base_nema_14_to_17_adapter` | 1 | Fertigung spezifiziert |
| [CAD-021](#cad-021) Riemen Spanner GT2 Basis | `y_belt_drive` | `belt_tightener_GT2_base` | 1 | Fertigung spezifiziert |
| [CAD-022](#cad-022) Riemen Spanner GT2 Flügel | `y_belt_drive` | `belt_tightener_GT2_wing` | 1 | Fertigung spezifiziert |
| [CAD-035](#cad-035) DIN 912 M3×10 | `y_belt_drive` | `din_912_m3x10` | 2 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-038](#cad-038) DIN 912 M3×16 | `y_belt_drive` | `din_912_m3x16` | 1 | bestellfähig; Plan gesamt 31 statt 28 |
| [CAD-044](#cad-044) DIN 912 M4×20 | `y_belt_drive` | `din_912_m4x20` | 1 | bestellfähig; Plan gesamt 22 statt 20 |
| [CAD-045](#cad-045) DIN 912 M4×30 | `y_belt_drive` | `din_912_m4x30` | 1 | bestellfähig; Plan gesamt 40 statt 36 |
| [CAD-056](#cad-056) Sechskantmutter DIN 934 M3 A2 | `y_belt_drive` | `iso_8673_nut_m3` | 1 | bestellfähig; Plan gesamt 49 statt 44 |
| [CAD-057](#cad-057) Sechskantmutter DIN 934 M4 A2 | `y_belt_drive` | `iso_8673_nut_m4` | 2 | bestellfähig; Plan gesamt 71 statt 64 |
| [CAD-064](#cad-064) Nanotec ST4118M1804-A NEMA17 X/Y-Motor | `y_belt_drive` | `nanotec_nema_17_ST4118M1804-A` | 1 | bestellfähig; fehlt im Fusion-Import |
| [CAD-077](#cad-077) GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | `y_belt_drive` | `pulley_gt2_z16_6mm` | 1 | bestellfähig |
| [CAD-078](#cad-078) GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | `y_belt_drive` | `return_pulley_gt2_z16_6mm` | 1 | bestellfähig |
| [CAD-104](#cad-104) GT2-Riemen Y, 6 mm breit | `y_belt_drive` | `y_belt` | 1 | bestellfähig |

<a id="komp-06"></a>

## K06 y_slide (1):1 – Y-Schlitten

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-001](#cad-001) Y-Riemenklemme (CAD-Name TR10x 2 GT2 Adapter) | direkt | `TR10x2_GT2_belt_adapter` | 1 | Fertigung spezifiziert |
| [CAD-002](#cad-002) Y-Riemenklemme, Deckel | direkt | `TR10x2_GT2_belt_adapter_cover` | 1 | Fertigung spezifiziert |
| [CAD-029](#cad-029) DIN 562 M3 Vierkantmutter | direkt | `din_562_m3_square_nut` | 1 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-030](#cad-030) DIN 562 M4 Vierkantmutter | direkt | `din_562_m4_square_nut` | 3 | bestellfähig; Plan gesamt 14 statt 12 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 4 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-036](#cad-036) DIN 912 M3×12 | direkt | `din_912_m3x12` | 2 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-037](#cad-037) DIN 912 M3×14 | direkt | `din_912_m3x14` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-038](#cad-038) DIN 912 M3×16 | direkt | `din_912_m3x16` | 2 | bestellfähig; Plan gesamt 31 statt 28 |
| [CAD-040](#cad-040) DIN 912 M3×20 | direkt | `din_912_m3x20` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-041](#cad-041) DIN 912 M3×30 | direkt | `din_912_m3x30` | 2 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-042](#cad-042) DIN 912 M3×8 | direkt | `din_912_m3x8` | 4 | bestellfähig; Plan gesamt 58 statt 52 |
| [CAD-045](#cad-045) DIN 912 M4×30 | direkt | `din_912_m4x30` | 4 | bestellfähig; Plan gesamt 40 statt 36 |
| [CAD-054](#cad-054) HIWIN MGN12CZ0HM Z-Führungswagen | direkt | `hiwin_slide_MGN12CZ0H` | 1 | bestellfähig |
| [CAD-056](#cad-056) Sechskantmutter DIN 934 M3 A2 | direkt | `iso_8673_nut_m3` | 6 | bestellfähig; Plan gesamt 49 statt 44 |
| [CAD-057](#cad-057) Sechskantmutter DIN 934 M4 A2 | direkt | `iso_8673_nut_m4` | 6 | bestellfähig; Plan gesamt 71 statt 64 |
| [CAD-063](#cad-063) NEMA14 Z-Motor, ERSATZ: STEPPERONLINE 14HS13-0804S statt Nanotec ST3518M1004-A | direkt | `nanotec_nema_14_ST3518M1004-A` | 2 | bestellfähig; Plan gesamt 4 statt 8 |
| [CAD-065](#cad-065) Optischer Endschalter 11×35 mm | direkt | `optical_endstop` | 1 | bestellfähig |
| [CAD-076](#cad-076) GT2-Zahnscheibe Z16 / 9 mm / Bohrung 5 mm, ANPASSUNG | direkt | `pulley_gt2_9mm` | 2 | bestellfähig |
| [CAD-080](#cad-080) GleitbuchseØ10 innen / Ø19 außen / Länge 29 mm | direkt | `rod_slide_d10_l19` | 4 | bestellfähig |
| [CAD-085](#cad-085) Bewegliches USB-Mikroskop | direkt | `usb_microscope` | 1 | teilweise geklärt; Plan gesamt 1 statt 4 |
| [CAD-105](#cad-105) Y-Achse Kamera Halter | direkt | `y_camera_holder` | 1 | Fertigung spezifiziert |
| [CAD-107](#cad-107) Y-Achse Schlitten | direkt | `y_slide` | 1 | Fertigung spezifiziert |
| [CAD-108](#cad-108) Y-Achse Schlitten Abstand Stange | direkt | `y_slide_distance_rod` | 2 | Fertigung spezifiziert |
| [CAD-109](#cad-109) Y-Achse Schlitten Abstand Rohr 2 mm | direkt | `y_slide_distance_tube_2mm` | 1 | Fertigung spezifiziert |
| [CAD-112](#cad-112) Y-Achse Schlitten oben | direkt | `y_slide_top` | 1 | Fertigung spezifiziert |
| [CAD-113](#cad-113) GT2-Riemen Z, 9 mm breit | direkt | `z_drive_belt` | 1 | bestellfähig |

<a id="komp-07"></a>

## K07 y_slide (1):2 – Y-Schlitten

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-001](#cad-001) Y-Riemenklemme (CAD-Name TR10x 2 GT2 Adapter) | direkt | `TR10x2_GT2_belt_adapter` | 1 | Fertigung spezifiziert |
| [CAD-002](#cad-002) Y-Riemenklemme, Deckel | direkt | `TR10x2_GT2_belt_adapter_cover` | 1 | Fertigung spezifiziert |
| [CAD-029](#cad-029) DIN 562 M3 Vierkantmutter | direkt | `din_562_m3_square_nut` | 1 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-030](#cad-030) DIN 562 M4 Vierkantmutter | direkt | `din_562_m4_square_nut` | 3 | bestellfähig; Plan gesamt 14 statt 12 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 4 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-036](#cad-036) DIN 912 M3×12 | direkt | `din_912_m3x12` | 2 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-037](#cad-037) DIN 912 M3×14 | direkt | `din_912_m3x14` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-038](#cad-038) DIN 912 M3×16 | direkt | `din_912_m3x16` | 2 | bestellfähig; Plan gesamt 31 statt 28 |
| [CAD-040](#cad-040) DIN 912 M3×20 | direkt | `din_912_m3x20` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-041](#cad-041) DIN 912 M3×30 | direkt | `din_912_m3x30` | 2 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-042](#cad-042) DIN 912 M3×8 | direkt | `din_912_m3x8` | 4 | bestellfähig; Plan gesamt 58 statt 52 |
| [CAD-045](#cad-045) DIN 912 M4×30 | direkt | `din_912_m4x30` | 4 | bestellfähig; Plan gesamt 40 statt 36 |
| [CAD-054](#cad-054) HIWIN MGN12CZ0HM Z-Führungswagen | direkt | `hiwin_slide_MGN12CZ0H` | 1 | bestellfähig |
| [CAD-056](#cad-056) Sechskantmutter DIN 934 M3 A2 | direkt | `iso_8673_nut_m3` | 6 | bestellfähig; Plan gesamt 49 statt 44 |
| [CAD-057](#cad-057) Sechskantmutter DIN 934 M4 A2 | direkt | `iso_8673_nut_m4` | 6 | bestellfähig; Plan gesamt 71 statt 64 |
| [CAD-063](#cad-063) NEMA14 Z-Motor, ERSATZ: STEPPERONLINE 14HS13-0804S statt Nanotec ST3518M1004-A | direkt | `nanotec_nema_14_ST3518M1004-A` | 2 | bestellfähig; Plan gesamt 4 statt 8 |
| [CAD-065](#cad-065) Optischer Endschalter 11×35 mm | direkt | `optical_endstop` | 1 | bestellfähig |
| [CAD-076](#cad-076) GT2-Zahnscheibe Z16 / 9 mm / Bohrung 5 mm, ANPASSUNG | direkt | `pulley_gt2_9mm` | 2 | bestellfähig |
| [CAD-080](#cad-080) GleitbuchseØ10 innen / Ø19 außen / Länge 29 mm | direkt | `rod_slide_d10_l19` | 4 | bestellfähig |
| [CAD-085](#cad-085) Bewegliches USB-Mikroskop | direkt | `usb_microscope` | 1 | teilweise geklärt; Plan gesamt 1 statt 4 |
| [CAD-105](#cad-105) Y-Achse Kamera Halter | direkt | `y_camera_holder` | 1 | Fertigung spezifiziert |
| [CAD-107](#cad-107) Y-Achse Schlitten | direkt | `y_slide` | 1 | Fertigung spezifiziert |
| [CAD-108](#cad-108) Y-Achse Schlitten Abstand Stange | direkt | `y_slide_distance_rod` | 2 | Fertigung spezifiziert |
| [CAD-109](#cad-109) Y-Achse Schlitten Abstand Rohr 2 mm | direkt | `y_slide_distance_tube_2mm` | 1 | Fertigung spezifiziert |
| [CAD-112](#cad-112) Y-Achse Schlitten oben | direkt | `y_slide_top` | 1 | Fertigung spezifiziert |
| [CAD-113](#cad-113) GT2-Riemen Z, 9 mm breit | direkt | `z_drive_belt` | 1 | bestellfähig |

<a id="komp-08"></a>

## K08 y_slide_mirrored (1):1 – Y-Schlitten, gespiegelt

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-001](#cad-001) Y-Riemenklemme (CAD-Name TR10x 2 GT2 Adapter) | direkt | `TR10x2_GT2_belt_adapter` | 1 | Fertigung spezifiziert |
| [CAD-002](#cad-002) Y-Riemenklemme, Deckel | direkt | `TR10x2_GT2_belt_adapter_cover` | 1 | Fertigung spezifiziert |
| [CAD-029](#cad-029) DIN 562 M3 Vierkantmutter | direkt | `din_562_m3_square_nut` | 1 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-030](#cad-030) DIN 562 M4 Vierkantmutter | direkt | `din_562_m4_square_nut` | 3 | bestellfähig; Plan gesamt 14 statt 12 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 4 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-036](#cad-036) DIN 912 M3×12 | direkt | `din_912_m3x12` | 2 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-037](#cad-037) DIN 912 M3×14 | direkt | `din_912_m3x14` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-038](#cad-038) DIN 912 M3×16 | direkt | `din_912_m3x16` | 2 | bestellfähig; Plan gesamt 31 statt 28 |
| [CAD-040](#cad-040) DIN 912 M3×20 | direkt | `din_912_m3x20` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-041](#cad-041) DIN 912 M3×30 | direkt | `din_912_m3x30` | 2 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-042](#cad-042) DIN 912 M3×8 | direkt | `din_912_m3x8` | 4 | bestellfähig; Plan gesamt 58 statt 52 |
| [CAD-045](#cad-045) DIN 912 M4×30 | direkt | `din_912_m4x30` | 4 | bestellfähig; Plan gesamt 40 statt 36 |
| [CAD-054](#cad-054) HIWIN MGN12CZ0HM Z-Führungswagen | direkt | `hiwin_slide_MGN12CZ0H` | 1 | bestellfähig |
| [CAD-056](#cad-056) Sechskantmutter DIN 934 M3 A2 | direkt | `iso_8673_nut_m3` | 6 | bestellfähig; Plan gesamt 49 statt 44 |
| [CAD-057](#cad-057) Sechskantmutter DIN 934 M4 A2 | direkt | `iso_8673_nut_m4` | 6 | bestellfähig; Plan gesamt 71 statt 64 |
| [CAD-063](#cad-063) NEMA14 Z-Motor, ERSATZ: STEPPERONLINE 14HS13-0804S statt Nanotec ST3518M1004-A | direkt | `nanotec_nema_14_ST3518M1004-A` | 2 | bestellfähig; Plan gesamt 4 statt 8 |
| [CAD-065](#cad-065) Optischer Endschalter 11×35 mm | direkt | `optical_endstop` | 1 | bestellfähig |
| [CAD-076](#cad-076) GT2-Zahnscheibe Z16 / 9 mm / Bohrung 5 mm, ANPASSUNG | direkt | `pulley_gt2_9mm` | 2 | bestellfähig |
| [CAD-080](#cad-080) GleitbuchseØ10 innen / Ø19 außen / Länge 29 mm | direkt | `rod_slide_d10_l19` | 4 | bestellfähig |
| [CAD-085](#cad-085) Bewegliches USB-Mikroskop | direkt | `usb_microscope` | 1 | teilweise geklärt; Plan gesamt 1 statt 4 |
| [CAD-106](#cad-106) Y-Achse Kamera Halter kompakt | direkt | `y_camera_holder_compact` | 1 | Fertigung spezifiziert |
| [CAD-108](#cad-108) Y-Achse Schlitten Abstand Stange | direkt | `y_slide_distance_rod` | 2 | Fertigung spezifiziert |
| [CAD-109](#cad-109) Y-Achse Schlitten Abstand Rohr 2 mm | direkt | `y_slide_distance_tube_2mm` | 1 | Fertigung spezifiziert |
| [CAD-110](#cad-110) Y-Achse Schlitten gespiegelt | direkt | `y_slide_mirrored` | 1 | Fertigung spezifiziert |
| [CAD-111](#cad-111) Y-Achse Schlitten gespiegelt oben | direkt | `y_slide_mirrored_top` | 1 | Fertigung spezifiziert |
| [CAD-113](#cad-113) GT2-Riemen Z, 9 mm breit | direkt | `z_drive_belt` | 1 | bestellfähig |

<a id="komp-09"></a>

## K09 y_slide_mirrored (1):2 – Y-Schlitten, gespiegelt

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-001](#cad-001) Y-Riemenklemme (CAD-Name TR10x 2 GT2 Adapter) | direkt | `TR10x2_GT2_belt_adapter` | 1 | Fertigung spezifiziert |
| [CAD-002](#cad-002) Y-Riemenklemme, Deckel | direkt | `TR10x2_GT2_belt_adapter_cover` | 1 | Fertigung spezifiziert |
| [CAD-029](#cad-029) DIN 562 M3 Vierkantmutter | direkt | `din_562_m3_square_nut` | 1 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-030](#cad-030) DIN 562 M4 Vierkantmutter | direkt | `din_562_m4_square_nut` | 3 | bestellfähig; Plan gesamt 14 statt 12 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 4 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-036](#cad-036) DIN 912 M3×12 | direkt | `din_912_m3x12` | 2 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-037](#cad-037) DIN 912 M3×14 | direkt | `din_912_m3x14` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-038](#cad-038) DIN 912 M3×16 | direkt | `din_912_m3x16` | 2 | bestellfähig; Plan gesamt 31 statt 28 |
| [CAD-040](#cad-040) DIN 912 M3×20 | direkt | `din_912_m3x20` | 1 | bestellfähig; Plan gesamt 6 statt 4 |
| [CAD-041](#cad-041) DIN 912 M3×30 | direkt | `din_912_m3x30` | 2 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-042](#cad-042) DIN 912 M3×8 | direkt | `din_912_m3x8` | 4 | bestellfähig; Plan gesamt 58 statt 52 |
| [CAD-045](#cad-045) DIN 912 M4×30 | direkt | `din_912_m4x30` | 4 | bestellfähig; Plan gesamt 40 statt 36 |
| [CAD-054](#cad-054) HIWIN MGN12CZ0HM Z-Führungswagen | direkt | `hiwin_slide_MGN12CZ0H` | 1 | bestellfähig |
| [CAD-056](#cad-056) Sechskantmutter DIN 934 M3 A2 | direkt | `iso_8673_nut_m3` | 6 | bestellfähig; Plan gesamt 49 statt 44 |
| [CAD-057](#cad-057) Sechskantmutter DIN 934 M4 A2 | direkt | `iso_8673_nut_m4` | 6 | bestellfähig; Plan gesamt 71 statt 64 |
| [CAD-063](#cad-063) NEMA14 Z-Motor, ERSATZ: STEPPERONLINE 14HS13-0804S statt Nanotec ST3518M1004-A | direkt | `nanotec_nema_14_ST3518M1004-A` | 2 | bestellfähig; Plan gesamt 4 statt 8 |
| [CAD-065](#cad-065) Optischer Endschalter 11×35 mm | direkt | `optical_endstop` | 1 | bestellfähig |
| [CAD-076](#cad-076) GT2-Zahnscheibe Z16 / 9 mm / Bohrung 5 mm, ANPASSUNG | direkt | `pulley_gt2_9mm` | 2 | bestellfähig |
| [CAD-080](#cad-080) GleitbuchseØ10 innen / Ø19 außen / Länge 29 mm | direkt | `rod_slide_d10_l19` | 4 | bestellfähig |
| [CAD-085](#cad-085) Bewegliches USB-Mikroskop | direkt | `usb_microscope` | 1 | teilweise geklärt; Plan gesamt 1 statt 4 |
| [CAD-106](#cad-106) Y-Achse Kamera Halter kompakt | direkt | `y_camera_holder_compact` | 1 | Fertigung spezifiziert |
| [CAD-108](#cad-108) Y-Achse Schlitten Abstand Stange | direkt | `y_slide_distance_rod` | 2 | Fertigung spezifiziert |
| [CAD-109](#cad-109) Y-Achse Schlitten Abstand Rohr 2 mm | direkt | `y_slide_distance_tube_2mm` | 1 | Fertigung spezifiziert |
| [CAD-110](#cad-110) Y-Achse Schlitten gespiegelt | direkt | `y_slide_mirrored` | 1 | Fertigung spezifiziert |
| [CAD-111](#cad-111) Y-Achse Schlitten gespiegelt oben | direkt | `y_slide_mirrored_top` | 1 | Fertigung spezifiziert |
| [CAD-113](#cad-113) GT2-Riemen Z, 9 mm breit | direkt | `z_drive_belt` | 1 | bestellfähig |

<a id="komp-10"></a>

## K10 z_slide:1 – Z-Achse

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-029](#cad-029) DIN 562 M3 Vierkantmutter | direkt | `din_562_m3_square_nut` | 1 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 1 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-042](#cad-042) DIN 912 M3×8 | direkt | `din_912_m3x8` | 2 | bestellfähig; Plan gesamt 58 statt 52 |
| [CAD-053](#cad-053) HIWIN MGNR12R150HM, Z-Schiene 150 mm | direkt | `hiwin_rail_MGNR12R150HM` | 1 | bestellfähig |
| [CAD-073](#cad-073) Prüfkontakt-Hülse P75-2 W | direkt | `plug_sleeve_P75-2_W` | 1 | nicht identifiziert |
| [CAD-114](#cad-114) Z-Achse Antrieb Riemen Halter v 3 | direkt | `z_drive_belt_holder_v3` | 1 | Fertigung spezifiziert |
| [CAD-115](#cad-115) Federkontakt der Prüfspitze | direkt | `z_pogo_pin` | 1 | nicht identifiziert |
| [CAD-116](#cad-116) Z-Achse Prüfspitze Platine Halter | direkt | `z_probe_tip_pcb_holder` | 1 | Fertigung spezifiziert |
| [CAD-119](#cad-119) Z-Achse Schlitten Endschalter Auslöser | direkt | `z_slide_end_stop_trigger.psm` | 1 | Fertigung spezifiziert |
| [CAD-061](#cad-061) MMCX-Stecker gerade / Messleitung | `probe_tip` | `mmcx_male_end` | 2 | nicht identifiziert |
| [CAD-073](#cad-073) Prüfkontakt-Hülse P75-2 W | `probe_tip` | `plug_sleeve_P75-2_W` | 1 | nicht identifiziert |
| [CAD-075](#cad-075) Prüfspitzen-PCB, unbestückt | `probe_tip` | `probe_tip_pcb` | 1 | Fertigung noch offen |
| [CAD-115](#cad-115) Federkontakt der Prüfspitze | `probe_tip` | `z_pogo_pin` | 1 | nicht identifiziert |

<a id="komp-11"></a>

## K11 z_slide:2 – Z-Achse

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-029](#cad-029) DIN 562 M3 Vierkantmutter | direkt | `din_562_m3_square_nut` | 1 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 1 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-042](#cad-042) DIN 912 M3×8 | direkt | `din_912_m3x8` | 2 | bestellfähig; Plan gesamt 58 statt 52 |
| [CAD-053](#cad-053) HIWIN MGNR12R150HM, Z-Schiene 150 mm | direkt | `hiwin_rail_MGNR12R150HM` | 1 | bestellfähig |
| [CAD-073](#cad-073) Prüfkontakt-Hülse P75-2 W | direkt | `plug_sleeve_P75-2_W` | 1 | nicht identifiziert |
| [CAD-114](#cad-114) Z-Achse Antrieb Riemen Halter v 3 | direkt | `z_drive_belt_holder_v3` | 1 | Fertigung spezifiziert |
| [CAD-115](#cad-115) Federkontakt der Prüfspitze | direkt | `z_pogo_pin` | 1 | nicht identifiziert |
| [CAD-116](#cad-116) Z-Achse Prüfspitze Platine Halter | direkt | `z_probe_tip_pcb_holder` | 1 | Fertigung spezifiziert |
| [CAD-119](#cad-119) Z-Achse Schlitten Endschalter Auslöser | direkt | `z_slide_end_stop_trigger.psm` | 1 | Fertigung spezifiziert |
| [CAD-061](#cad-061) MMCX-Stecker gerade / Messleitung | `probe_tip` | `mmcx_male_end` | 2 | nicht identifiziert |
| [CAD-073](#cad-073) Prüfkontakt-Hülse P75-2 W | `probe_tip` | `plug_sleeve_P75-2_W` | 1 | nicht identifiziert |
| [CAD-075](#cad-075) Prüfspitzen-PCB, unbestückt | `probe_tip` | `probe_tip_pcb` | 1 | Fertigung noch offen |
| [CAD-115](#cad-115) Federkontakt der Prüfspitze | `probe_tip` | `z_pogo_pin` | 1 | nicht identifiziert |

<a id="komp-12"></a>

## K12 z_slide_long:1 – Z-Achse, lange Ausführung

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-029](#cad-029) DIN 562 M3 Vierkantmutter | direkt | `din_562_m3_square_nut` | 1 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 1 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-053](#cad-053) HIWIN MGNR12R150HM, Z-Schiene 150 mm | direkt | `hiwin_rail_MGNR12R150HM` | 1 | bestellfähig |
| [CAD-073](#cad-073) Prüfkontakt-Hülse P75-2 W | direkt | `plug_sleeve_P75-2_W` | 1 | nicht identifiziert |
| [CAD-114](#cad-114) Z-Achse Antrieb Riemen Halter v 3 | direkt | `z_drive_belt_holder_v3` | 1 | Fertigung spezifiziert |
| [CAD-115](#cad-115) Federkontakt der Prüfspitze | direkt | `z_pogo_pin` | 1 | nicht identifiziert |
| [CAD-117](#cad-117) Z-Achse Prüfspitze Platine Halter lang | direkt | `z_probe_tip_pcb_holder_long` | 1 | Fertigung spezifiziert |
| [CAD-118](#cad-118) Z-Achse Schlitten Kabel Halter | direkt | `z_slide_cable_holder` | 2 | Fertigung spezifiziert |
| [CAD-120](#cad-120) Z-Achse Schlitten Endschalter Auslöser gespiegelt | direkt | `z_slide_end_stop_trigger_mirrored.psm` | 1 | Fertigung spezifiziert |
| [CAD-062](#cad-062) MMCX-Stecker gewinkelt / Messleitung | `probe_tip_with_angle` | `mmcx_male_end_with_angle` | 2 | nicht identifiziert |
| [CAD-073](#cad-073) Prüfkontakt-Hülse P75-2 W | `probe_tip_with_angle` | `plug_sleeve_P75-2_W` | 1 | nicht identifiziert |
| [CAD-075](#cad-075) Prüfspitzen-PCB, unbestückt | `probe_tip_with_angle` | `probe_tip_pcb` | 1 | Fertigung noch offen |
| [CAD-115](#cad-115) Federkontakt der Prüfspitze | `probe_tip_with_angle` | `z_pogo_pin` | 1 | nicht identifiziert |

<a id="komp-13"></a>

## K13 z_slide_long:2 – Z-Achse, lange Ausführung

| ID / Teil | Unterbaugruppe | CAD-Name | Stück | Status |
| --- | --- | --- | --- | --- |
| [CAD-029](#cad-029) DIN 562 M3 Vierkantmutter | direkt | `din_562_m3_square_nut` | 1 | bestellfähig; Plan gesamt 10 statt 8 |
| [CAD-035](#cad-035) DIN 912 M3×10 | direkt | `din_912_m3x10` | 1 | bestellfähig; Plan gesamt 84 statt 76 |
| [CAD-053](#cad-053) HIWIN MGNR12R150HM, Z-Schiene 150 mm | direkt | `hiwin_rail_MGNR12R150HM` | 1 | bestellfähig |
| [CAD-073](#cad-073) Prüfkontakt-Hülse P75-2 W | direkt | `plug_sleeve_P75-2_W` | 1 | nicht identifiziert |
| [CAD-114](#cad-114) Z-Achse Antrieb Riemen Halter v 3 | direkt | `z_drive_belt_holder_v3` | 1 | Fertigung spezifiziert |
| [CAD-115](#cad-115) Federkontakt der Prüfspitze | direkt | `z_pogo_pin` | 1 | nicht identifiziert |
| [CAD-117](#cad-117) Z-Achse Prüfspitze Platine Halter lang | direkt | `z_probe_tip_pcb_holder_long` | 1 | Fertigung spezifiziert |
| [CAD-118](#cad-118) Z-Achse Schlitten Kabel Halter | direkt | `z_slide_cable_holder` | 2 | Fertigung spezifiziert |
| [CAD-120](#cad-120) Z-Achse Schlitten Endschalter Auslöser gespiegelt | direkt | `z_slide_end_stop_trigger_mirrored.psm` | 1 | Fertigung spezifiziert |
| [CAD-062](#cad-062) MMCX-Stecker gewinkelt / Messleitung | `probe_tip_with_angle` | `mmcx_male_end_with_angle` | 2 | nicht identifiziert |
| [CAD-073](#cad-073) Prüfkontakt-Hülse P75-2 W | `probe_tip_with_angle` | `plug_sleeve_P75-2_W` | 1 | nicht identifiziert |
| [CAD-075](#cad-075) Prüfspitzen-PCB, unbestückt | `probe_tip_with_angle` | `probe_tip_pcb` | 1 | Fertigung noch offen |
| [CAD-115](#cad-115) Federkontakt der Prüfspitze | `probe_tip_with_angle` | `z_pogo_pin` | 1 | nicht identifiziert |

<a id="komp-14"></a>

## K14 Nicht im CAD-Modell – Systemteile ohne CAD-Körper

| ID / Teil | Planmenge | Beschaffungsart | Status |
| --- | --- | --- | --- |
| [SYS-001](#sys-001) TMC2130 SPI Treibermodule | 16 Stück | Kaufteile | teilweise geklärt |
| [SYS-002](#sys-002) Stationäre Übersichtskamera | 1 Stück | Kaufteile | teilweise geklärt |
| [SYS-003](#sys-003) Signal-Multiplexer, unbestückte Leiterplatte | 1 Stück | PCB extern | Fertigung noch offen |
| [SYS-004](#sys-004) Kalibrier-Referenzkörper / Platte | 1 Stück | 3D-Druck intern | Fertigung noch offen |
| [SYS-005](#sys-005) Innere Messing-Referenzzylinder | 4 Stück | Weitere Fertigung | Fertigung noch offen |
| [SYS-006](#sys-006) Kalibriermarker / matte Druckvorlage | 1 Satz | Weitere Fertigung | Fertigung noch offen |
| [SYS-007](#sys-007) Weißer 24-V-LED-Streifen | 2 m | Kaufteile | teilweise geklärt |
| [SYS-008](#sys-008) LED-Aluprofile, Diffusoren, Kappen, Halter | 2 m | Kaufteile | teilweise geklärt |
| [SYS-009](#sys-009) LED-Anschluss an vorhan denen SKR-Ausgang | 1 Satz | Kaufteile | teilweise geklärt |
| [SYS-010](#sys-010) USB-Hub 7Port aktiv | 1 Stück | Kaufteile | teilweise geklärt |
| [SYS-011](#sys-011) USB-Kabel für 4 SKR | 4 Stück | Kaufteile | teilweise geklärt |
| [SYS-012](#sys-012) USB-Kabel für MUX/UART/Zielversorgung | 3 Stück | Kaufteile | teilweise geklärt |
| [SYS-013](#sys-013) Bewegliche Kameraleitung / USB-Verlängerung | 1 Stück | Kaufteile | teilweise geklärt |
| [SYS-014](#sys-014) Motorleitungen 4adrig | 32 m | Kaufteile | teilweise geklärt |
| [SYS-015](#sys-015) Motor-Gegenstecker und Crimpkontakte | 32 Satz | Kaufteile | teilweise geklärt |
| [SYS-016](#sys-016) Sensorleitungen / Verlängerungen | 24 Stück | Kaufteile | teilweise geklärt |
| [SYS-017](#sys-017) Sensor-Gegenstecker und Kontakte | 28 Satz | Kaufteile | teilweise geklärt |
| [SYS-018](#sys-018) 24-V-Verteilung, Sicherungen, Klemmen, Leitungen | 1 Satz | Kaufteile | teilweise geklärt |
| [SYS-019](#sys-019) Sensor-Pegelanpassung / Eingangsschutz | 24 Kanäle | PCB extern | Fertigung noch offen |
| [SYS-020](#sys-020) Netzeinspeisung, Leitung, Sicherung und Zugentlastung | 1 Satz | Kaufteile | teilweise geklärt |
| [SYS-021](#sys-021) Schutzleiter, Ringkabelschuhe und Klemmenabdeckung | 1 Satz | Kaufteile | teilweise geklärt |
| [SYS-022](#sys-022) Messkoax und instrumentenseitige Adapter | 4 Kanäle | Kaufteile | teilweise geklärt |
| [SYS-023](#sys-023) Signal-Multiplexer Bestückung | 1 Baugruppe | PCB extern | Fertigung noch offen |
| [SYS-024](#sys-024) Prüfspitzen-PCB Bestückung | 4 Baugruppen | PCB extern | Fertigung noch offen |
| [SYS-025](#sys-025) USB-UART-Adapter | 1 Stück | Kaufteile | teilweise geklärt |
| [SYS-026](#sys-026) Zielplatinen-Versorgungscontroller | 1 Baugruppe | PCB extern | Fertigung noch offen |
| [SYS-027](#sys-027) Energieketten-Endanschlüsse schmal | 16 Sätze | Kaufteile | teilweise geklärt |
| [SYS-028](#sys-028) Energieketten-Endanschlüsse breit | 8 Sätze | Kaufteile | teilweise geklärt |
| [SYS-029](#sys-029) Profil-Nutensteine und Zusatzbefestigung | 1 Satz | Kaufteile | teilweise geklärt |
| [SYS-030](#sys-030) Scheiben, Sicherungselemente, Distanzteile | 1 Satz | Kaufteile | teilweise geklärt |
| [SYS-031](#sys-031) Lötzinn, Schrumpfschlauch, Binder, Labels, Kleber | 1 Satz | Kaufteile | teilweise geklärt |
| [SYS-032](#sys-032) Controller-Befestigung und Kühlung | 1 Satz | Kaufteile | teilweise geklärt |
| [SYS-033](#sys-033) Zusätzliche bewegliche Kameras | 3 Stück | Optional | teilweise geklärt |
| [SYS-034](#sys-034) Host-PC, Messgeräte und Werkzeuge | 1 Bestand | Nicht benötigt | nicht benötigt |
| [SYS-035](#sys-035) Z-Antriebsriemenscheibe / integrierter Adapter | 0 Stück | Nicht benötigt | nicht benötigt |
| [SYS-036](#sys-036) USB-/Versorgungsanschlüsse der Kalibrierung | 1 Prüfung | Nicht benötigt | nicht benötigt |
| [SYS-037](#sys-037) Weiße äußere Kalibrierreferenzen | 4 Stück | Weitere Fertigung | Fertigung noch offen |
| [SYS-038](#sys-038) Kalibrier-Kontaktleitungen und gemeinsame Messreferenz | 1 Satz | Kaufteile | teilweise geklärt |
| [SYS-039](#sys-039) Erhöhte Messing-Referenzzylinder | 4 Stück | Weitere Fertigung | Fertigung noch offen |
| [SYS-040](#sys-040) Äußere flache Messing-Referenzzylinder | 4 Stück | Weitere Fertigung | Fertigung noch offen |
| [SYS-041](#sys-041) Nutenstein I-Typ Nut 6, M6, Motorplatten | 8 Stück | Kaufteile | bestellfähig |
| [SYS-042](#sys-042) Nutenstein I-Typ Nut 6, M4, Rückwand | 6 Stück | Kaufteile | bestellfähig |
| [SYS-043](#sys-043) Zylinderschraube DIN 912 M4×10 A2, Rückwand | 6 Stück | Kaufteile | bestellfähig |
| [SYS-044](#sys-044) Nutenstein I-Typ Nut 6, M5, Griff | 2 Stück | Kaufteile | bestellfähig |
| [SYS-045](#sys-045) Zylinderschraube DIN 912 M5×35 A2, Griff | 2 Stück | Kaufteile | bestellfähig |
| [SYS-046](#sys-046) Zylinderschraube DIN 912 M4×10 A2, Wellenhalter | 7 Stück | Kaufteile | bestellfähig |
| [SYS-047](#sys-047) Nutenstein I-Typ Nut 6, M4, Wellenhalter | 8 Stück | Kaufteile | bestellfähig |
| [SYS-048](#sys-048) Linsenkopfschraube ISO 7380-1 M4×8 A2, Teleskopschienen | 12 Stück | Kaufteile | bestellfähig |
| [SYS-049](#sys-049) Nutenstein I-Typ Nut 6, M4, Teleskopschienen | 12 Stück | Kaufteile | bestellfähig |
| [SYS-050](#sys-050) Zylinderschraube DIN 912 M3×8 A2, Kabelhalter M3 | 4 Stück | Kaufteile | bestellfähig |
| [SYS-051](#sys-051) Zylinderschraube DIN 912 M3×10 A2, igus-Kettenanschlüsse | 106 Stück | Kaufteile | bestellfähig |
| [SYS-052](#sys-052) Zylinderschraube DIN 912 M3×12 A2, Z-Kabelhalter | 6 Stück | Kaufteile | bestellfähig |
| [SYS-053](#sys-053) Sechskantmutter DIN 934 M3 A2, Kabelführung | 111 Stück | Kaufteile | bestellfähig |
| [SYS-054](#sys-054) Linsenkopfschraube ISO 7380-1 M4×8 A2, Kabelführung | 11 Stück | Kaufteile | bestellfähig |
| [SYS-055](#sys-055) Nutenstein I-Typ Nut 6, M4, Kabelhalter | 3 Stück | Kaufteile | bestellfähig |
| [SYS-056](#sys-056) Zylinderschraube DIN 912 M5×10 A2, Kabelhalter M5 | 6 Stück | Kaufteile | bestellfähig |

# Details nach Beschaffungsart

## Kaufteile

| ID / Teil | CAD / Fusion / Plan | Status | Geometrie / Werkstoff | Quelle und konkreter Klärbedarf |
| --- | --- | --- | --- | --- |
| <a id="cad-023"></a>**CAD-023** BIGTREETECH SKR V1.3 Steuerplatine<br>`bigtreetech_skr_v1_3` | 4 / 4 / **4 Stück** | teilweise geklärt | 109.67 x 1.55 x 84.3; nicht belegt | Original laut CAD, Firmware und Masterarbeit. Neu in DE/EU nicht gefunden (Recherche 17.10.2026). Kandidat SKR 1.4 Turbo (RBS13645) passt auf fast dieselben Löcher, braucht aber Marlin-Pinanpassung; nicht freigegeben.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-016` |
| <a id="cad-027"></a>**CAD-027** CPC MR12ML Führungswagen<br>`cpc_MR12ML` | 8 / 8 / **8 Stück** | bestellfähig | 47.6 x 10.0 x 27.0; nicht belegt | 8 Wagen MR12MLSSV0N für 2×600-mm-Schienen. CPC-Katalog SS-Ausführung: L 47,6, Körperhöhe 10, Breite 27, Lochbild 20×20 M3 = CAD und Fusion-Messung. Lieferbarkeit bei Motedis prüfen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-018` |
| <a id="cad-028"></a>**CAD-028** DIN 466 Rändelmutter hoch M4<br>`din_466_knurled_nut_high_m4` | 8 / 8 / **10 Stück** | bestellfähig | 16.0 x 16.0 x 9.5; Edelstahl A1; A2 in DIN 466 nicht gefunden | Norm und Maße mit CAD abgeglichen; Artikel OS-466-1-040. DIN 466 M4: dk 16, m 9,5 = CAD. Nur A1 statt A2 lieferbar. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-028` |
| <a id="cad-029"></a>**CAD-029** DIN 562 M3 Vierkantmutter<br>`din_562_m3_square_nut` | 8 / 8 / **10 Stück** | bestellfähig | 5.5 x 1.8 x 5.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-562-2-0030. DIN 562 M3: s 5,5, m 1,8 = CAD. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-029` |
| <a id="cad-030"></a>**CAD-030** DIN 562 M4 Vierkantmutter<br>`din_562_m4_square_nut` | 12 / 12 / **14 Stück** | bestellfähig | 7.0 x 2.2 x 7.0; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-562-2-0040. DIN 562 M4: s 7, m 2,2 = CAD. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-030` |
| <a id="cad-031"></a>**CAD-031** DIN 7991 M3×8<br>`din_7991_m3x8` | 32 / 32 / **36 Stück** | bestellfähig | 8.0 x 6.0 x 6.0; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-7991-2-030008. Blankes A2; Schrauben.Expert nur schwarz. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-031` |
| <a id="cad-032"></a>**CAD-032** DIN 7991 M6×12<br>`din_7991_m6x12` | 16 / 16 / **18 Stück** | bestellfähig | 12.0 x 12.0 x 12.0; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 7991 6 12 A2. ISO 10642 = DIN 7991; Kopf Ø13,44. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-032` |
| <a id="cad-033"></a>**CAD-033** DIN 7991 M6×14<br>`din_7991_m6x14` | 6 / 6 / **8 Stück** | bestellfähig | 14.0 x 12.0 x 12.0; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 7991 6 14 A2. ISO 10642 = DIN 7991. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-033` |
| <a id="cad-034"></a>**CAD-034** DIN 7991 M6×20<br>`din_7991_m6x20` | 22 / 22 / **25 Stück** | bestellfähig | 20.0 x 12.0 x 12.0; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 7991 6 20 A2. ISO 10642 = DIN 7991. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-034` |
| <a id="cad-035"></a>**CAD-035** DIN 912 M3×10<br>`din_912_m3x10` | 76 / 76 / **84 Stück** | bestellfähig | 13.0 x 5.5 x 5.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-912-2-030010. Blankes A2. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-035` |
| <a id="cad-036"></a>**CAD-036** DIN 912 M3×12<br>`din_912_m3x12` | 8 / 8 / **10 Stück** | bestellfähig | 15.0 x 5.5 x 5.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-912-2-030012. Blankes A2. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-036` |
| <a id="cad-037"></a>**CAD-037** DIN 912 M3×14<br>`din_912_m3x14` | 4 / 4 / **6 Stück** | bestellfähig | 17.0 x 5.5 x 5.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-912-2-030014. Blankes A2; 100 Stück günstiger als 6. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-037` |
| <a id="cad-038"></a>**CAD-038** DIN 912 M3×16<br>`din_912_m3x16` | 28 / 28 / **31 Stück** | bestellfähig | 19.0 x 5.5 x 5.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-912-2-030016. Blankes A2. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-038` |
| <a id="cad-039"></a>**CAD-039** DIN 912 M3×18<br>`din_912_m3x18` | 32 / 32 / **36 Stück** | bestellfähig | 21.0 x 5.5 x 5.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-912-2-030018. Blankes A2. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-039` |
| <a id="cad-040"></a>**CAD-040** DIN 912 M3×20<br>`din_912_m3x20` | 4 / 4 / **6 Stück** | bestellfähig | 23.0 x 5.5 x 5.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-912-2-030020. Blankes A2. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-040` |
| <a id="cad-041"></a>**CAD-041** DIN 912 M3×30<br>`din_912_m3x30` | 8 / 8 / **10 Stück** | bestellfähig | 33.0 x 5.5 x 5.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-912-2-030030. Blankes A2. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-041` |
| <a id="cad-042"></a>**CAD-042** DIN 912 M3×8<br>`din_912_m3x8` | 52 / 52 / **58 Stück** | bestellfähig | 11.0 x 5.5 x 5.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel OS-912-2-030008. Blankes A2. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-042` |
| <a id="cad-043"></a>**CAD-043** DIN 912 M4×10<br>`din_912_m4x10` | 1 / 1 / **3 Stück** | bestellfähig | 14.0 x 7.0 x 7.0; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 912 4 10 A2. Kopf Ø7, k 4. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-043` |
| <a id="cad-044"></a>**CAD-044** DIN 912 M4×20<br>`din_912_m4x20` | 20 / 20 / **22 Stück** | bestellfähig | 24.0 x 7.0 x 7.0; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 912 4 20 A2. 25 Stück günstiger als 22. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-044` |
| <a id="cad-045"></a>**CAD-045** DIN 912 M4×30<br>`din_912_m4x30` | 36 / 36 / **40 Stück** | bestellfähig | 34.0 x 7.0 x 7.0; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 912 4 30 A2. 50 Stück günstiger als 40. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-045` |
| <a id="cad-046"></a>**CAD-046** DIN 912 M5×10<br>`din_912_m5x10` | 32 / 32 / **36 Stück** | bestellfähig | 15.0 x 8.5 x 8.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 912 5 10 A2. 50 Stück günstiger als 36. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-046` |
| <a id="cad-047"></a>**CAD-047** DIN 912 M5×14<br>`din_912_m5x14` | 4 / 4 / **6 Stück** | bestellfähig | 19.0 x 8.5 x 8.5; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 912 5 14 A2. Preisstaffel: Kaufmenge = günstigste Staffel ≥ Planmenge. Festigkeitsklasse A2-70 nicht ausgewiesen. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-047` |
| <a id="cad-048"></a>**CAD-048** DIN 933 M4×20<br>`din_933_m4x20` | 8 / 8 / **10 Stück** | bestellfähig | 7.0 x 21.4 x 8.083; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 933 4 20 A2. SW 7, Vollgewinde. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-048` |
| <a id="cad-049"></a>**CAD-049** igus E2i.10.10.028.0, 16 kurze Abschnitte<br>`drag_chain_0_24m_E2i_10_10_028_0_4` | 16 / 16 / **16 Stück** | bestellfähig | 193.0 x 17.8 x 71.0; nicht belegt | Teilung 20 mm, Außenbreite 17,4, Einbauhöhe 71 bei R28 = CAD. 0,24 m = 12 Glieder, zusammen 192 Glieder. Anschlüsse siehe SYS-027.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-008` |
| <a id="cad-050"></a>**CAD-050** igus E2i.10.20.028.0, 8 lange Abschnitte<br>`drag_chain_0_28m_E2i_10_20_028_0_igus` | 8 / 8 / **8 Stück** | bestellfähig | 248.0 x 27.8 x 71.0; nicht belegt | Teilung 20 mm, Außenbreite 27,4, Einbauhöhe 71 = CAD. 0,28 m = 14 Glieder, zusammen 112 Glieder. Anschlüsse siehe SYS-028.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-023` |
| <a id="cad-051"></a>**CAD-051** Schubladengriff DOLD A-75873, Lochabstand 100 mm<br>`handle_l100_dold` | 1 / 1 / **1 Stück** | bestellfähig | 113.0 x 20.0 x 49.0; nicht belegt | Fusion-Messung: Bohrungen Ø5,5 durchgehend (29 mm) = Variante mit Befestigungsbohrungen A-75873 (Ø5,4, 112 statt 113 mm lang). Entscheidung Luis 17.10.2026. Befestigung SYS-044/045.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-C051` |
| <a id="cad-052"></a>**CAD-052** Gelenkfuß M6×20 / Teller Ø40 mm<br>`hinged_M6_40_dold` | 4 / 4 / **4 Stück** | bestellfähig | 40.0 x 40.0 x 30.4; nicht belegt | DOLD GF-K-10-PA-028: M6, Teller Ø40 = CAD; Fusion-Messung Gewindelänge 20 mm = Variante M6×20. Traglast vom Händler nicht angegeben.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-C052` |
| <a id="cad-053"></a>**CAD-053** HIWIN MGNR12R150HM, Z-Schiene 150 mm<br>`hiwin_rail_MGNR12R150HM` | 4 / 4 / **4 Stück** | bestellfähig | 12.0 x 150.0 x 8.0; nicht belegt | HIWIN-Katalog: 12×8, Teilung 25, Bohrung Ø3,5/Ø6; 150 mm mit 6 Bohrungen und Endabstand 12,5 = Fusion-Messung. Bezug Damen CNC (NL), Zuschnitt.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-020` |
| <a id="cad-054"></a>**CAD-054** HIWIN MGN12CZ0HM Z-Führungswagen<br>`hiwin_slide_MGN12CZ0H` | 4 / 4 / **4 Stück** | bestellfähig | 27.0 x 35.688 x 10.0; nicht belegt | Bestellschlüssel: Z0 spielfrei, H hohe Genauigkeit, M Edelstahl. Breite 27, Körperhöhe 10, Lochbild 20×15 M3 = CAD; Katalog-Länge 34,7 statt CAD 35,7.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-021` |
| <a id="cad-056"></a>**CAD-056** Sechskantmutter DIN 934 M3 A2<br>`iso_8673_nut_m3` | 44 / 44 / **49 Stück** | bestellfähig | 5.5 x 2.4 x 6.351; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 934 3 A2. SW 5,5, H 2,4 = CAD; ISO 4032 identisch. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026). CAD-Name ISO 8673 ist ein Bibliotheksfehler: ISO 8673 beginnt erst bei M8, die CAD-Maße entsprechen ISO 4032/DIN 934.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-056` |
| <a id="cad-057"></a>**CAD-057** Sechskantmutter DIN 934 M4 A2<br>`iso_8673_nut_m4` | 64 / 64 / **71 Stück** | bestellfähig | 7.0 x 3.2 x 8.083; Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen | Norm und Maße mit CAD abgeglichen; Artikel 934 4 A2. SW 7, H 3,2 = CAD; ISO 4032 identisch. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026). CAD-Name ISO 8673 ist ein Bibliotheksfehler: ISO 8673 beginnt erst bei M8, die CAD-Maße entsprechen ISO 4032/DIN 934.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-057` |
| <a id="cad-058"></a>**CAD-058** ISO 8673 Mutter M8<br>`iso_8673_nut_m8` | 48 / 48 / **53 Stück** | teilweise geklärt | 13.0 x 6.8 x 15.011; Edelstahl A4-80 statt A2; A2 in M8×1 nicht gefunden | Norm und Maße mit CAD abgeglichen; Artikel 24122 08 1. A4 statt A2; H 6,5 statt 6,8. Datenblatt nennt Linksgewinde, vermutlich Datenfehler: vor Bestellung klären. Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026). ISO 8673 M8×1 passt zu den M8×1-Gewinden der induktiven Sensoren. Sensoren liefern meist 2 Muttern mit; dann nur Reserve kaufen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `N-058` |
| <a id="cad-059"></a>**CAD-059** Mean Well MHS012 Montagewinkel<br>`mean_well_MHS-012_mounting_bracket` | 4 / 4 / **4 Stück** | bestellfähig | 16.0 x 15.0 x 19.2; nicht belegt | 4 Winkel für RSP-200. Mean-Well-Zeichnung 15×16,2×19,5 mm = CAD (Abweichung höchstens 0,3 mm). Reichelt MHS-012.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-C059` |
| <a id="cad-060"></a>**CAD-060** Mean Well RSP-200-24 Netzteil,24 V/8,4 A<br>`mean_well_RSP-200-24` | 1 / 1 / **1 Stück** | bestellfähig | 115.0 x 30.0 x 215.0; nicht belegt | Originalmodell,215×115×30 mm. Lastbilanz, Absicherung, Berührungsschutz und Schutzleiter separat.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-001` |
| <a id="cad-063"></a>**CAD-063** NEMA14 Z-Motor, ERSATZ: STEPPERONLINE 14HS13-0804S statt Nanotec ST3518M1004-A<br>`nanotec_nema_14_ST3518M1004-A` | 8 / 8 / **4 Stück** | bestellfähig | 35.0 x 65.0 x 60.0; nicht belegt | ORIGINALMOTOR AUSGETAUSCHT (Entscheidung Luis 17.10.2026). Original nur im Nanotec-Archiv. Ersatz 34,8 mm statt 36 mm lang, Welle Ø5×24 mit D-Abflachung, 0,8 A statt 1,0 A, 18 statt 14 Ncm, Litzen ohne Stecker. Motorstrom in der Firmware auf 0,8 A begrenzen. Fusion-Messung: nur 2,8 mm Luft zum Endschalter, kürzerer Motor passt.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-015` |
| <a id="cad-064"></a>**CAD-064** Nanotec ST4118M1804-A NEMA17 X/Y-Motor<br>`nanotec_nema_17_ST4118M1804-A` | 12 / 0 / **12 Stück** | bestellfähig | offen; nicht belegt | Originalmodell, aktuelle Nanotec-Serie: 1,8 A, 0,28 Nm, 38 mm, Welle Ø5×24, Litzen 300 mm mit JST XHP-4. 12 laut STEP (8 X + 4 Y), im Fusion-Import fehlend. Verfügbarkeit beim Hersteller anfragen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-014` |
| <a id="cad-065"></a>**CAD-065** Optischer Endschalter 11×35 mm<br>`optical_endstop` | 4 / 4 / **4 Stück** | bestellfähig | 35.0 x 11.0 x 11.7; nicht belegt | RBS12901: 35×11 mm und Lochabstand 28 mm stimmen mit der Fusion-Messung überein. VCC/GND/SIG, 2,7–5 V, HIGH bei Unterbrechung. Pinfolge am SKR-Stecker vor dem Anschluss prüfen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-009` |
| <a id="cad-076"></a>**CAD-076** GT2-Zahnscheibe Z16 / 9 mm / Bohrung 5 mm, ANPASSUNG<br>`pulley_gt2_9mm` | 8 / 8 / **8 Stück** | bestellfähig | 11.0 x 18.0 x 18.0; nicht belegt | Exaktes Teil (Ø18×11) in der EU nicht lieferbar. RBS12867 (Ø13×19,5, für 10-mm-Riemen) wird verwendet; Y-Schlitten-Druckteil und Umlenkachse müssen angepasst werden (Entscheidung Luis 17.10.2026). Fusion-Messung: Umlenkscheibe hat nur 3 mm Luft zum Schlitten.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-006` |
| <a id="cad-077"></a>**CAD-077** GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm<br>`pulley_gt2_z16_6mm` | 12 / 12 / **12 Stück** | bestellfähig | 14.1 x 13.0 x 13.0; nicht belegt | 12 X/Y-Antriebe. RBS10278: Bordscheibe Ø14 statt CAD Ø13; Fusion-Messung zeigt 4,6 mm Abstand zum nächsten Teil, passt.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-004` |
| <a id="cad-078"></a>**CAD-078** GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm<br>`return_pulley_gt2_z16_6mm` | 20 / 20 / **20 Stück** | bestellfähig | 8.5 x 13.0 x 13.0; nicht belegt | 20 Stück. Tinytronics 002225: Bohrung 3, Ø13, Breite 8,5 mm = CAD exakt (Rollen sitzen paarweise ohne Luft zwischen den Spannerflügeln).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-005` |
| <a id="cad-079"></a>**CAD-079** SHF10 Flanschhalter fürØ10 mm Welle<br>`rod_holder_flange_d10_dold` | 16 / 16 / **16 Stück** | bestellfähig | 10.0 x 24.0 x 43.0; nicht belegt | 16 Stück.43×24×10 mm undØ5,5-Befestigung stimmen mit DOLD11260 überein. Liefertermin 27.11.2026 angekündigt.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-003` |
| <a id="cad-080"></a>**CAD-080** GleitbuchseØ10 innen / Ø19 außen / Länge 29 mm<br>`rod_slide_d10_l19` | 16 / 16 / **16 Stück** | bestellfähig | 29.0 x 19.0 x 19.0; nicht belegt | igus RJ4JP-01-10: d 10, D 19, B 29, Nut Ø18 = CAD und Fusion-Messung. iglidur J4, LM10UU-Bauform.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-022` |
| <a id="cad-081"></a>**CAD-081** Anschraubwinkel 30 / Nut 6<br>`screw_on_bracket_30_6` | 26 / 26 / **26 Stück** | bestellfähig | 28.0 x 28.0 x 28.0; nicht belegt | DOLD 62378 (I-Typ Nut 6) 28×28×28 = CAD; bestellt als Satz 62385-BS mit Schrauben und Nutensteinen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-C081` |
| <a id="cad-084"></a>**CAD-084** Teleskopschiene 350 mm, Vollauszug<br>`telescopic_bar_tsaa514613-350` | 2 / 2 / **2 Stück** | bestellfähig | 45.5 x 12.7 x 350.0; nicht belegt | DOLD HS-4613-350 (CAD-Name enthält 4613): 350×45,7×12,7 (CAD 45,5), 1 Paar = die 2 CAD-Schienen. Vollauszug 354 mm.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-C084` |
| <a id="cad-085"></a>**CAD-085** Bewegliches USB-Mikroskop<br>`usb_microscope` | 4 / 4 / **1 Stück** | teilweise geklärt | 108.0 x 60.0 x 36.0; nicht belegt | Plan 1 laut Hardware-Blog,4CAD. Weitere 3 optional. Originalmodell unbekannt; Kandidat muss 100 mm Arbeitsabstand/ca 30×40 mm Bildfeld und Linux-UVC erfüllen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-011` |
| <a id="cad-087"></a>**CAD-087** GT2-Riemen X, 6 mm breit<br>`x_belt` | 8 / 8 / **8 Stück** | bestellfähig | 710.3 x 6.0 x 11.3; nicht belegt | 8 Verläufe, offen mit Spanner an beiden Enden. Fusion-Messung: 699 mm Trum, Teillänge 1.430 mm je Verlauf; Zuschnitt mit 2×40 mm Klemmzugabe ca. 1,51 m. Summe X+Y ca. 16,5 m aus zwei 10-m-Rollen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-007` |
| <a id="cad-095"></a>**CAD-095** CPC MR12M Führungsschiene 600 mm<br>`x_guiding_cpc_MR12M` | 2 / 2 / **2 Stück** | bestellfähig | 600.0 x 7.5 x 12.0; nicht belegt | 2 Stück MR12M-N-600: 12×7,5 mm, Teilung 25, 24 Bohrungen Ø3,5/Ø6, Endabstand 12,5 = CAD. Nicht mit HIWIN MGN mischen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-019` |
| <a id="cad-104"></a>**CAD-104** GT2-Riemen Y, 6 mm breit<br>`y_belt` | 4 / 4 / **4 Stück** | bestellfähig | 503.3 x 6.0 x 11.3; nicht belegt | 4 Verläufe. Fusion-Messung: 492 mm Trum, Teillänge 1.016 mm; Zuschnitt mit 2×40 mm Klemmzugabe ca. 1,10 m. Einkauf gemeinsam mit CAD-087, nicht doppelt rechnen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-007` |
| <a id="cad-113"></a>**CAD-113** GT2-Riemen Z, 9 mm breit<br>`z_drive_belt` | 4 / 4 / **4 Stück** | bestellfähig | 11.3 x 9.0 x 119.3; nicht belegt | 4 Verläufe, offen am Z-Riemenhalter geklemmt. Fusion-Messung: Achsabstand 108 mm, Teillänge 248 mm; Zuschnitt mit 2×35 mm Klemmzugabe ca. 0,32 m, zusammen 1,3 m. RBS14040 als Meterware.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-017` |
| <a id="sys-001"></a>**SYS-001** TMC2130 SPI Treibermodule | – / – / **16 Stück** | teilweise geklärt | offen; nicht belegt | 4 je SKR für X/X2/Y/Z. RBS13024: 4 Treiber mit Kühlkörpern und Kabel, SPI-Pins laut Fotos vorgelötet. Revision nicht angegeben; SPI-Modus laut Datenblatt per Lötbrücke CFG4/CFG5 prüfen.<br>[Beleg](../firmware/Marlin/Configuration.h); Kostenzeile `BUY-002` |
| <a id="sys-002"></a>**SYS-002** Stationäre Übersichtskamera | – / – / **1 Stück** | teilweise geklärt | offen; nicht belegt | 1080p-Softwarekonfiguration; Optik, Blickfeld und Halterpassung offen.<br>[Beleg](https://www.schutzwerk.com/en/blog/proboter-02/); Kostenzeile `BUY-010` |
| <a id="sys-007"></a>**SYS-007** Weißer 24-V-LED-Streifen | – / – / **2 m** | teilweise geklärt | offen; nicht belegt | 2 m vorläufig;5 m-Rolle. Weiß 4500K vorgeschlagen; Leistung, Flimmern und Lichtverteilung testen.<br>[Beleg](https://www.schutzwerk.com/en/blog/proboter-02/); Kostenzeile `BUY-013` |
| <a id="sys-008"></a>**SYS-008** LED-Aluprofile, Diffusoren, Kappen, Halter | – / – / **2 m** | teilweise geklärt | offen; nicht belegt | 8 mm-Streifen aufnehmen, Wärmeabfuhr und Befestigung; genaue Aufteilung/Menge offen. Keine Doppelrechnung als Band.<br>[Beleg](https://www.schutzwerk.com/en/blog/proboter-02/); Kostenzeile `BUD-S008` |
| <a id="sys-009"></a>**SYS-009** LED-Anschluss an vorhan denen SKR-Ausgang | – / – / **1 Satz** | teilweise geklärt | offen; nicht belegt | Configuration_adv.h:4396 setzt PROBOTER_LIGHT_CONTROL_PIN auf HEATER_BED_PIN; M376 steuert Helligkeit. Kein separater USB-LED-Controller nötig. Stecker/Leitungen, Strom und Flimmern prüfen; keine zusätzliche MOSFET-Platine pauschal kaufen.<br>[Beleg](../firmware/Marlin/Configuration_adv.h); Kostenzeile `OPEN-SYS-009` |
| <a id="sys-010"></a>**SYS-010** USB-Hub 7Port aktiv | – / – / **1 Stück** | teilweise geklärt | offen; nicht belegt | Steuergeräte am Hub; zwei separate Kamera-Hostports vorausgesetzt. Netzteil und Hubkabel enthalten.<br>[Beleg](../software/hardware-control/proboter/cli.py); Kostenzeile `BUY-012` |
| <a id="sys-011"></a>**SYS-011** USB-Kabel für 4 SKR | – / – / **4 Stück** | teilweise geklärt | offen; nicht belegt | Host USB-A auf Board USB-B bestätigen; Länge vorläufig 2 m je Board, Ports/Verlegung prüfen.<br>[Beleg](../firmware/Marlin/Configuration.h); Kostenzeile `BUD-S011` |
| <a id="sys-012"></a>**SYS-012** USB-Kabel für MUX/UART/Zielversorgung | – / – / **3 Stück** | teilweise geklärt | offen; nicht belegt | 3 Verbindungen aus Softwarekonfiguration, Geräteseite und enthaltene Kabel offen; nur nach Geräteauswahl kaufen.<br>[Beleg](../software/hardware-control/proboter/cli.py); Kostenzeile `BUD-S012` |
| <a id="sys-013"></a>**SYS-013** Bewegliche Kameraleitung / USB-Verlängerung | – / – / **1 Stück** | teilweise geklärt | offen; nicht belegt | Schleppkettengeeignete Leitung/Länge/Stecker offen; Kamera-Beipack gegenrechnen.<br>[Beleg](https://www.schutzwerk.com/en/blog/proboter-02/); Kostenzeile `BUD-S013` |
| <a id="sys-014"></a>**SYS-014** Motorleitungen 4adrig | – / – / **32 m** | teilweise geklärt | offen; nicht belegt | Plan 16×2 m; Schleppkettenradius, Querschnitt/Strom, Aderfarben und reale Wege offen.<br>[Beleg](../firmware/Marlin/Configuration.h); Kostenzeile `BUD-S014` |
| <a id="sys-015"></a>**SYS-015** Motor-Gegenstecker und Crimpkontakte | – / – / **32 Satz** | teilweise geklärt | offen; nicht belegt | Plan 2 Enden je 16 Motoren. Board-/Motorhersteller-Raster und Kontaktzahl prüfen; beiliegende Kabel abziehen.<br>[Beleg](../firmware/Marlin/Configuration.h); Kostenzeile `BUD-S015` |
| <a id="sys-016"></a>**SYS-016** Sensorleitungen / Verlängerungen | – / – / **24 Stück** | teilweise geklärt | offen; nicht belegt | Für 24 induktive Sensoren; enthaltene Anschlussleitungen zuerst prüfen. Optische 1 m-Kabel sind bei O-009 enthalten.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-SYS-016` |
| <a id="sys-017"></a>**SYS-017** Sensor-Gegenstecker und Kontakte | – / – / **28 Satz** | teilweise geklärt | offen; nicht belegt | 24 induktiv+4 optisch; bei steckerfertigem Beipack reduzieren. Keine generischen JST/Dupont ohne Rasterprüfung.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-SYS-017` |
| <a id="sys-018"></a>**SYS-018** 24-V-Verteilung, Sicherungen, Klemmen, Leitungen | – / – / **1 Satz** | teilweise geklärt | offen; nicht belegt | 4 Controller+Sensoren+LED; Last/Stromlaufplan, Aderquerschnitte und Sicherungswerte bestimmen.<br>[Beleg](../firmware/Marlin/Configuration.h); Kostenzeile `BUD-S018` |
| <a id="sys-020"></a>**SYS-020** Netzeinspeisung, Leitung, Sicherung und Zugentlastung | – / – / **1 Satz** | teilweise geklärt | offen; nicht belegt | 230 V-Anschluss an offenes Netzteil: Anschlussmodul, Netzleitung, Sicherungshalter und geschützter Kabelweg planen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUD-S020` |
| <a id="sys-021"></a>**SYS-021** Schutzleiter, Ringkabelschuhe und Klemmenabdeckung | – / – / **1 Satz** | teilweise geklärt | offen; nicht belegt | Metallrahmen/Netzteil erden; Querschnitt, Anschlusspunkte und Prüfverfahren in Stromlaufplan dokumentieren.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUD-S021` |
| <a id="sys-022"></a>**SYS-022** Messkoax und instrumentenseitige Adapter | – / – / **4 Kanäle** | teilweise geklärt | offen; nicht belegt | Vorhan dene Messgeräte verwenden; BNC/SMA/MMCX und Impedanz gerätespezifisch. CAD-MM CX-Stecker 61/62 sind separat, hier nur Kabel und Instrumentadapter.<br>[Beleg](../software/hardware-control/proboter/cli.py); Kostenzeile `BUD-S022` |
| <a id="sys-025"></a>**SYS-025** USB-UART-Adapter | – / – / **1 Stück** | teilweise geklärt | offen; nicht belegt | Software setzt Adapter voraus; Pegel, Isolation, Pinout und Zielversorgung prüfen; Laborausstattung ggf. gegenrechnen.<br>[Beleg](../software/hardware-control/proboter/cli.py); Kostenzeile `BUD-S025` |
| <a id="sys-027"></a>**SYS-027** Energieketten-Endanschlüsse schmal | – / – / **16 Sätze** | teilweise geklärt | offen; nicht belegt | igus E2.100.10.34PZ, beidseitig schwenkbar mit Zugentlastung; Breite 17,4 = Anschlusskörper im CAD (Fusion-Messung).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-024` |
| <a id="sys-028"></a>**SYS-028** Energieketten-Endanschlüsse breit | – / – / **8 Sätze** | teilweise geklärt | offen; nicht belegt | igus E2.100.20.34PZ; Breite 27,4 = Anschlusskörper im CAD (Fusion-Messung).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-025` |
| <a id="sys-029"></a>**SYS-029** Profil-Nutensteine und Zusatzbefestigung | – / – / **1 Satz** | teilweise geklärt | offen; nicht belegt | Nut 6/Profilserie klären; 26Winkel plus Halter. CAD-Vierkantmuttern 29/30 und mitgelieferte Winkelsätze abziehen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUD-S029` |
| <a id="sys-030"></a>**SYS-030** Scheiben, Sicherungselemente, Distanzteile | – / – / **1 Satz** | teilweise geklärt | offen; nicht belegt | Ergänzungsbedarf je Verschraubung/Idler; CAD-Normteile und Sensor-Beipack abziehen. Stückzahlen noch offen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUD-S030` |
| <a id="sys-031"></a>**SYS-031** Lötzinn, Schrumpfschlauch, Binder, Labels, Kleber | – / – / **1 Satz** | teilweise geklärt | offen; nicht belegt | Verbrauchsmaterialbudget; vorhan dene Bestände später abziehen. Werkzeuge nicht enthalten.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUD-S031` |
| <a id="sys-032"></a>**SYS-032** Controller-Befestigung und Kühlung | – / – / **1 Satz** | teilweise geklärt | offen; nicht belegt | Abstandshalter, Isolierung, ggf.Lüfter; SKR/TMC-Beipack und thermische Auslegung prüfen.<br>[Beleg](../firmware/Marlin/Configuration.h); Kostenzeile `BUD-S032` |
| <a id="sys-038"></a>**SYS-038** Kalibrier-Kontaktleitungen und gemeinsame Messreferenz | – / – / **1 Satz** | teilweise geklärt | offen; nicht belegt | 4 SKR-Zentriereingänge P0_17 mit Pull-up/aktiv Low sowie Referenzkörper/Kontaktkreis verdrahten. Netzplan, Stecker, Länge und Bezugspotenzial mit Multiplexer klären; keine Verbindung ungeprüft festlegen.<br>[Beleg](../firmware/Marlin/src/module/proboter.cpp); Kostenzeile `OPEN-SYS-038` |
| <a id="sys-041"></a>**SYS-041** Nutenstein I-Typ Nut 6, M6, Motorplatten | – / – / **8 Stück** | bestellfähig | offen; nicht belegt | Fusion-Kontaktanalyse M01: die 8 Senkschrauben M6×20 der Motorplatten greifen in die Nut der 60×30-Profile; im CAD kein Gegenstück.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-041` |
| <a id="sys-042"></a>**SYS-042** Nutenstein I-Typ Nut 6, M4, Rückwand | – / – / **6 Stück** | bestellfähig | offen; nicht belegt | Fusion-Kontaktanalyse M01: 6 Bohrungen Ø4,5 der Rückwand liegen auf den langen Profilen; im CAD keine Befestigung.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-042` |
| <a id="sys-043"></a>**SYS-043** Zylinderschraube DIN 912 M4×10 A2, Rückwand | – / – / **6 Stück** | bestellfähig | offen; nicht belegt | Zu SYS-042; 3 mm Rückwand plus Nutenstein.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-043` |
| <a id="sys-044"></a>**SYS-044** Nutenstein I-Typ Nut 6, M5, Griff | – / – / **2 Stück** | bestellfähig | offen; nicht belegt | Griff A-75873 mit Durchgangsbohrungen wird von vorn ins Schubladenprofil geschraubt.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-044` |
| <a id="sys-045"></a>**SYS-045** Zylinderschraube DIN 912 M5×35 A2, Griff | – / – / **2 Stück** | bestellfähig | offen; nicht belegt | Länge aus 29 mm Griffbein plus Nutenstein; Schrauben.Expert 912 5 35 A2.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-045` |
| <a id="sys-046"></a>**SYS-046** Zylinderschraube DIN 912 M4×10 A2, Wellenhalter | – / – / **7 Stück** | bestellfähig | offen; nicht belegt | Fusion-Messung: 4 Wellenhalter mit je 2 Bohrungen Ø4,5 über der Nut der Schubladen-Querprofile; 1 von 8 Schrauben im CAD.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-046` |
| <a id="sys-047"></a>**SYS-047** Nutenstein I-Typ Nut 6, M4, Wellenhalter | – / – / **8 Stück** | bestellfähig | offen; nicht belegt | Gegenstück zu den 8 Wellenhalter-Schrauben.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-047` |
| <a id="sys-048"></a>**SYS-048** Linsenkopfschraube ISO 7380-1 M4×8 A2, Teleskopschienen | – / – / **12 Stück** | bestellfähig | offen; nicht belegt | ANNAHME (Luis 17.10.2026): je Schiene 3 Schrauben zum Rahmen und 3 zur Schublade; im CAD keine Befestigung. Linsenkopf ISO 7380-1, Kopfhöhe 2,2 mm.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-048` |
| <a id="sys-049"></a>**SYS-049** Nutenstein I-Typ Nut 6, M4, Teleskopschienen | – / – / **12 Stück** | bestellfähig | offen; nicht belegt | ANNAHME, Gegenstück zu SYS-048.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-049` |
| <a id="sys-050"></a>**SYS-050** Zylinderschraube DIN 912 M3×8 A2, Kabelhalter M3 | – / – / **4 Stück** | bestellfähig | offen; nicht belegt | Fusion: Kabelhalter 3,4 mm dick auf den M3-Gewinden des Kettenhalter-Profils (Wand 3,8 mm). Planmenge mit Reserve +10 %, mindestens +2.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-050` |
| <a id="sys-051"></a>**SYS-051** Zylinderschraube DIN 912 M3×10 A2, igus-Kettenanschlüsse | – / – / **106 Stück** | bestellfähig | offen; nicht belegt | ANNAHME: 48 Anschlusselemente mit je 2 Bohrungen Ø3,2 (Fusion), je eine M3×10 mit Mutter; davon 16 am Kettenadapter (Wand 5,2 mm). Planmenge mit Reserve +10 %, mindestens +2.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-051` |
| <a id="sys-052"></a>**SYS-052** Zylinderschraube DIN 912 M3×12 A2, Z-Kabelhalter | – / – / **6 Stück** | bestellfähig | offen; nicht belegt | ANNAHME: Kabelhalter 3,4 mm an der Z-Schiene, mit Mutter. Planmenge mit Reserve +10 %, mindestens +2.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-052` |
| <a id="sys-053"></a>**SYS-053** Sechskantmutter DIN 934 M3 A2, Kabelführung | – / – / **111 Stück** | bestellfähig | offen; nicht belegt | Muttern zu SYS-051 und SYS-052. Planmenge mit Reserve +10 %, mindestens +2.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-053` |
| <a id="sys-054"></a>**SYS-054** Linsenkopfschraube ISO 7380-1 M4×8 A2, Kabelführung | – / – / **11 Stück** | bestellfähig | offen; nicht belegt | 1× Kabelhalter M4 auf dem Rahmenprofil (4,5 mm + Nutenstein), 8× Kettenadapter auf dem Versteifungsträger (ANNAHME, Gegenstück hängt vom Profil CAD-103 ab). Planmenge mit Reserve +10 %, mindestens +2.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-054` |
| <a id="sys-055"></a>**SYS-055** Nutenstein I-Typ Nut 6, M4, Kabelhalter | – / – / **3 Stück** | bestellfähig | offen; nicht belegt | Für den Kabelhalter M4 am Rahmenprofil. Planmenge mit Reserve +10 %, mindestens +2.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-055` |
| <a id="sys-056"></a>**SYS-056** Zylinderschraube DIN 912 M5×10 A2, Kabelhalter M5 | – / – / **6 Stück** | bestellfähig | offen; nicht belegt | Fusion: Kabelhalter 5,5 mm auf der Seitenplatte des X-Wagens (M5-Gewinde). Planmenge mit Reserve +10 %, mindestens +2.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `BUY-SYS-056` |

## 3D-Druck intern

| ID / Teil | CAD / Fusion / Plan | Status | Geometrie / Werkstoff | Quelle und konkreter Klärbedarf |
| --- | --- | --- | --- | --- |
| <a id="cad-001"></a>**CAD-001** Y-Riemenklemme (CAD-Name TR10x 2 GT2 Adapter)<br>`TR10x2_GT2_belt_adapter` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 15.0 x 20.0 x 22.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-002"></a>**CAD-002** Y-Riemenklemme, Deckel<br>`TR10x2_GT2_belt_adapter_cover` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 7.0 x 20.0 x 20.494; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-004"></a>**CAD-004** Grundgestell: Kabel Halter M3 flach<br>`base_cable_holder_m3_flat` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 18.0 x 10.0 x 8.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-005"></a>**CAD-005** Grundgestell: Kabel Halter M4<br>`base_cable_holder_m4` | 1 / 1 / **1 Stück** | Fertigung spezifiziert | 18.0 x 12.0 x 10.5; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-006"></a>**CAD-006** Grundgestell: Kabel Halter M5 flach<br>`base_cable_holder_m5_flat` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 18.0 x 14.0 x 10.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-015"></a>**CAD-015** Grundgestell: NEMA 14 auf 17 Adapter<br>`base_nema_14_to_17_adapter` | 12 / 12 / **12 Stück** | Fertigung spezifiziert | 40.0 x 45.0 x 52.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-021"></a>**CAD-021** Riemen Spanner GT2 Basis<br>`belt_tightener_GT2_base` | 20 / 20 / **20 Stück** | Fertigung spezifiziert | 44.0 x 35.0 x 20.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-022"></a>**CAD-022** Riemen Spanner GT2 Flügel<br>`belt_tightener_GT2_wing` | 20 / 20 / **20 Stück** | Fertigung spezifiziert | 40.0 x 20.0 x 10.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-024"></a>**CAD-024** Kabel Abdeckung<br>`cable_cover` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 22.0 x 58.0 x 3.0; PETG (Entscheidung Luis 17.10.2026); Original Blech 3 mm | Kabelabdeckung 22×58×3 mm mit 16 Bohrungen Ø4, als PETG-Druckteil statt Blech.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-025"></a>**CAD-025** Kamera Halter<br>`camera_holder` | 1 / 1 / **1 Stück** | Fertigung spezifiziert | 37.0 x 42.0 x 19.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-067"></a>**CAD-067** Platine Halter Gleiter<br>`pcb_holder_glider` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 24.0 x 30.0 x 18.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-068"></a>**CAD-068** Platine Halter Führung Halter rund d 10<br>`pcb_holder_guiding_holder_round_d10` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 37.0 x 14.0 x 26.5; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-071"></a>**CAD-071** Platine Halter Stange kurz rund d 10<br>`pcb_holder_rod_short_round_d10` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 30.0 x 30.0 x 18.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-072"></a>**CAD-072** Platine Halter Stange kurz rund d 10 gespiegelt<br>`pcb_holder_rod_short_round_d10_mirrored` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 30.0 x 30.0 x 18.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-074"></a>**CAD-074** Stromversorgung Schalter Halter<br>`power_switch_holder` | 1 / 1 / **1 Stück** | Fertigung spezifiziert | 65.0 x 30.0 x 41.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-083"></a>**CAD-083** Signal-Multiplexer Halter<br>`signal_multiplexer_holder` | 1 / 1 / **1 Stück** | Fertigung spezifiziert | 117.0 x 103.0 x 45.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-088"></a>**CAD-088** X-Achse Riemen Halter<br>`x_belt_holder` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 47.0 x 20.0 x 44.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-089"></a>**CAD-089** X-Achse Riemen Halter 1<br>`x_belt_holder_1` | 12 / 12 / **12 Stück** | Fertigung spezifiziert | 35.0 x 20.0 x 44.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-090"></a>**CAD-090** X-Achse Schlepp Energiekette Adapter<br>`x_drag_chain_adapter` | 8 / 8 / **8 Stück** | Fertigung spezifiziert | 45.7 x 30.0 x 7.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-091"></a>**CAD-091** X-Achse Endschalter Halter Seite kurz<br>`x_end_stop_holder_side_short` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 12.0 x 68.5 x 12.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-092"></a>**CAD-092** X-Achse Endschalter Halter oben lang<br>`x_end_stop_holder_top_long` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 15.0 x 98.5 x 18.2; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-101"></a>**CAD-101** X-Achse Schlitten induktiv Endschalter Adapter<br>`x_slide_inductive_endstop_adapter` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 20.5 x 50.0 x 48.5; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-102"></a>**CAD-102** X-Achse Schlitten induktiv Endschalter Adapter gespiegelt<br>`x_slide_inductive_endstop_adapter_mirrored` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 20.5 x 50.0 x 48.5; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-105"></a>**CAD-105** Y-Achse Kamera Halter<br>`y_camera_holder` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 50.816 x 51.0 x 35.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-106"></a>**CAD-106** Y-Achse Kamera Halter kompakt<br>`y_camera_holder_compact` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 55.982 x 42.0 x 40.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-107"></a>**CAD-107** Y-Achse Schlitten<br>`y_slide` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 65.0 x 19.8 x 136.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-109"></a>**CAD-109** Y-Achse Schlitten Abstand Rohr 2 mm<br>`y_slide_distance_tube_2mm` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 3.0 x 10.0 x 10.0; PETG (Entscheidung Luis 17.10.2026) | Fusion-Messung: Hülse Ø3/Ø4,8 × 3 mm (Name sagt 2 mm). Als PETG-Druckteil (Entscheidung Luis 17.10.2026); kein passender Kaufartikel gefunden.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-110"></a>**CAD-110** Y-Achse Schlitten gespiegelt<br>`y_slide_mirrored` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 65.0 x 19.8 x 136.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-111"></a>**CAD-111** Y-Achse Schlitten gespiegelt oben<br>`y_slide_mirrored_top` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 65.0 x 14.0 x 82.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-112"></a>**CAD-112** Y-Achse Schlitten oben<br>`y_slide_top` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 65.0 x 14.0 x 82.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-114"></a>**CAD-114** Z-Achse Antrieb Riemen Halter v 3<br>`z_drive_belt_holder_v3` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 35.0 x 15.0 x 35.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-116"></a>**CAD-116** Z-Achse Prüfspitze Platine Halter<br>`z_probe_tip_pcb_holder` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 79.382 x 16.0 x 12.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-117"></a>**CAD-117** Z-Achse Prüfspitze Platine Halter lang<br>`z_probe_tip_pcb_holder_long` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 103.413 x 16.0 x 55.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-118"></a>**CAD-118** Z-Achse Schlitten Kabel Halter<br>`z_slide_cable_holder` | 4 / 4 / **4 Stück** | Fertigung spezifiziert | 16.0 x 8.0 x 10.0; PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis | Geometrie vorhan den; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-119"></a>**CAD-119** Z-Achse Schlitten Endschalter Auslöser<br>`z_slide_end_stop_trigger.psm` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 9.05 x 22.5 x 15.0; PETG (Entscheidung Luis 17.10.2026); Original Blechteil | Auslöser für den optischen Z-Endschalter, keine Last. Statt Blech als PETG-Druckteil (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="cad-120"></a>**CAD-120** Z-Achse Schlitten Endschalter Auslöser gespiegelt<br>`z_slide_end_stop_trigger_mirrored.psm` | 2 / 2 / **2 Stück** | Fertigung spezifiziert | 9.05 x 22.5 x 15.0; PETG (Entscheidung Luis 17.10.2026); Original Blechteil | Auslöser für den optischen Z-Endschalter, keine Last. Statt Blech als PETG-Druckteil (Entscheidung 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-001` |
| <a id="sys-004"></a>**SYS-004** Kalibrier-Referenzkörper / Platte | – / – / **1 Stück** | Fertigung noch offen | offen; nicht belegt | Geometrie mit aktueller Software festlegen; Plattendicke 5,1 mm ist Konfigurationswert, keine validierte Zeichnung.<br>[Beleg](../software/hardware-control/proboter/cli.py); Kostenzeile `MAT-001` |

## Blech intern

| ID / Teil | CAD / Fusion / Plan | Status | Geometrie / Werkstoff | Quelle und konkreter Klärbedarf |
| --- | --- | --- | --- | --- |
| <a id="cad-003"></a>**CAD-003** Grundgestell: Rückseite Platte<br>`base_back_plate` | 1 / 1 / **1 Stück** | Fertigung noch offen | 650.0 x 3.0 x 270.0; Aluminium 3 mm (Entscheidung 17.10.2026), z. B. EN AW-5754 | 650×270×3 mm, 54 Bohrungen Ø3,4, 10 Bohrungen Ø4,5, 1 Bohrung Ø8. 6 Ø4,5-Bohrungen sitzen auf den langen Profilen (M4 + Nutenstein, siehe M01). Zuschnitt und Bohrungen intern; Zeichnung aus CAD ableiten.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-007"></a>**CAD-007** Grundgestell: Abdeckung lang Seite<br>`base_cover_long_side` | 2 / 2 / **2 Stück** | Fertigung noch offen | 660.0 x 5.0 x 135.5; Stahl S235 vorgeschlagen; Abdeckungen alternativ Alublech, nicht freigegeben | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-008"></a>**CAD-008** Grundgestell: Abdeckung oben<br>`base_cover_top` | 2 / 2 / **2 Stück** | Fertigung noch offen | 656.0 x 5.0 x 182.5; Stahl S235 vorgeschlagen; Abdeckungen alternativ Alublech, nicht freigegeben | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-016"></a>**CAD-016** Grundgestell: Platte Adapter 1<br>`base_plate_adapter_1` | 2 / 2 / **2 Stück** | Fertigung noch offen | 130.4 x 10.0 x 91.0; Stahl- oder Aluminiumblech, Werkstattentscheidung | 10 mm Platte mit Stufen auf 5 mm und 90°-Senkungen; trägt die X-Riemenantriebe. Fräsen oder aus zwei 5-mm-Platten. Zeichnung aus CAD ableiten.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-017"></a>**CAD-017** Grundgestell: Platte Adapter 2<br>`base_plate_adapter_2` | 2 / 2 / **2 Stück** | Fertigung noch offen | 130.5 x 10.0 x 91.0; Stahl- oder Aluminiumblech, Werkstattentscheidung | 10 mm Platte mit Stufen auf 5 mm und 90°-Senkungen; trägt die X-Riemenantriebe. Fräsen oder aus zwei 5-mm-Platten. Zeichnung aus CAD ableiten.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-018"></a>**CAD-018** Grundgestell: Platte Adapter links<br>`base_plate_adapter_left` | 2 / 2 / **2 Stück** | Fertigung noch offen | 162.0 x 10.0 x 67.079; Stahl- oder Aluminiumblech, Werkstattentscheidung | 10 mm Platte mit Stufen auf 5 mm und 90°-Senkungen; trägt die X-Riemenantriebe. Fräsen oder aus zwei 5-mm-Platten. Zeichnung aus CAD ableiten.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-019"></a>**CAD-019** Grundgestell: Platte Adapter rechts<br>`base_plate_adapter_right` | 2 / 2 / **2 Stück** | Fertigung noch offen | 162.0 x 10.0 x 67.079; Stahl- oder Aluminiumblech, Werkstattentscheidung | 10 mm Platte mit Stufen auf 5 mm und 90°-Senkungen; trägt die X-Riemenantriebe. Fräsen oder aus zwei 5-mm-Platten. Zeichnung aus CAD ableiten.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-026"></a>**CAD-026** Kamera Halter oben<br>`camera_holder_top` | 1 / 1 / **1 Stück** | Fertigung noch offen | 104.0 x 56.63 x 5.0; Stahl S235 vorgeschlagen; Abdeckungen alternativ Alublech, nicht freigegeben | Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-096"></a>**CAD-096** X-Achse Motor Platte<br>`x_motor_plate` | 1 / 1 / **1 Stück** | Fertigung noch offen | 550.0 x 5.0 x 135.0; Stahl- oder Aluminiumblech 5 mm, Werkstattentscheidung | 5 mm Stahl, 550×135 mm. Fusion-Messung: 16 Kernlöcher Ø2,46 für M3-Gewinde (Riemenspanner), Senkungen für M6 und Ø22-Durchbrüche für die Motoren. Kontur und Bohrungen aus CAD; Gewinde und Senkungen intern. Zeichnung mit Lagetoleranzen der Führungsbohrungen fehlt.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-097"></a>**CAD-097** X-Achse Motor Platte 2<br>`x_motor_plate_2` | 1 / 1 / **1 Stück** | Fertigung noch offen | 550.0 x 5.0 x 135.0; Stahl- oder Aluminiumblech 5 mm, Werkstattentscheidung | 5 mm Stahl, 550×135 mm. Fusion-Messung: 16 Kernlöcher Ø2,46 für M3-Gewinde (Riemenspanner), Senkungen für M6 und Ø22-Durchbrüche für die Motoren. Kontur und Bohrungen aus CAD; Gewinde und Senkungen intern. Zeichnung mit Lagetoleranzen der Führungsbohrungen fehlt.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-099"></a>**CAD-099** X-Achse Seite Platte<br>`x_side_plate` | 4 / 4 / **4 Stück** | Fertigung noch offen | 55.0 x 5.0 x 166.5; Stahl- oder Aluminiumblech, Werkstattentscheidung | 5 mm Seitenplatte des X-Wagens, im Original lasergeschnitten. Zeichnung aus CAD ableiten.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |
| <a id="cad-100"></a>**CAD-100** X-Achse Seite Platte beweglich<br>`x_side_plate_moving` | 4 / 4 / **4 Stück** | Fertigung noch offen | 55.0 x 5.0 x 166.5; Stahl- oder Aluminiumblech, Werkstattentscheidung | 5 mm Seitenplatte des X-Wagens, im Original lasergeschnitten. Zeichnung aus CAD ableiten.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-006` |

## CNC extern

| ID / Teil | CAD / Fusion / Plan | Status | Geometrie / Werkstoff | Quelle und konkreter Klärbedarf |
| --- | --- | --- | --- | --- |

## Weitere Fertigung

| ID / Teil | CAD / Fusion / Plan | Status | Geometrie / Werkstoff | Quelle und konkreter Klärbedarf |
| --- | --- | --- | --- | --- |
| <a id="cad-009"></a>**CAD-009** Grundgestell: Schlepp Energiekette Halter<br>`base_drag_chain_holder` | 4 / 4 / **4 Stück** | teilweise geklärt | 80.0 x 650.0 x 16.0; Aluminium, DOLD I-Typ Nut 8 | Fusion-Messung: Alu-Flachprofil 16×80×650 mm (932 mm², 2 Kerne Ø5) mit 18 M3-Gewinden. Kandidat DOLD 80x 16S I-Typ Nut 8 (60886-Z), gleiche Serie wie CAD-103, aber 813 mm² und laut Produktseite M8-Kern. Kerngröße an der DOLD-Zeichnung prüfen; M3-Gewinde in der Werkstatt.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-008` |
| <a id="cad-011"></a>**CAD-011** Grundgestell: Schublade lang Seite<br>`base_drawer_long_side` | 2 / 2 / **2 Stück** | bestellfähig | 30.0 x 564.0 x 30.0; je Teil vorgeschlagen, siehe Fertigung.md | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-002` |
| <a id="cad-012"></a>**CAD-012** Grundgestell: Rahmen lang Seite<br>`base_frame_long_side` | 3 / 3 / **3 Stück** | bestellfähig | 30.0 x 590.0 x 30.0; je Teil vorgeschlagen, siehe Fertigung.md | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-002` |
| <a id="cad-013"></a>**CAD-013** Grundgestell: Rahmen kurz<br>`base_frame_short` | 8 / 8 / **8 Stück** | bestellfähig | 30.0 x 350.0 x 30.0; je Teil vorgeschlagen, siehe Fertigung.md | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-002` |
| <a id="cad-014"></a>**CAD-014** Grundgestell: Rahmen Seite<br>`base_frame_side` | 2 / 2 / **2 Stück** | bestellfähig | 30.0 x 650.0 x 60.0; je Teil vorgeschlagen, siehe Fertigung.md | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-003` |
| <a id="cad-020"></a>**CAD-020** Grundgestell: vertikal<br>`base_vertical` | 4 / 4 / **4 Stück** | bestellfähig | 30.0 x 350.0 x 30.0; je Teil vorgeschlagen, siehe Fertigung.md | Querschnitt und Länge aus CAD (4×350 mm). Unten M6-Gewinde in die Kernbohrung Ø5 für die Gelenkfüße, intern schneiden (Entscheidung 17.10.2026). Profilserie siehe M01.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-002` |
| <a id="cad-069"></a>**CAD-069** Platine Halter Führung rund<br>`pcb_holder_guiding_round` | 2 / 2 / **2 Stück** | bestellfähig | 10.0 x 356.8 x 10.0; je Teil vorgeschlagen, siehe Fertigung.md | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-004` |
| <a id="cad-070"></a>**CAD-070** Platine Halter rechteckig Stange<br>`pcb_holder_rect_rod` | 2 / 2 / **2 Stück** | Fertigung noch offen | 11.5 x 205.0 x 11.5; Aluminium-Vierkantrohr 12×12×1 (Al Mg Si 0,5) | ABWEICHUNG (Entscheidung Luis 17.10.2026): CAD-Vierkantrohr 11,5×11,5×1,5×205 mm (Fusion-Messung) wird durch Alu-Vierkantrohr 12×12×1 mm ersetzt (keine Last; 12×12×1,5 in DE/EU nicht gefunden); gedruckte Schieber CAD-067 auf 12 mm anpassen. Bezugsquelle z. B. e Bay metalexpres (Al Mg Si 0,5, ab 500 mm), Preis und Lager noch prüfen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-005` |
| <a id="cad-093"></a>**CAD-093** X-Achse Endschalter oben lang<br>`x_end_stop_top_long` | 4 / 4 / **4 Stück** | Fertigung noch offen | 125.0 x 8.0 x 8.0; je Teil vorgeschlagen, siehe Fertigung.md | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-005` |
| <a id="cad-094"></a>**CAD-094** X-Achse Endschalter oben kurz<br>`x_end_stop_top_short` | 4 / 4 / **4 Stück** | Fertigung noch offen | 75.0 x 8.0 x 8.0; je Teil vorgeschlagen, siehe Fertigung.md | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-005` |
| <a id="cad-098"></a>**CAD-098** X-Achse rund Schiene<br>`x_round_rail` | 8 / 8 / **8 Stück** | bestellfähig | 10.0 x 450.0 x 10.0; je Teil vorgeschlagen, siehe Fertigung.md | Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-004` |
| <a id="cad-103"></a>**CAD-103** X-Achse Schlitten Versteifung Träger<br>`x_slide_stiffener_beam` | 4 / 4 / **4 Stück** | bestellfähig | 40.0 x 436.0 x 16.0; Aluminium, DOLD 40x 16S I-Typ Nut 8 | DOLD 40x 16S I-Typ Nut 8 schwer (60879-Z) im Zuschnitt: 1,178 kg/m ≈ 436 mm² (CAD 446 mm²), Kern Ø5 für M6 = CAD. M6-Gewinde in die Stirnseiten selbst schneiden.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-007` |
| <a id="cad-108"></a>**CAD-108** Y-Achse Schlitten Abstand Stange<br>`y_slide_distance_rod` | 8 / 8 / **8 Stück** | Fertigung spezifiziert | 4.0 x 70.0 x 4.0; Silberstahl 1.2210 Ø4 h 6 | Fusion-Messung: massiver Rundstab Ø4×70 mm, Fasen an beiden Enden, ohne Gewinde. Werkstatt: aus Ø4-h 6-Silberstahl (1.2210) ablängen und anfasen (Entscheidung Luis 17.10.2026).<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `MAT-005` |
| <a id="sys-005"></a>**SYS-005** Innere Messing-Referenzzylinder | – / – / **4 Stück** | Fertigung noch offen | offen; nicht belegt | Je 1×Ø7/8/9/10 mm nach Reference Board.inner_brass_pin_position_map; Raster 11,95×19,95 mm. Endfläche auf Bezugsebene; Gesamtlänge, Einbau, Toleranzen und Messprotokoll fehlen.<br>[Beleg](../software/hardware-control/proboter/tasks/utils/reference_board.py); Kostenzeile `OPEN-SYS-005` |
| <a id="sys-006"></a>**SYS-006** Kalibriermarker / matte Druckvorlage | – / – / **1 Satz** | Fertigung noch offen | offen; nicht belegt | 4 Hamming-Marker mit IDs 1/3/6/12 laut Reference Board, je 18,2×18,2 mm, Raster 60×80 mm. Mtracker-Format verwenden, keine beliebigen Ar Uco-Marker. Maßstab 1:1 und reale Abstände vermessen.<br>[Beleg](../software/hardware-control/proboter/tasks/utils/reference_board.py); Kostenzeile `OPEN-SYS-006` |
| <a id="sys-037"></a>**SYS-037** Weiße äußere Kalibrierreferenzen | – / – / **4 Stück** | Fertigung noch offen | offen; nicht belegt | Reference Board Config beschreibt vier äußere weiße Referenzpins. Raster 109,9×89,8 mm; Durchmesser, Höhe, Material und Umsetzung am gewählten Board fehlen. Nicht mit 12Messingpins gleichsetzen.<br>[Beleg](../software/hardware-control/proboter/model/reference_board_config.py); Kostenzeile `OPEN-SYS-037` |
| <a id="sys-039"></a>**SYS-039** Erhöhte Messing-Referenzzylinder | – / – / **4 Stück** | Fertigung noch offen | offen; nicht belegt | Ø7 mm laut Reference Board-Skizze; Code setzt vier Endflächen 6/8/10/12 mm über Bezugsebene auf Raster 59,6×39,9 mm. Gesamtlängen und Einstecktiefe sind nicht diese Höhen; Zeichnung und Toleranzen fehlen.<br>[Beleg](../software/hardware-control/proboter/tasks/utils/reference_board.py); Kostenzeile `OPEN-SYS-039` |
| <a id="sys-040"></a>**SYS-040** Äußere flache Messing-Referenzzylinder | – / – / **4 Stück** | Fertigung noch offen | offen; nicht belegt | Ø7 mm laut Reference Board-Skizze; Mittelpunkte(±54,95;0) und(0;±44,9)mm. Endflächen auf Bezugsebene; Länge und Montage offen. Insgesamt 12Messingzylinder plus 4weiße Referenzen.<br>[Beleg](../software/hardware-control/proboter/tasks/utils/reference_board.py); Kostenzeile `OPEN-SYS-040` |

## PCB extern

| ID / Teil | CAD / Fusion / Plan | Status | Geometrie / Werkstoff | Quelle und konkreter Klärbedarf |
| --- | --- | --- | --- | --- |
| <a id="cad-075"></a>**CAD-075** Prüfspitzen-PCB, unbestückt<br>`probe_tip_pcb` | 4 / 4 / **4 Stück** | Fertigung noch offen | 26.67 x 10.96 x 1.6; FR4 1,6 mm vorgeschlagen; Dicke geometrisch belegt | 4 Stück;26,67×10,96×1,6 mm Hülle. Schaltplan, Kupfer, Bohrungen, Gerber und Bestückungsdaten fehlen. Bestückung SYS-024 separat.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-CAD-075` |
| <a id="sys-003"></a>**SYS-003** Signal-Multiplexer, unbestückte Leiterplatte | – / – / **1 Stück** | Fertigung noch offen | offen; nicht belegt | CAD-082 ist nur Platzhalter. Schaltplan/Gerber/Board-BOM fehlen; USB/9600Baud-Protokoll ist keine Schaltung.<br>[Beleg](../software/hardware-control/proboter/cli.py); Kostenzeile `OPEN-SYS-003` |
| <a id="sys-019"></a>**SYS-019** Sensor-Pegelanpassung / Eingangsschutz | – / – / **24 Kanäle** | Fertigung noch offen | offen; nicht belegt | Bedarf abhängig von M8-Ausgang; 24 V/3,3 V-Interface. Keine Schaltung/BOM vorhan den; nicht blind 24Module bestellen.<br>[Beleg](../firmware/Marlin/Configuration.h); Kostenzeile `OPEN-SYS-019` |
| <a id="sys-023"></a>**SYS-023** Signal-Multiplexer Bestückung | – / – / **1 Baugruppe** | Fertigung noch offen | offen; nicht belegt | MCU, USB/Versorgung, Schalter/Relais, Schutz, Stecker, Passives und Montage nach noch fehlendem Schaltplan. Keine Stückzahlen erfinden.<br>[Beleg](../software/hardware-control/proboter/cli.py); Kostenzeile `OPEN-SYS-023` |
| <a id="sys-024"></a>**SYS-024** Prüfspitzen-PCB Bestückung | – / – / **4 Baugruppen** | Fertigung noch offen | offen; nicht belegt | CAD-MM CX/Federkontakte separat; zusätzliche Buchsen und Bauteile erst aus Schaltplan. Unbestückte Platine CAD-075 nicht erneut zählen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-SYS-024` |
| <a id="sys-026"></a>**SYS-026** Zielplatinen-Versorgungscontroller | – / – / **1 Baugruppe** | Fertigung noch offen | offen; nicht belegt | Softwareziel /dev/proboter_target-power-controller; Schaltung, Firmware/Hardware und Kabel fehlen. Separat vom RSP-Netzteil.<br>[Beleg](../software/hardware-control/proboter/cli.py); Kostenzeile `OPEN-SYS-026` |

## Ungeklärte Teile

| ID / Teil | CAD / Fusion / Plan | Status | Geometrie / Werkstoff | Quelle und konkreter Klärbedarf |
| --- | --- | --- | --- | --- |
| <a id="cad-010"></a>**CAD-010** Schubladen-Dummyplatte<br>`base_drawer_dummy_plate` | 1 / 1 / **1 Stück** | nicht identifiziert | 564.0 x 410.0 x 12.0; nicht belegt | Schubladen-Dummy 564×410×12 mm: unklar, ob reale Platte benötigt und welches Material. Nicht stillschweigend ausschließen oder aus Stahl fertigen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-CAD-010` |
| <a id="cad-055"></a>**CAD-055** Induktiver Näherungsschalter M8, Bauhülle 60 mm<br>`inductive_proximity_sensor_m8` | 24 / 24 / **24 Stück** | nicht identifiziert | 8.0 x 60.0 x 8.0; nicht belegt | 24 CAD-Vorkommen. MPN, Schaltabstand, NPN/PNP, NO/NC, Versorgung, Pegel und Kabellänge fehlen.24 V nicht direkt an SKR-Eingänge; Interface CAD-unabhängig SYS-019.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-CAD-055` |
| <a id="cad-061"></a>**CAD-061** MMCX-Stecker gerade / Messleitung<br>`mmcx_male_end` | 4 / 4 / **4 Stück** | nicht identifiziert | 54.154 x 4.02 x 15.714; nicht belegt | 4 CAD-Modelle enthalten Kabelansätze. Impedanz, Kabeltyp, Crimp/Lötanschluss, Gegenstecker und Länge unbekannt.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-CAD-061` |
| <a id="cad-062"></a>**CAD-062** MMCX-Stecker gewinkelt / Messleitung<br>`mmcx_male_end_with_angle` | 4 / 4 / **4 Stück** | nicht identifiziert | 72.342 x 4.02 x 28.475; nicht belegt | 4 CAD-Modelle; Kabel-/Buchsenpaarung mit CAD-061/075 und Multiplexer offen.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-CAD-062` |
| <a id="cad-073"></a>**CAD-073** Prüfkontakt-Hülse P75-2 W<br>`plug_sleeve_P75-2_W` | 8 / 8 / **8 Stück** | nicht identifiziert | 25.4 x 1.2 x 1.2; nicht belegt | 8 Stück, CADØ1,2×25,4 mm. Hersteller und passender Federkontakt CAD-115 unklar; Kontaktpaar vollständig spezifizieren.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-CAD-073` |
| <a id="cad-086"></a>**CAD-086** Bedientaster/-schalterØ19 mm<br>`vandalism_switch_d19` | 1 / 1 / **1 Stück** | nicht identifiziert | 17.91 x 23.0 x 23.0; nicht belegt | Schaltfunktion rastend/tastend, Kontaktlast, Beleuchtung und Zuordnung zu Versorgung/Software unbekannt.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-CAD-086` |
| <a id="cad-115"></a>**CAD-115** Federkontakt der Prüfspitze<br>`z_pogo_pin` | 8 / 8 / **8 Stück** | nicht identifiziert | 16.6 x 1.0 x 1.0; nicht belegt | 8 Stück, CADØ1×16,6 mm. Spitzenform, Hub, Federkraft, Kontaktmaterial und Paarung mit P75-2-W unklar.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `OPEN-CAD-115` |

## Optional

| ID / Teil | CAD / Fusion / Plan | Status | Geometrie / Werkstoff | Quelle und konkreter Klärbedarf |
| --- | --- | --- | --- | --- |
| <a id="sys-033"></a>**SYS-033** Zusätzliche bewegliche Kameras | – / – / **3 Stück** | teilweise geklärt | offen; nicht belegt | Optional zur Vollbestückung aller 4CAD-Halter; zusätzliche USB-Ports/Bandbreite/Kabel separat dimensionieren.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `ausgeschlossen/optional` |

## Nicht benötigt

| ID / Teil | CAD / Fusion / Plan | Status | Geometrie / Werkstoff | Quelle und konkreter Klärbedarf |
| --- | --- | --- | --- | --- |
| <a id="cad-066"></a>**CAD-066** Prüfobjekt-Platzhalter im CAD<br>`pcb_dummy` | 1 / 1 / **0 Stück** | nicht benötigt | 200.0 x 300.0 x 50.0; nicht belegt | CAD-Prüfobjekt, kein Maschinenteil.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `ausgeschlossen/optional` |
| <a id="cad-082"></a>**CAD-082** Multiplexer-Platzhalter im CAD<br>`signal_multiplexer_dummy` | 1 / 1 / **0 Stück** | nicht benötigt | 110.0 x 40.0 x 100.0; nicht belegt | Nur Platzhalter; reale Multiplexer-Platine und Bestückung unter SYS-003/023 erfasst.<br>[Beleg](evidence/cad-geometry.csv); Kostenzeile `ausgeschlossen/optional` |
| <a id="sys-034"></a>**SYS-034** Host-PC, Messgeräte und Werkzeuge | – / – / **1 Bestand** | nicht benötigt | offen; nicht belegt | Vom Käufer vorhan den; Kosten ausgeschlossen. Software nennt Pico Scope PS5000a; bestehendes Gerät/Hostkompatibilität prüfen.<br>[Beleg](../software/hardware-control/proboter/cli.py); Kostenzeile `ausgeschlossen/optional` |
| <a id="sys-035"></a>**SYS-035** Z-Antriebsriemenscheibe / integrierter Adapter | – / – / **0 Stück** | nicht benötigt | offen; nicht belegt | Entfällt: Fusion-Messung zeigt die Antriebsrolle als CAD-076 koaxial auf der Ø5-Motorwelle. CAD-001/002 sind keine Riemenscheiben.<br>[Beleg](../firmware/Marlin/Configuration.h); Kostenzeile `ausgeschlossen/optional` |
| <a id="sys-036"></a>**SYS-036** USB-/Versorgungsanschlüsse der Kalibrierung | – / – / **1 Prüfung** | nicht benötigt | offen; nicht belegt | Passive Referenzplatte benötigt nach veröffentlichtem Konzept keine eigene USB-Elektronik; kein zusätzliches Gerät.<br>[Beleg](https://www.schutzwerk.com/en/blog/proboter-02/); Kostenzeile `ausgeschlossen/optional` |
