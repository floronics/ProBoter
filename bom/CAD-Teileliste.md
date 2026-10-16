# CAD-Teileliste (vollständige Rohinventur)

Stand: 16.10.2026. Quelle: `hardware/3d_models/proboter.stp` (SCHUTZWERK, 19.04.2022). Die Mengen sind **rekursiv gezählte Vorkommen im STEP-Modell**, keine geprüften Bestellmengen. Wiederverwendete Baugruppen werden je Einbau aufgelöst: 1066 Blattteil-Vorkommen und 53 Unterbaugruppen-Vorkommen. Die Unterbaugruppen sind nicht zusätzlich zu bestellen.

**Status:** `MODELL BELEGT` = Hersteller/Modell aus CAD und Herstellerquelle nachvollziehbar; `KLÄREN` = konkrete Variante oder Menge offen; `FERTIGEN` = Sonderteil mit Fertigungsangaben offen; `PLATZHALTER` = vor Bestellung durch reales Teil ersetzen/prüfen.

**Diese Datei ist die Rohinventur nach CAD-Namen.** Die aktuellen geometrischen Erkenntnisse, Fertigungsgruppen und Planmengen stehen in [Teileliste](Teileliste.md), [CAD-Prüfung](CAD-Pruefung.md) und [Bestellliste](Bestellliste.md). Die ältere Klassifikation unten ist keine aktuelle Fertigungsfreigabe.

## Elektronik, Kameras und Prüfkontakte (11 Positionen)

| CAD-Name | Stück | Beschreibung | Status | Vor Bestellung |
|---|---:|---|---|---|
| `bigtreetech_skr_v1_3` | 4 | BIGTREETECH SKR V1.3 Steuerplatine | **MODELL BELEGT** | TMC2130-Treibermodule separat einplanen |
| `inductive_proximity_sensor_m8` | 24 | Induktiver Näherungsschalter M8 | **KLÄREN** | Schaltabstand, PNP/NPN, Versorgung und Stecker fehlen |
| `mean_well_RSP-200-24` | 1 | Mean Well RSP-200-24, 24-V-Netzteil | **MODELL BELEGT** | Netzanschluss, Absicherung und Leistungsauslegung prüfen |
| `mmcx_male_end` | 4 | MMCX-Stecker, gerade | **KLÄREN** | Kabeltyp und konkrete Steckerbauform fehlen |
| `mmcx_male_end_with_angle` | 4 | MMCX-Stecker, gewinkelt | **KLÄREN** | Kabeltyp und konkrete Steckerbauform fehlen |
| `optical_endstop` | 4 | Optischer Endschalter | **KLÄREN** | Bauform, Versorgung, Anschluss und Schaltlogik fehlen |
| `plug_sleeve_P75-2_W` | 8 | Prüfkontakt-Hülse P75-2 W | **KLÄREN** | Hersteller, Einbaumaß und passender Kontakt fehlen |
| `probe_tip_pcb` | 4 | Prüfspitzen-Platine | **KLÄREN** | Keine Gerber/Schaltpläne im Upstream; Fertigung offen |
| `usb_microscope` | 4 | USB-Mikroskop | **KLÄREN** | Auflösung, Optik, Haltermaß und reale Anzahl prüfen |
| `vandalism_switch_d19` | 1 | Vandalismussicherer Schalter Ø19 mm | **KLÄREN** | Schaltfunktion, Beleuchtung und Spannung fehlen |
| `z_pogo_pin` | 8 | Federkontakt für Z-Prüfspitze | **KLÄREN** | Federweg, Spitzenform und Kontaktierung fehlen |

## Antriebe und Linearführungen (7 Positionen)

