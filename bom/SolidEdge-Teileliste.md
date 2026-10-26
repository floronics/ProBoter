# Solid-Edge-Teileliste (SCHUTZWERK-Original)

Stand 26.10.2026. Quelle: SCHUTZWERK-CAD in [hardware/cad](../hardware/cad) (Solid Edge). Druck-, Mechanik- und Platinenteile wurden in Fusion importiert und vermessen ([solidedge-geometry.json](evidence/solidedge-geometry.json)). Normteile sind nur über den Dateinamen zugeordnet. „Menge Gesamtmodell“ = Vorkommen in `proboter.stp`, „Planmenge“ und „Unsere Gruppe“ aus der [Teileliste](Teileliste.md). [CSV](SolidEdge-Teileliste.csv)

**Abgleich:** 119 Teile OK, 1 Abweichungen, 36 Teile nur als Solid-Edge-Datei (nicht im Gesamtmodell), 19 Baugruppen.

**Regel:** printed_parts = selbst drucken (PETG), mechanical_parts = Werkstatt/Zuschnitt oder Kaufprofil (Motorhalteplatten CAD-096/097 und Seitenplatten CAD-099/100 selbst gefräst), standard_parts = kaufen. Der Signal-Multiplexer ist kein Druck- oder Kaufteil mehr, sondern die Platine aus [hardware/signal-multiplexer](../hardware/signal-multiplexer) (Bestellung bei JLCPCB, Gerber `gerber1.1`).

## Druckteile (printed_parts)

