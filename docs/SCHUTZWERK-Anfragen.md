# Offene Fragen an SCHUTZWERK

Sammelliste für Anfragen an SCHUTZWERK zum Nachbau. Stand 26.10.2026.
Neue Punkte unten in die passende Gruppe eintragen und den Status pflegen: `offen`, `angefragt <Datum>`, `beantwortet`.

## Fehlende Leiterplatten

| Nr. | Frage | Bezug | Status |
|---:|---|---|---|
| 1 | KiCad-Projekt oder Gerber, Schaltplan und Stückliste der Prüfspitzen-Platine (`probe_tip_pcb`, 26,67 × 10,96 × 1,6 mm, 4 Stück) | CAD-075, SYS-024 | angefragt 17.10.2026 |
| 2 | Schaltung, Layout und Firmware des Versorgungscontrollers für die Zielplatine (`/dev/proboter_target-power-controller`). Passt er in das Gehäuse `target_power_switch`? | SYS-026, SYS-067/068 | offen |
| 3 | Gibt es eine Platine für die Pegelanpassung der induktiven Sensoren (24 V auf SKR-Eingänge), oder wie sind sie angeschlossen? | SYS-019 | offen |
| 4 | Signal-Multiplexer: Werte für die unbestimmten Bauteile C3, C8, R3, R10, RN1–RN3, D4, D8, D11–D13, D14 und Y1 (Frequenz), MOSFET-Typ Q1–Q10 (SI2308CDS?), LED-Farben D1–D3 sowie das verwendete Aluminiumgehäuse | SYS-003/023, `hardware/signal-multiplexer` | offen |
| 5 | Ist `gerber1.1` der zuletzt gefertigte und funktionierende Stand des Multiplexers? | SYS-003 | offen |

## Elektronik und Verkabelung

| Nr. | Frage | Bezug | Status |
|---:|---|---|---|
| 6 | Wird ein Raspberry Pi 4 verbaut (`base_raspberry_pi_4_adapter`, `raspberry_pi_4_dummy`)? Wenn ja: Aufgabe, Stromversorgung, Speicher | SYS-071 | offen |
| 7 | Welches Netzteil oder welcher Wandler kommt in das kleine Gehäuse `base_power_supply_housing` (80 × 50 × 25 mm)? | SYS-069/070 | offen |
| 8 | Typ der Netzbuchse im Halter `base_drawer_power_plug_socket` (Kaltgerätebuchse mit Schalter oder Sicherung?) | SYS-066 | offen |
| 9 | Induktive Endschalter: Die BOM nennt 16 × M12 und 8 × M8, das CAD zeigt 24 × M8. Welche Typen (PNP/NPN, Schaltabstand, Stecker) sind verbaut? | CAD-055 | offen |
| 10 | Wofür ist das Netzteil Mean Well HRPG-1000-24 in `probotor.asm`? Verbaut ist laut STEP das RSP-200-24 | standard_parts | offen |

## Mechanik und Druckteile

| Nr. | Frage | Bezug | Status |
|---:|---|---|---|
| 11 | Kalibrierplatte v4: Sind die 4 `calibration_plate_pin` die weißen Außenreferenzen? Welche Materialien und Farben (Platte, Markereinlagen, Stifte)? Werden die Referenzzylinder aus Messing gefertigt? | SYS-061…063, SYS-005/039/040 | offen |
| 12 | Die Software rechnet mit 5,1 mm Plattendicke (`cli.py`), die v4-Platte ist 17 mm hoch. Welcher Wert gilt? | SYS-061 | offen |
| 13 | `base_drag_chain_holder` liegt in `printed_parts`, ist aber 650 mm lang, als Aluminium modelliert und hat zusätzlich eine Blechversion mit Zeichnung. Wie wurde er gefertigt? | CAD-009 | offen |
| 14 | Adapterplatten `base_plate_adapter_*` (10 mm, tragen die X-Riemenantriebe) und `camera_holder_top` liegen in `printed_parts`: Wurden sie wirklich gedruckt, und mit welchem Material und welcher Füllung? | CAD-016…019, CAD-026 | offen |
| 15 | Motorhalteplatten und Seitenplatten: Werkstoff (Modell: S355MC bzw. Aluminium 7075) und Fertigung (gelasert oder gefräst)? | CAD-096/097/099/100 | offen |
| 16 | Druckparameter der Druckteile: Material (PETG/PLA/ASA), Wandstärke und Füllung | MAT-001 | offen |
| 17 | Schubladenkette: genaue igus-Artikel (E2C.10.10.028.0, Anschlüsse E2.100.10.56PZ.A1) und Länge 0,5 m bestätigen | SYS-073/074 | offen |

## Fehlende CAD-Dateien

| Nr. | Frage | Bezug | Status |
|---:|---|---|---|
| 18 | Die Baugruppen verweisen auf Dateien, die nicht im Paket enthalten sind: `measuring_tool_x.asm`, `x_side_plate_v3.par`, `x_slide_v3_1.asm`, `z_slide_v2.asm`, `y_slide_mirrored_2.asm`, `probe_misumi_NP20.par`, `distance_sheet_metal_1mm.par`, `beld_holder_GT2_square_mount.par`, `x_slide_inductive_endstop_adapter_v2(_mirrored).par`. Sind das neuere Stände, die zum aktuellen Aufbau gehören? | `hardware/cad` | offen |
| 19 | Ist `proboter.stp` (19.04.2022) der aktuelle Aufbau, oder weicht der reale Roboter davon ab? | `hardware/3d_models` | offen |