| CAD-Name | Stück | Beschreibung | Status | Vor Bestellung |
|---|---:|---|---|---|
| `cpc_MR12ML` | 8 | CPC MR12ML Miniatur-Führungswagen | **KLÄREN** | Vorspannung/Genauigkeitsklasse und Schiene festlegen |
| `hiwin_rail_MGNR12R150HM` | 4 | HIWIN MGNR12R150HM Führungsschiene | **KLÄREN** | Ausführung und Schienenlänge/Endbearbeitung bestätigen |
| `hiwin_slide_MGN12CZ0H` | 4 | HIWIN MGN12CZ0H Führungswagen | **KLÄREN** | Exakte Suffixvariante und Paarung zur Schiene bestätigen |
| `nanotec_nema_14_ST3518M1004-A` | 8 | Nanotec ST3518M1004-A, NEMA-14-Schrittmotor | **KLÄREN** | Nur im Nanotec-Archiv gefunden; Verfügbarkeit/Ersatz prüfen |
| `nanotec_nema_17_ST4118M1804-A` | 12 | Nanotec ST4118M1804-A, NEMA-17-Schrittmotor | **MODELL BELEGT** | Motorzahl mit vier Achseinheiten abgleichen |
| `rod_slide_d10_l19` | 16 | Gleitlager Ø10 innen / Ø19 außen / Länge29mm | **KLÄREN** | Fusion:29mm lang; CAD-Name irreführend. RJ4JP-01-10 Kandidat, siehe neue Teileliste |
| `x_guiding_cpc_MR12M` | 2 | CPC MR12M X-Führungsschiene | **KLÄREN** | Länge und genaue Ausführung fehlen im Namen |

## Energieketten, Riemen und Kaufmechanik (14 Positionen)

| CAD-Name | Stück | Beschreibung | Status | Vor Bestellung |
|---|---:|---|---|---|
| `drag_chain_0_24m_E2i_10_10_028_0_4` | 16 | igus E2i.10 Energieketten-Abschnitt 0.24 m | **KLÄREN** | Gliederzahl, Länge und Endanschlüsse bestätigen |
| `drag_chain_0_28m_E2i_10_20_028_0_igus` | 8 | igus E2i.10 Energieketten-Abschnitt 0.28 m | **KLÄREN** | Gliederzahl, Länge und Endanschlüsse bestätigen |
| `handle_l100_dold` | 1 | Schubladengriff L100 | **KLÄREN** | Befestigungsabstand und Lieferant bestätigen |
| `hinged_M6_40_dold` | 4 | Gelenkfuß M6/40 | **KLÄREN** | Fußdurchmesser, Gewindelänge und Lieferant bestätigen |
| `mean_well_MHS-012_mounting_bracket` | 4 | Mean Well MHS-012 Montagewinkel | **KLÄREN** | Modellzuordnung und Bestellbarkeit prüfen |
| `pulley_gt2_9mm` | 8 | GT2-Riemenscheibe für 9-mm-Riemen | **KLÄREN** | Zähnezahl, Bohrung und Befestigung fehlen |
| `pulley_gt2_z16_6mm` | 12 | GT2-Riemenscheibe 16 Zähne / 6 mm | **KLÄREN** | Bohrung und Befestigung fehlen |
| `return_pulley_gt2_z16_6mm` | 20 | GT2-Umlenkrolle 16 Zähne / 6 mm | **KLÄREN** | Lager/Bohrung und Befestigung fehlen |
| `rod_holder_flange_d10_dold` | 16 | Flanschhalter für Ø10-mm-Stange | **KLÄREN** | Lochbild und Bauform bestätigen |
| `screw_on_bracket_30_6` | 26 | Anschraubwinkel 30/6 | **KLÄREN** | Profilserie und Lochbild bestätigen |
| `telescopic_bar_tsaa514613-350` | 2 | Teleskopschiene TSAA514613-350 | **KLÄREN** | Hersteller, Traglast und Lieferform bestätigen |
| `x_belt` | 8 | GT2-Riemen X-Achse | **KLÄREN** | Breite und Länge aus Konstruktion ermitteln |
| `y_belt` | 4 | GT2-Riemen Y-Achse | **KLÄREN** | Breite und Länge aus Konstruktion ermitteln |
| `z_drive_belt` | 4 | GT2-Riemen Z-Achse | **KLÄREN** | Breite und Länge aus Konstruktion ermitteln |

## Normteile und Befestigung (24 Positionen)