| Datei | ID | Bezeichnung | Menge Gesamtmodell | Planmenge | Unsere Gruppe | Hülle mm | Volumen cm³ | Abgleich | Hinweis |
|---|---|---|---|---|---|---|---|---|---|
| base_cable_holder_m3_flat.par | CAD-004 | Grundgestell: Kabel Halter M3 flach | 2 | 2 | 3D-Druck intern | 18 x 10 x 8 | 0.966 | OK |  |
| base_cable_holder_m4.par | CAD-005 | Grundgestell: Kabel Halter M4 | 1 | 1 | 3D-Druck intern | 18 x 12 x 10.5 | 1.508 | OK |  |
| base_cable_holder_m5_flat.par | CAD-006 | Grundgestell: Kabel Halter M5 flach | 4 | 4 | 3D-Druck intern | 18 x 14 x 10 | 1.497 | OK |  |
| base_drag_chain_holder.par | CAD-009 | Grundgestell: Schlepp Energiekette Halter | 4 | 4 | Weitere Fertigung | 80 x 650 x 16 | 606.011 | ABWEICHUNG | liegt in printed_parts, ist aber 650 mm lang, Material Alu 7075, zusätzlich .psm und Zeichnung in mechanical_parts: nicht am Stück druckbar, bleibt Alu-Flachprofil |
| base_nema_14_to_17_adapter.par | CAD-015 | Grundgestell: NEMA 14 auf 17 Adapter | 12 | 12 | 3D-Druck intern | 40 x 45 x 52 | 20.243 | OK |  |
| base_plate_adapter_1.par | CAD-016 | Grundgestell: Platte Adapter 1 | 2 | 2 | 3D-Druck intern | 130.4 x 10 x 91 | 75.205 | OK |  |
| base_plate_adapter_2.par | CAD-017 | Grundgestell: Platte Adapter 2 | 2 | 2 | 3D-Druck intern | 130.5 x 10 x 91 | 74.712 | OK |  |
| base_plate_adapter_left.par | CAD-018 | Grundgestell: Platte Adapter links | 2 | 2 | 3D-Druck intern | 162 x 10 x 67.08 | 49.256 | OK |  |
| base_plate_adapter_right.par | CAD-019 | Grundgestell: Platte Adapter rechts | 2 | 2 | 3D-Druck intern | 162 x 10 x 67.08 | 49.256 | OK |  |
| belt_tightener_GT2_base.par | CAD-021 | Riemen Spanner GT2 Basis | 20 | 20 | 3D-Druck intern | 44 x 35 x 20 | 10.843 | OK |  |
| belt_tightener_GT2_wing.par | CAD-022 | Riemen Spanner GT2 Flügel | 20 | 20 | 3D-Druck intern | 40 x 20 x 10 | 4.904 | OK |  |
| cable_cover.par | CAD-024 | Kabel Abdeckung | 4 | 4 | 3D-Druck intern | 22 x 58 x 3 | 1.121 | OK |  |
| calibration_plate.asm |  |  |  |  |  | 148 x 198 x 18 | 106.636 | Baugruppe | Kalibrierplatte v1 (gedruckt) |
| camera_holder.par | CAD-025 | Kamera Halter | 1 | 1 | 3D-Druck intern | 37 x 42 x 19 | 7.664 | OK |  |
| camera_holder_top.par | CAD-026 | Kamera Halter oben | 1 | 1 | 3D-Druck intern | 104 x 56.63 x 5 | 11.238 | OK |  |
| pcb_holder_glider.par | CAD-067 | Platine Halter Gleiter | 4 | 4 | 3D-Druck intern | 24 x 30 x 18 | 7.265 | OK |  |
| pcb_holder_guiding_holder_round_d10.par | CAD-068 | Platine Halter Führung Halter rund d 10 | 4 | 4 | 3D-Druck intern | 37 x 14 x 26.5 | 6.962 | OK |  |
| pcb_holder_rod_short_round_d10.par | CAD-071 | Platine Halter Stange kurz rund d 10 | 2 | 2 | 3D-Druck intern | 30 x 30 x 18 | 9.311 | OK |  |
| pcb_holder_rod_short_round_d10_mirrored.par | CAD-072 | Platine Halter Stange kurz rund d 10 gespiegelt | 2 | 2 | 3D-Druck intern | 30 x 30 x 18 | 9.311 | OK |  |
| power_switch_holder.par | CAD-074 | Stromversorgung Schalter Halter | 1 | 1 | 3D-Druck intern | 65 x 30 x 41 | 22.245 | OK |  |
| signal_multiplexer_holder.par | CAD-083 | Signal-Multiplexer Halter | 1 | 1 | 3D-Druck intern | 117 x 103 x 45 | 35.447 | OK |  |
| TR10x2_GT2_belt_adapter.par | CAD-001 | Y-Riemenklemme (CAD-Name TR10x 2 GT2 Adapter) | 4 | 4 | 3D-Druck intern | 15 x 20 x 22 | 3.982 | OK |  |
| TR10x2_GT2_belt_adapter_cover.par | CAD-002 | Y-Riemenklemme, Deckel | 4 | 4 | 3D-Druck intern | 7 x 20 x 20.49 | 1.77 | OK |  |
| x_belt_holder.par | CAD-088 | X-Achse Riemen Halter | 4 | 4 | 3D-Druck intern | 47 x 20 x 44 | 14.729 | OK |  |
| x_belt_holder_1.par | CAD-089 | X-Achse Riemen Halter 1 | 12 | 12 | 3D-Druck intern | 35 x 20 x 44 | 12.473 | OK |  |
| x_drag_chain_adapter.par | CAD-090 | X-Achse Schlepp Energiekette Adapter | 8 | 8 | 3D-Druck intern | 45.7 x 30 x 7 | 5.763 | OK |  |
| x_end_stop_holder_side_short.par | CAD-091 | X-Achse Endschalter Halter Seite kurz | 4 | 4 | 3D-Druck intern | 12 x 68.5 x 12 | 6.097 | OK |  |
| x_end_stop_holder_top_long.par | CAD-092 | X-Achse Endschalter Halter oben lang | 4 | 4 | 3D-Druck intern | 15 x 98.5 x 18.2 | 13.721 | OK |  |
| x_slide_inductive_endstop_adapter.par | CAD-101 | X-Achse Schlitten induktiv Endschalter Adapter | 4 | 4 | 3D-Druck intern | 20.5 x 50 x 48.5 | 12.154 | OK |  |
| x_slide_inductive_endstop_adapter_mirrored.par | CAD-102 | X-Achse Schlitten induktiv Endschalter Adapter gespiegelt | 4 | 4 | 3D-Druck intern | 20.5 x 50 x 48.5 | 12.154 | OK |  |
| y_camera_holder.par | CAD-105 | Y-Achse Kamera Halter | 2 | 2 | 3D-Druck intern | 50.82 x 51 x 35 | 23.701 | OK |  |
| y_camera_holder_compact.par | CAD-106 | Y-Achse Kamera Halter kompakt | 2 | 2 | 3D-Druck intern | 55.98 x 42 x 40 | 14.609 | OK |  |
| y_slide.par | CAD-107 | Y-Achse Schlitten | 2 | 2 | 3D-Druck intern | 65 x 19.8 x 136 | 83.211 | OK | SE-Material: Aluminium, 7075-T6 |
| y_slide_distance_tube_2mm.par | CAD-109 | Y-Achse Schlitten Abstand Rohr 2 mm | 4 | 4 | 3D-Druck intern | 3 x 10 x 10 | 0.1 | OK |  |
| y_slide_mirrored.par | CAD-110 | Y-Achse Schlitten gespiegelt | 2 | 2 | 3D-Druck intern | 65 x 19.8 x 136 | 83.211 | OK | SE-Material: Aluminium, 7075-T6 |
| y_slide_mirrored_top.par | CAD-111 | Y-Achse Schlitten gespiegelt oben | 2 | 2 | 3D-Druck intern | 65 x 14 x 82 | 44.19 | OK |  |
| y_slide_top.par | CAD-112 | Y-Achse Schlitten oben | 2 | 2 | 3D-Druck intern | 65 x 14 x 82 | 44.19 | OK |  |
| z_drive_belt_holder_v3.par | CAD-114 | Z-Achse Antrieb Riemen Halter v 3 | 4 | 4 | 3D-Druck intern | 35 x 15 x 35 | 8.112 | OK |  |
| z_probe_tip_pcb_holder.par | CAD-116 | Z-Achse Prüfspitze Platine Halter | 2 | 2 | 3D-Druck intern | 79.38 x 16 x 12 | 8.592 | OK |  |
| z_probe_tip_pcb_holder_long.par | CAD-117 | Z-Achse Prüfspitze Platine Halter lang | 2 | 2 | 3D-Druck intern | 103.41 x 16 x 55 | 16.319 | OK |  |
| z_slide_cable_holder.par | CAD-118 | Z-Achse Schlitten Kabel Halter | 4 | 4 | 3D-Druck intern | 16 x 8 x 10 | 0.763 | OK |  |
| z_slide_end_stop_trigger.psm.par | CAD-119 | Z-Achse Schlitten Endschalter Auslöser | 2 | 2 | 3D-Druck intern | 9.05 x 22.5 x 15 | 0.31 | OK |  |
| z_slide_end_stop_trigger_mirrored.psm.par | CAD-120 | Z-Achse Schlitten Endschalter Auslöser gespiegelt | 2 | 2 | 3D-Druck intern | 9.05 x 22.5 x 15 | 0.31 | OK |  |