| CAD-Name | Stück | Beschreibung | Status | Vor Bestellung |
|---|---:|---|---|---|
| `din_466_knurled_nut_high_m4` | 8 | DIN 466 Rändelmutter hoch M4 | **KLÄREN** | Werkstoff/Festigkeitsklasse und Liefermenge prüfen |
| `din_562_m3_square_nut` | 8 | DIN 562 M3 Vierkantmutter | **KLÄREN** | Werkstoff/Festigkeitsklasse und Liefermenge prüfen |
| `din_562_m4_square_nut` | 12 | DIN 562 M4 Vierkantmutter | **KLÄREN** | Werkstoff/Festigkeitsklasse und Liefermenge prüfen |
| `din_7991_m3x8` | 32 | DIN 7991 M3×8 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_7991_m6x12` | 16 | DIN 7991 M6×12 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_7991_m6x14` | 6 | DIN 7991 M6×14 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_7991_m6x20` | 22 | DIN 7991 M6×20 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m3x10` | 76 | DIN 912 M3×10 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m3x12` | 8 | DIN 912 M3×12 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m3x14` | 4 | DIN 912 M3×14 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m3x16` | 28 | DIN 912 M3×16 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m3x18` | 32 | DIN 912 M3×18 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m3x20` | 4 | DIN 912 M3×20 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m3x30` | 8 | DIN 912 M3×30 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m3x8` | 52 | DIN 912 M3×8 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m4x10` | 1 | DIN 912 M4×10 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m4x20` | 20 | DIN 912 M4×20 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m4x30` | 36 | DIN 912 M4×30 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m5x10` | 32 | DIN 912 M5×10 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_912_m5x14` | 4 | DIN 912 M5×14 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `din_933_m4x20` | 8 | DIN 933 M4×20 | **KLÄREN** | Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen |
| `iso_8673_nut_m3` | 44 | ISO 8673 Mutter M3 | **KLÄREN** | Werkstoff/Festigkeitsklasse und Liefermenge prüfen |
| `iso_8673_nut_m4` | 64 | ISO 8673 Mutter M4 | **KLÄREN** | Werkstoff/Festigkeitsklasse und Liefermenge prüfen |
| `iso_8673_nut_m8` | 48 | ISO 8673 Mutter M8 | **KLÄREN** | Werkstoff/Festigkeitsklasse und Liefermenge prüfen |

## CAD-Fertigungsteile (61 Positionen)