### Nur als Solid-Edge-Datei, nicht im Gesamtmodell (28)

Nicht in der Bestell-/Druckplanung. Bedarf je Teil entscheiden.

| Datei | Hülle mm | Volumen cm³ | Hinweis |
|---|---|---|---|
| base_drawer_drag_chain_holder.par | 52 x 30 x 10 | 10.374 | Schleppkettenhalter Schublade, ältere/alternative Variante |
| base_drawer_power_plug_socket.par | 102 x 24 x 30 | 30.008 | Halter Netzbuchse in der Schublade |
| base_nema_14_belt_drive_adapter_motor.par | 35 x 40 x 45 | 14.157 | NEMA14-Adapter Riemenantrieb, ältere Variante |
| base_power_supply_housing.par | 80 x 50 x 25 | 26.362 | Gehäuse kleines Netzteil (Baugruppe base_power_supply) |
| base_power_supply_housing_top.par | 50 x 50 x 2.5 | 6.008 | Deckel dazu |
| base_raspberry_pi_4_adapter.par | 97 x 72 x 5 | 34.47 | Halteplatte Raspberry Pi 4 |
| calibration_plate.par | 148 x 198 x 18 | 106.636 | Kalibrierplatte v1 (gedruckt) |
| calibration_plate_marker_fill.par | 18.2 x 1.9 x 18.2 | 0.527 | Markereinlage (Farbwechsel-Druck) |
| calibration_plate_marker_fill_001.par | 18.2 x 1.9 x 18.2 | 0.527 | Markereinlage ID 1 |
| calibration_plate_marker_fill_003.par | 18.2 x 1.9 x 18.2 | 0.51 | Markereinlage ID 3 |
| calibration_plate_marker_fill_006.par | 18.2 x 1.9 x 18.2 | 0.51 | Markereinlage ID 6 |
| calibration_plate_marker_fill_012.par | 18.2 x 1.9 x 18.2 | 0.527 | Markereinlage ID 12 |
| calibration_plate_pin.par | 10 x 10 x 8 | 0.316 | Kalibrierstift |
| calibration_plate_v2.par | 138 x 178 x 17 | 112.03 | Kalibrierplatte v2 |
| calibration_plate_v3.par | 100 x 140 x 17 | 66.626 | Kalibrierplatte v3 |
| calibration_plate_v4.par | 110 x 130 x 17 | 65.476 | Kalibrierplatte v4, neueste |
| drawer_drag_chain_holder.par | 120 x 25 x 40 | 31.445 | Schleppkettenhalter Schublade (Baugruppe drawer_drag_chain) |
| motor_adapter_nema_17.par | 40 x 45 x 52 | 20.243 | gleiche Geometrie wie base_nema_14_to_17_adapter (Duplikat) |
| pcb_holder_glider_slim_long.par | 44 x 15 x 18 | 8.024 | schmaler, langer Platinenhalter-Gleiter (Variante) |
| target_power_switch.par | 95 x 28 x 75 | 48.525 | Gehäuse Zielplatinen-Versorgungsschalter |
| target_power_switch_top.par | 95 x 75 x 6 | 24.043 | Deckel dazu |
| utils_height_leveling_probe_holder.par | 45 x 20 x 32 | 12.145 | Hilfsmittel: Halter für Höhennivellier-Taster |
| x_end_stop_holder_side_long.par | 12 x 69 x 54 | 10.953 | X-Endschalterhalter seitlich, lange Variante |
| y_camera_holder_mirrored.par | 50.82 x 51 x 35 | 23.701 | Y-Kamerahalter gespiegelt |
| z_pogo_pin_holder.par | 16 x 20.97 x 79.35 | 11.664 | Pogo-Pin-Halter (Prüfspitze ohne PCB) |
| z_pogo_pin_holder_cover.par | 16 x 1 x 4 | 0.052 | Deckel dazu |
| z_pogo_pin_holder_long.par | 16 x 53.39 x 108.6 | 16.198 | Pogo-Pin-Halter lang |
| z_pogo_pin_holder_long_mirrored.par | 16 x 53.39 x 108.6 | 16.198 | Pogo-Pin-Halter lang, gespiegelt |

## Mechanik und Werkstatt (mechanical_parts)

| Datei | ID | Bezeichnung | Menge Gesamtmodell | Planmenge | Unsere Gruppe | Hülle mm | Volumen cm³ | Abgleich | Hinweis |
|---|---|---|---|---|---|---|---|---|---|
| base.asm |  |  | 1 |  |  |  |  | Baugruppe |  |
| base_back_plate.par | CAD-003 | Grundgestell: Rückseite Platte | 1 | 1 | Blech intern | 650 x 3 x 270 | 519.941 | OK |  |
| base_cover_long_side.par | CAD-007 | Grundgestell: Abdeckung lang Seite | 2 | 2 | Kaufteile | 660 x 5 x 135.5 | 444.939 | OK |  |
| base_cover_top.par | CAD-008 | Grundgestell: Abdeckung oben | 2 | 2 | Kaufteile | 656 x 5 x 182.5 | 594.206 | OK |  |
| base_drawer_dummy_plate.par | CAD-010 | Schubladen-Dummyplatte | 1 | 1 | Ungeklärte Teile | 564 x 410 x 12 | 1586.78 | OK | Material im Solid-Edge-Modell: Birke 12 mm (Schubladenboden) |
| base_drawer_long_side.par | CAD-011 | Grundgestell: Schublade lang Seite | 2 | 2 | Weitere Fertigung | 30 x 564 x 30 | 313.87 | OK |  |
| base_frame_long_side.par | CAD-012 | Grundgestell: Rahmen lang Seite | 3 | 3 | Weitere Fertigung | 30 x 590 x 30 | 328.339 | OK |  |
| base_frame_short.par | CAD-013 | Grundgestell: Rahmen kurz | 8 | 8 | Weitere Fertigung | 30 x 350 x 30 | 194.777 | OK |  |
| base_frame_side.par | CAD-014 | Grundgestell: Rahmen Seite | 2 | 2 | Weitere Fertigung | 30 x 650 x 60 | 790.967 | OK |  |
| base_plate_adapter.asm |  |  | 2 |  |  |  |  | Baugruppe |  |
| base_power_supply.asm |  |  |  |  |  |  |  | Baugruppe |  |
| base_vertical.par | CAD-020 | Grundgestell: vertikal | 4 | 4 | Weitere Fertigung | 30 x 350 x 30 | 194.777 | OK |  |
| belt_tightener_GT2.asm |  |  | 20 |  |  |  |  | Baugruppe |  |
| camera_holder.asm | CAD-025 | Kamera Halter | 1 | 1 | 3D-Druck intern |  |  | Baugruppe |  |
| drawer_drag_chain.asm |  |  |  |  |  |  |  | Baugruppe |  |
| pcb_holder.asm |  |  | 1 |  |  |  |  | Baugruppe |  |
| pcb_holder_guiding_round.par | CAD-069 | Platine Halter Führung rund | 2 | 2 | Weitere Fertigung | 10 x 356.8 x 10 | 28.023 | OK |  |
| pcb_holder_rect_rod.par | CAD-070 | Platine Halter rechteckig Stange | 2 | 2 | Weitere Fertigung | 11.5 x 205 x 11.5 | 12.3 | OK |  |
| target_power_switch.asm |  |  |  |  |  |  |  | Baugruppe | Gehäuse Zielplatinen-Versorgungsschalter |
| x_belt.par | CAD-087 | GT2-Riemen X, 6 mm breit | 8 | 8 | Kaufteile | 710.3 x 6 x 11.3 | 11.833 | OK |  |
| x_belt_drive.asm |  |  | 8 |  |  |  |  | Baugruppe |  |
| x_end_stop_top_long.par | CAD-093 | X-Achse Endschalter oben lang | 4 | 4 | Weitere Fertigung | 125 x 8 x 8 | 6.277 | OK |  |
| x_end_stop_top_short.par | CAD-094 | X-Achse Endschalter oben kurz | 4 | 4 | Weitere Fertigung | 75 x 8 x 8 | 3.764 | OK |  |
| x_guiding_cpc_MR12M.par | CAD-095 | CPC MR12M Führungsschiene 600 mm | 2 | 2 | Kaufteile | 600 x 7.5 x 12 | 49.819 | OK |  |
| x_motor_plate.par | CAD-096 | X-Achse Motor Platte | 1 | 1 | Blech intern | 550 x 5 x 135 | 328.519 | OK |  |
| x_motor_plate_2.par | CAD-097 | X-Achse Motor Platte 2 | 1 | 1 | Blech intern | 550 x 5 x 135 | 328.382 | OK |  |
| x_round_rail.par | CAD-098 | X-Achse rund Schiene | 8 | 8 | Weitere Fertigung | 10 x 450 x 10 | 35.335 | OK |  |
| x_side_plate.par | CAD-099 | X-Achse Seite Platte | 4 | 4 | Blech intern | 55 x 5 x 166.5 | 40.663 | OK | SE-Material: S355MC |
| x_side_plate_moving.par | CAD-100 | X-Achse Seite Platte beweglich | 4 | 4 | Blech intern | 55 x 5 x 166.5 | 41.473 | OK | SE-Material: S355MC |
| x_slide.asm |  |  | 4 |  |  |  |  | Baugruppe |  |
| x_slide_stiffener_beam.par | CAD-103 | X-Achse Schlitten Versteifung Träger | 4 | 4 | Weitere Fertigung | 40 x 436 x 16 | 194.502 | OK |  |
| y_belt.par | CAD-104 | GT2-Riemen Y, 6 mm breit | 4 | 4 | Kaufteile | 503.3 x 6 x 11.3 | 8.406 | OK |  |
| y_belt_drive.asm |  |  | 4 |  |  |  |  | Baugruppe |  |
| y_slide.asm | CAD-107 | Y-Achse Schlitten | 2 | 2 | 3D-Druck intern |  |  | Baugruppe |  |
| y_slide_distance_rod.par | CAD-108 | Y-Achse Schlitten Abstand Stange | 8 | 8 | Weitere Fertigung | 4 x 70 x 4 | 0.877 | OK |  |
| y_slide_mirrored.asm | CAD-110 | Y-Achse Schlitten gespiegelt | 2 | 2 | 3D-Druck intern |  |  | Baugruppe |  |
| z_drive_belt.par | CAD-113 | GT2-Riemen Z, 9 mm breit | 4 | 4 | Kaufteile | 11.3 x 9 x 119.3 | 3.07 | OK |  |
| z_slide.asm |  |  | 2 |  |  |  |  | Baugruppe |  |
| z_slide_long.asm |  |  | 2 |  |  |  |  | Baugruppe |  |