| CAD-Name | Stück | Beschreibung | Status | Vor Bestellung |
|---|---:|---|---|---|
| `TR10x2_GT2_belt_adapter` | 4 | TR10x2 GT2 Riemen Adapter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `TR10x2_GT2_belt_adapter_cover` | 4 | TR10x2 GT2 Riemen Adapter Abdeckung | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_back_plate` | 1 | Grundgestell: Rückseite Platte | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_cable_holder_m3_flat` | 2 | Grundgestell: Kabel Halter M3 flach | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_cable_holder_m4` | 1 | Grundgestell: Kabel Halter M4 | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_cable_holder_m5_flat` | 4 | Grundgestell: Kabel Halter M5 flach | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_cover_long_side` | 2 | Grundgestell: Abdeckung lang Seite | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_cover_top` | 2 | Grundgestell: Abdeckung oben | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_drag_chain_holder` | 4 | Grundgestell: Schlepp Energiekette Halter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_drawer_long_side` | 2 | Grundgestell: Schublade lang Seite | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_frame_long_side` | 3 | Grundgestell: Rahmen lang Seite | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_frame_short` | 8 | Grundgestell: Rahmen kurz | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_frame_side` | 2 | Grundgestell: Rahmen Seite | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_nema_14_to_17_adapter` | 12 | Grundgestell: NEMA 14 auf 17 Adapter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_plate_adapter_1` | 2 | Grundgestell: Platte Adapter 1 | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_plate_adapter_2` | 2 | Grundgestell: Platte Adapter 2 | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_plate_adapter_left` | 2 | Grundgestell: Platte Adapter links | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_plate_adapter_right` | 2 | Grundgestell: Platte Adapter rechts | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `base_vertical` | 4 | Grundgestell: vertikal | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `belt_tightener_GT2_base` | 20 | Riemen Spanner GT2 Basis | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `belt_tightener_GT2_wing` | 20 | Riemen Spanner GT2 Flügel | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `cable_cover` | 4 | Kabel Abdeckung | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `camera_holder` | 1 | Kamera Halter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `camera_holder_top` | 1 | Kamera Halter oben | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `pcb_holder_glider` | 4 | Platine Halter Gleiter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `pcb_holder_guiding_holder_round_d10` | 4 | Platine Halter Führung Halter rund d10 | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `pcb_holder_guiding_round` | 2 | Platine Halter Führung rund | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `pcb_holder_rect_rod` | 2 | Platine Halter rechteckig Stange | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `pcb_holder_rod_short_round_d10` | 2 | Platine Halter Stange kurz rund d10 | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `pcb_holder_rod_short_round_d10_mirrored` | 2 | Platine Halter Stange kurz rund d10 gespiegelt | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `power_switch_holder` | 1 | Stromversorgung Schalter Halter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `signal_multiplexer_holder` | 1 | Signal-Multiplexer Halter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_belt_holder` | 4 | X-Achse Riemen Halter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_belt_holder_1` | 12 | X-Achse Riemen Halter 1 | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_drag_chain_adapter` | 8 | X-Achse Schlepp Energiekette Adapter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_end_stop_holder_side_short` | 4 | X-Achse Endschalter Halter Seite kurz | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_end_stop_holder_top_long` | 4 | X-Achse Endschalter Halter oben lang | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_end_stop_top_long` | 4 | X-Achse Endschalter oben lang | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_end_stop_top_short` | 4 | X-Achse Endschalter oben kurz | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_motor_plate` | 1 | X-Achse Motor Platte | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_motor_plate_2` | 1 | X-Achse Motor Platte 2 | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_round_rail` | 8 | X-Achse rund Schiene | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_side_plate` | 4 | X-Achse Seite Platte | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_side_plate_moving` | 4 | X-Achse Seite Platte beweglich | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_slide_inductive_endstop_adapter` | 4 | X-Achse Schlitten induktiv Endschalter Adapter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_slide_inductive_endstop_adapter_mirrored` | 4 | X-Achse Schlitten induktiv Endschalter Adapter gespiegelt | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `x_slide_stiffener_beam` | 4 | X-Achse Schlitten Versteifung Träger | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `y_camera_holder` | 2 | Y-Achse Kamera Halter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `y_camera_holder_compact` | 2 | Y-Achse Kamera Halter kompakt | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `y_slide` | 2 | Y-Achse Schlitten | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `y_slide_distance_rod` | 8 | Y-Achse Schlitten Abstand Stange | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `y_slide_distance_tube_2mm` | 4 | Y-Achse Schlitten Abstand Rohr 2mm | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `y_slide_mirrored` | 2 | Y-Achse Schlitten gespiegelt | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `y_slide_mirrored_top` | 2 | Y-Achse Schlitten gespiegelt oben | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `y_slide_top` | 2 | Y-Achse Schlitten oben | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `z_drive_belt_holder_v3` | 4 | Z-Achse Antrieb Riemen Halter v3 | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `z_probe_tip_pcb_holder` | 2 | Z-Achse Prüfspitze Platine Halter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `z_probe_tip_pcb_holder_long` | 2 | Z-Achse Prüfspitze Platine Halter lang | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `z_slide_cable_holder` | 4 | Z-Achse Schlitten Kabel Halter | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `z_slide_end_stop_trigger.psm` | 2 | Z-Achse Schlitten Endschalter Auslöser | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |
| `z_slide_end_stop_trigger_mirrored.psm` | 2 | Z-Achse Schlitten Endschalter Auslöser gespiegelt | **FERTIGEN** | Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen |

## Platzhalter und Modell-Dummys (3 Positionen)

| CAD-Name | Stück | Beschreibung | Status | Vor Bestellung |
|---|---:|---|---|---|
| `base_drawer_dummy_plate` | 1 | Schubladen-Dummyplatte | **PLATZHALTER** | Prüfen, ob reale Schubladenplatte benötigt wird |
| `pcb_dummy` | 1 | Prüfobjekt-Platzhalter im CAD | **PLATZHALTER** | Kein Maschinenteil; nicht bestellen |
| `signal_multiplexer_dummy` | 1 | Multiplexer-Platzhalter im CAD | **PLATZHALTER** | Echte Multiplexer-Platine samt Schaltplan/BOM fehlt |

## Abgrenzung

Alle 120 Blattteil-Namen aus dem Modell sind oben aufgeführt. Die zusätzliche [CSV-Inventur](cad-inventory.csv) enthält auch 14 Baugruppennamen (53 Vorkommen), damit keine Baugruppe doppelt gezählt wird. Die Klassifikation ist eine Beschaffungshilfe; sie ersetzt keine technische Freigabe des CAD-Modells.