### Nur als Solid-Edge-Datei, nicht im Gesamtmodell (4)

Nicht in der Bestell-/Druckplanung. Bedarf je Teil entscheiden.

| Datei | Hülle mm | Volumen cm³ | Hinweis |
|---|---|---|---|
| x_motor_plate_2_raw.par | 550 x 5 x 135 | 331.193 | Rohteil zur gefrästen Motorplatte CAD-097 |
| x_motor_plate_raw.par | 550 x 5 x 135 | 331.33 | Rohteil zur gefrästen Motorplatte CAD-096 |
| x_side_plate_moving_raw.par | 55 x 5 x 166.5 | 41.898 | Rohteil zur gefrästen Seitenplatte CAD-100 |
| x_side_plate_raw.par | 55 x 5 x 166.5 | 41.091 | Rohteil zur gefrästen Seitenplatte CAD-099; SE-Material: Aluminium, 7075-T6 |

## Kaufteile (standard_parts)

| Datei | ID | Bezeichnung | Menge Gesamtmodell | Planmenge | Unsere Gruppe | Hülle mm | Volumen cm³ | Abgleich | Hinweis |
|---|---|---|---|---|---|---|---|---|---|
| bigtreetech_skr_v1_3.par | CAD-023 | Steuerplatine, ERSATZ: BIGTREETECH SKR 1.4 Turbo statt SKR V1.3 | 4 | 4 | Kaufteile |  |  | OK |  |
| cpc_MR12ML.par | CAD-027 | CPC MR12ML Führungswagen | 8 | 8 | Kaufteile |  |  | OK |  |
| din_466_knurled_nut_high_m4.par | CAD-028 | DIN 466 Rändelmutter hoch M4 | 8 | 10 | Kaufteile |  |  | OK |  |
| din_562_m3_square_nut.par | CAD-029 | DIN 562 M3 Vierkantmutter | 8 | 10 | Kaufteile |  |  | OK |  |
| din_562_m4_square_nut.par | CAD-030 | DIN 562 M4 Vierkantmutter | 12 | 14 | Kaufteile |  |  | OK |  |
| din_7991_m3x8.par | CAD-031 | DIN 7991 M3×8 | 32 | 36 | Kaufteile |  |  | OK |  |
| din_7991_m6x12.par | CAD-032 | DIN 7991 M6×12 | 16 | 18 | Kaufteile |  |  | OK |  |
| din_7991_m6x14.par | CAD-033 | DIN 7991 M6×14 | 6 | 8 | Kaufteile |  |  | OK |  |
| din_7991_m6x20.par | CAD-034 | DIN 7991 M6×20 | 22 | 25 | Kaufteile |  |  | OK |  |
| din_912_m3x10.par | CAD-035 | DIN 912 M3×10 | 76 | 84 | Kaufteile |  |  | OK |  |
| din_912_m3x12.par | CAD-036 | DIN 912 M3×12 | 8 | 10 | Kaufteile |  |  | OK |  |
| din_912_m3x14.par | CAD-037 | DIN 912 M3×14 | 4 | 6 | Kaufteile |  |  | OK |  |
| din_912_m3x16.par | CAD-038 | DIN 912 M3×16 | 28 | 31 | Kaufteile |  |  | OK |  |
| din_912_m3x18.par | CAD-039 | DIN 912 M3×18 | 32 | 36 | Kaufteile |  |  | OK |  |
| din_912_m3x20.par | CAD-040 | DIN 912 M3×20 | 4 | 6 | Kaufteile |  |  | OK |  |
| din_912_m3x30.par | CAD-041 | DIN 912 M3×30 | 8 | 10 | Kaufteile |  |  | OK |  |
| din_912_m3x8.par | CAD-042 | DIN 912 M3×8 | 52 | 58 | Kaufteile |  |  | OK |  |
| din_912_m4x10.par | CAD-043 | DIN 912 M4×10 | 1 | 3 | Kaufteile |  |  | OK |  |
| din_912_m4x20.par | CAD-044 | DIN 912 M4×20 | 20 | 22 | Kaufteile |  |  | OK |  |
| din_912_m4x30.par | CAD-045 | DIN 912 M4×30 | 36 | 40 | Kaufteile |  |  | OK |  |
| din_912_m5x10.par | CAD-046 | DIN 912 M5×10 | 32 | 36 | Kaufteile |  |  | OK |  |
| din_912_m5x14.par | CAD-047 | DIN 912 M5×14 | 4 | 6 | Kaufteile |  |  | OK |  |
| din_933_m4x20.par | CAD-048 | DIN 933 M4×20 | 8 | 10 | Kaufteile |  |  | OK |  |
| drag_chain_0_24m_E2i_10_10_028_0_4.par | CAD-049 | igus E2i.10.10.028.0, 16 kurze Abschnitte | 16 | 16 | Kaufteile |  |  | OK |  |
| drag_chain_0_28m_E2i_10_20_028_0_igus.par | CAD-050 | igus E2i.10.20.028.0, 8 lange Abschnitte | 8 | 8 | Kaufteile |  |  | OK |  |
| handle_l100_dold.par | CAD-051 | Schubladengriff DOLD A-75873, Lochabstand 100 mm | 1 | 1 | Kaufteile |  |  | OK |  |
| hinged_M6_40_dold.par | CAD-052 | Gelenkfuß M6×20 / Teller Ø40 mm | 4 | 4 | Kaufteile |  |  | OK |  |
| hiwin_rail_MGNR12R150HM.par | CAD-053 | HIWIN MGNR12R150HM, Z-Schiene 150 mm | 4 | 4 | Kaufteile |  |  | OK |  |
| hiwin_slide_MGN12CZ0H.par | CAD-054 | HIWIN MGN12CZ0HM Z-Führungswagen | 4 | 4 | Kaufteile |  |  | OK |  |
| inductive_proximity_sensor_m8.par | CAD-055 | Induktiver Näherungsschalter ELCO NI4-M08-ON6L-Q8 (AUSWAHL, Original unbekannt) | 24 | 24 | Kaufteile |  |  | OK |  |
| iso_8673_nut_m3.par | CAD-056 | Sechskantmutter DIN 934 M3 A2 | 44 | 49 | Kaufteile |  |  | OK |  |
| iso_8673_nut_m4.par | CAD-057 | Sechskantmutter DIN 934 M4 A2 | 64 | 71 | Kaufteile |  |  | OK |  |
| iso_8673_nut_m8.par | CAD-058 | ISO 8673 Mutter M8 | 48 | 53 | Kaufteile |  |  | OK |  |
| mean_well_MHS-012_mounting_bracket.par | CAD-059 | Mean Well MHS012 Montagewinkel | 4 | 4 | Kaufteile |  |  | OK |  |
| mean_well_RSP-200-24.par | CAD-060 | Mean Well RSP-200-24 Netzteil,24 V/8,4 A | 1 | 1 | Kaufteile |  |  | OK |  |
| mmcx_male_end.par | CAD-061 | MMCX-Stecker gerade mit RG316, offenes Ende | 4 | 4 | Kaufteile |  |  | OK |  |
| mmcx_male_end_with_angle.par | CAD-062 | MMCX-Stecker gewinkelt mit RG316, offenes Ende | 4 | 4 | Kaufteile |  |  | OK |  |
| nanotec_nema_14_ST3518M1004-A.par | CAD-063 | NEMA14 Z-Motor, ERSATZ: STEPPERONLINE 14HS13-0804S statt Nanotec ST3518M1004-A | 8 | 4 | Kaufteile |  |  | OK |  |
| nanotec_nema_17_ST4118M1804-A.par | CAD-064 | Nanotec ST4118M1804-A NEMA17 X/Y-Motor | 12 | 12 | Kaufteile |  |  | OK |  |
| optical_endstop.par | CAD-065 | Optischer Endschalter 11×35 mm | 4 | 4 | Kaufteile |  |  | OK |  |
| plug_sleeve_P75-2_W.par | CAD-073 | Aufnahmehülse R75 mit Drahtende (CAD: P75-2_W) | 8 | 8 | Kaufteile |  |  | OK |  |
| pulley_gt2_9mm.par | CAD-076 | GT2-Zahnscheibe Z16 / 9 mm / Bohrung 5 mm, ANPASSUNG | 8 | 8 | Kaufteile |  |  | OK |  |
| pulley_gt2_z16_6mm.par | CAD-077 | GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm | 12 | 12 | Kaufteile |  |  | OK |  |
| return_pulley_gt2_z16_6mm.par | CAD-078 | GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm | 20 | 20 | Kaufteile |  |  | OK |  |
| rod_holder_flange_d10_dold.par | CAD-079 | SHF10 Flanschhalter fürØ10 mm Welle | 16 | 16 | Kaufteile |  |  | OK |  |
| rod_slide_d10_l19.par | CAD-080 | GleitbuchseØ10 innen / Ø19 außen / Länge 29 mm | 16 | 16 | Kaufteile |  |  | OK |  |
| screw_on_bracket_30_6.par | CAD-081 | Anschraubwinkel 30 / Nut 6 | 26 | 26 | Kaufteile |  |  | OK |  |
| signal_multiplexer_dummy.par | CAD-082 | Multiplexer-Platzhalter im CAD | 1 | 0 | Nicht benötigt |  |  | OK | erledigt: echte Platine in hardware/signal-multiplexer, Bestellung SYS-003/023 bei JLCPCB |
| telescopic_bar_tsaa514613-350.par | CAD-084 | Teleskopschiene 350 mm, Vollauszug | 2 | 2 | Kaufteile |  |  | OK |  |
| usb_microscope.par | CAD-085 | Bewegliches USB-Mikroskop Toolcraft 2 MP (AUSWAHL, ANPASSUNG) | 4 | 1 | Kaufteile |  |  | OK |  |
| vandalism_switch_d19.par | CAD-086 | Netzschalter Ø19 ONPOW LAS1 A-ZG24, rastend | 1 | 1 | Kaufteile |  |  | OK |  |
| z_pogo_pin.par | CAD-115 | Federkontakt P75-B1 (Nadelspitze, wie CAD) | 8 | 8 | Kaufteile |  |  | OK |  |

### Nur als Solid-Edge-Datei, nicht im Gesamtmodell (4)

Nicht in der Bestell-/Druckplanung. Bedarf je Teil entscheiden.

| Datei | Hülle mm | Volumen cm³ | Hinweis |
|---|---|---|---|
| drag_chain_0_5m_E2C_10_10_028_0___E2_100_10_56PZ_A1_1.par |  |  | Energiekette 0,5 m, nicht im Gesamtmodell |
| drag_chain_0_5m_E2C_10_10_028_0___E2_100_10_56PZ_A1_2.par |  |  | Energiekette 0,5 m, nicht im Gesamtmodell |
| mean_well_HRPG-1000-24 .par |  |  | Netzteil 1000 W, nicht im Gesamtmodell (verbaut: RSP-200-24) |
| raspberry_pi_4_dummy.par |  |  | Platzhalter Raspberry Pi 4 |

## Leiterplatten (pcbs)

| Datei | ID | Bezeichnung | Menge Gesamtmodell | Planmenge | Unsere Gruppe | Hülle mm | Volumen cm³ | Abgleich | Hinweis |
|---|---|---|---|---|---|---|---|---|---|
| probe_tip.asm |  |  | 2 |  |  |  |  | Baugruppe |  |
| probe_tip_pcb.par | CAD-075 | Prüfspitzen-PCB, unbestückt | 4 | 4 | PCB extern | 26.67 x 10.96 x 1.6 | 0.273 | OK |  |
| probe_tip_with_angle.asm |  |  | 2 |  |  |  |  | Baugruppe |  |

## Gesamtmodell

| Datei | ID | Bezeichnung | Menge Gesamtmodell | Planmenge | Unsere Gruppe | Hülle mm | Volumen cm³ | Abgleich | Hinweis |
|---|---|---|---|---|---|---|---|---|---|
| pcb_dummy.par | CAD-066 | Prüfobjekt-Platzhalter im CAD | 1 | 0 | Nicht benötigt |  |  | OK | Prüfling im Modell, kein Maschinenteil |
| probotor.asm |  |  |  |  |  |  |  | Baugruppe |  |
