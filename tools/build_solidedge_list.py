"""Part list of SCHUTZWERK's Solid Edge files (hardware/cad), checked against bom/teileliste.csv.

Inputs: hardware/cad (file names), bom/evidence/solidedge-geometry.json (Fusion
measurement, tools/fusion_solidedge_measure.py), bom/cad-inventory.csv (STEP counts)
and bom/teileliste.csv (our classification). Output: bom/SolidEdge-Teileliste.md/.csv.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOM = ROOT / 'bom'
CAD_DIR = ROOT / 'hardware' / 'cad'

# What SCHUTZWERK's folder says about how a part is made
FOLDER_PROCESS = {'printed_parts': '3D-Druck', 'mechanical_parts': 'Werkstatt/Zuschnitt',
                  'standard_parts': 'Kaufteil', 'pcbs': 'Leiterplatte', 'cad': 'Gesamtmodell'}
EXPECTED_GROUPS = {'printed_parts': {'3D-Druck intern'},
                   'mechanical_parts': {'Blech intern', 'Weitere Fertigung', 'CNC extern', 'Kaufteile', 'Ungeklärte Teile'},
                   'standard_parts': {'Kaufteile'}, 'pcbs': {'PCB extern'}}

# Parts that exist only as Solid Edge files (not in proboter.stp): purpose and what to do
ONLY_SE = {
    'base_drawer_drag_chain_holder': 'Schleppkettenhalter Schublade, ältere/alternative Variante',
    'drawer_drag_chain_holder': 'Schleppkettenhalter Schublade (Baugruppe drawer_drag_chain)',
    'base_drawer_power_plug_socket': 'Halter Netzbuchse in der Schublade',
    'base_nema_14_belt_drive_adapter_motor': 'NEMA14-Adapter Riemenantrieb, ältere Variante',
    'motor_adapter_nema_17': 'gleiche Geometrie wie base_nema_14_to_17_adapter (Duplikat)',
    'base_power_supply_housing': 'Gehäuse kleines Netzteil (Baugruppe base_power_supply)',
    'base_power_supply_housing_top': 'Deckel dazu',
    'base_raspberry_pi_4_adapter': 'Halteplatte Raspberry Pi 4',
    'calibration_plate': 'Kalibrierplatte v1 (gedruckt)',
    'calibration_plate_v2': 'Kalibrierplatte v2',
    'calibration_plate_v3': 'Kalibrierplatte v3',
    'calibration_plate_v4': 'Kalibrierplatte v4, neueste',
    'calibration_plate_pin': 'Kalibrierstift',
    'calibration_plate_marker_fill': 'Markereinlage (Farbwechsel-Druck)',
    'calibration_plate_marker_fill_001': 'Markereinlage ID 1',
    'calibration_plate_marker_fill_003': 'Markereinlage ID 3',
    'calibration_plate_marker_fill_006': 'Markereinlage ID 6',
    'calibration_plate_marker_fill_012': 'Markereinlage ID 12',
    'target_power_switch': 'Gehäuse Zielplatinen-Versorgungsschalter',
    'target_power_switch_top': 'Deckel dazu',
    'pcb_holder_glider_slim_long': 'schmaler, langer Platinenhalter-Gleiter (Variante)',
    'utils_height_leveling_probe_holder': 'Hilfsmittel: Halter für Höhennivellier-Taster',
    'x_end_stop_holder_side_long': 'X-Endschalterhalter seitlich, lange Variante',
    'y_camera_holder_mirrored': 'Y-Kamerahalter gespiegelt',
    'z_pogo_pin_holder': 'Pogo-Pin-Halter (Prüfspitze ohne PCB)',
    'z_pogo_pin_holder_cover': 'Deckel dazu',
    'z_pogo_pin_holder_long': 'Pogo-Pin-Halter lang',
    'z_pogo_pin_holder_long_mirrored': 'Pogo-Pin-Halter lang, gespiegelt',
    'x_motor_plate_raw': 'Rohteil zur gefrästen Motorplatte CAD-096',
    'x_motor_plate_2_raw': 'Rohteil zur gefrästen Motorplatte CAD-097',
    'x_side_plate_raw': 'Rohteil zur gefrästen Seitenplatte CAD-099',
    'x_side_plate_moving_raw': 'Rohteil zur gefrästen Seitenplatte CAD-100',
    'drag_chain_0_5m_E2C_10_10_028_0___E2_100_10_56PZ_A1_1': 'Energiekette 0,5 m, nicht im Gesamtmodell',
    'drag_chain_0_5m_E2C_10_10_028_0___E2_100_10_56PZ_A1_2': 'Energiekette 0,5 m, nicht im Gesamtmodell',
    'mean_well_HRPG-1000-24': 'Netzteil 1000 W, nicht im Gesamtmodell (verbaut: RSP-200-24)',
    'raspberry_pi_4_dummy': 'Platzhalter Raspberry Pi 4',
}
# Decision per Solid-Edge-only part (Luis 26.10.2026)
NOT_NEEDED_OLD = 'nicht benötigt: ältere Variante/Duplikat, nicht im Gesamtmodell'
DECISION = {
    'calibration_plate_v4': 'drucken: SYS-061', 'calibration_plate_pin': 'drucken: SYS-063',
    'calibration_plate_marker_fill_001': 'drucken: SYS-062', 'calibration_plate_marker_fill_003': 'drucken: SYS-062',
    'calibration_plate_marker_fill_006': 'drucken: SYS-062', 'calibration_plate_marker_fill_012': 'drucken: SYS-062',
    'calibration_plate': 'nicht benötigt: Altstand, Baugruppe nutzt v4', 'calibration_plate_v2': 'nicht benötigt: Altstand, Baugruppe nutzt v4',
    'calibration_plate_v3': 'nicht benötigt: Altstand, Baugruppe nutzt v4', 'calibration_plate_marker_fill': 'nicht benötigt: nicht in calibration_plate.asm',
    'base_drawer_drag_chain_holder': 'drucken: SYS-064', 'drawer_drag_chain_holder': 'drucken: SYS-065',
    'base_drawer_power_plug_socket': 'drucken: SYS-066',
    'drag_chain_0_5m_E2C_10_10_028_0___E2_100_10_56PZ_A1_1': 'kaufen: SYS-073/074',
    'drag_chain_0_5m_E2C_10_10_028_0___E2_100_10_56PZ_A1_2': 'kaufen: SYS-073/074',
    'target_power_switch': 'drucken: SYS-067', 'target_power_switch_top': 'drucken: SYS-068',
    'base_power_supply_housing': 'drucken: SYS-069', 'base_power_supply_housing_top': 'drucken: SYS-070',
    'base_raspberry_pi_4_adapter': 'drucken: SYS-071', 'raspberry_pi_4_dummy': 'offen: Raspberry Pi 4 bei SCHUTZWERK anfragen',
    'utils_height_leveling_probe_holder': 'drucken: SYS-072',
    'z_pogo_pin_holder': 'nicht benötigt: ältere Prüfspitze, aktuell Spitzen-PCB', 'z_pogo_pin_holder_cover': 'nicht benötigt: ältere Prüfspitze, aktuell Spitzen-PCB',
    'z_pogo_pin_holder_long': 'nicht benötigt: ältere Prüfspitze, aktuell Spitzen-PCB', 'z_pogo_pin_holder_long_mirrored': 'nicht benötigt: ältere Prüfspitze, aktuell Spitzen-PCB',
    'x_motor_plate_raw': 'Rohteil, über MAT-006', 'x_motor_plate_2_raw': 'Rohteil, über MAT-006',
    'x_side_plate_raw': 'Rohteil, über MAT-006', 'x_side_plate_moving_raw': 'Rohteil, über MAT-006',
    'mean_well_HRPG-1000-24': 'nicht benötigt: RSP-200-24 verbaut',
    'motor_adapter_nema_17': NOT_NEEDED_OLD, 'base_nema_14_belt_drive_adapter_motor': NOT_NEEDED_OLD,
    'x_end_stop_holder_side_long': NOT_NEEDED_OLD, 'y_camera_holder_mirrored': NOT_NEEDED_OLD,
    'pcb_holder_glider_slim_long': NOT_NEEDED_OLD,
}
CONFLICT_NOTES = {
    'base_drag_chain_holder': 'liegt in printed_parts, ist aber 650 mm lang, Material Alu 7075, zusätzlich .psm und Zeichnung in mechanical_parts: nicht am Stück druckbar, bleibt Alu-Flachprofil',
    'signal_multiplexer_dummy': 'erledigt: echte Platine in hardware/signal-multiplexer, Bestellung SYS-003/023 bei JLCPCB',
    'pcb_dummy': 'Prüfling im Modell, kein Maschinenteil',
    'base_drawer_dummy_plate': 'Material im Solid-Edge-Modell: Birke 12 mm (Schubladenboden)',
}


def stem(name):
    for suffix in ('.par', '.psm', '.asm'):
        if name.endswith(suffix):
            name = name[:-len(suffix)]
            break
    return name.strip()


def main():
    geo = json.loads((BOM / 'evidence' / 'solidedge-geometry.json').read_text(encoding='utf-8'))
    geo = {(v['folder'], v['file']): v for v in geo.values()}
    with (BOM / 'cad-inventory.csv').open(encoding='utf-8-sig') as f:
        step = {r['cad_name'].strip(): r for r in csv.DictReader(f)}
    with (BOM / 'teileliste.csv').open(encoding='utf-8-sig') as f:
        parts = {r['cad_name'].strip(): r for r in csv.DictReader(f) if r['cad_name']}

    rows = []
    for path in sorted(CAD_DIR.rglob('*'), key=lambda p: (p.parent.name, p.name.lower())):
        if path.suffix.lower() not in ('.par', '.psm', '.asm'):
            continue
        folder, name = path.parent.name, stem(path.name)
        if path.suffix == '.psm' and (path.with_suffix('.par')).exists():
            continue  # sheet metal twin of a .par with the same name
        part = parts.get(name)
        g = geo.get((folder, name))
        kind = 'Baugruppe' if path.suffix == '.asm' else 'Teil'
        step_qty = step.get(name, {}).get('quantity', '')
        if kind == 'Baugruppe':
            check = 'Baugruppe'
        elif name in CONFLICT_NOTES:
            check = 'ABWEICHUNG' if name == 'base_drag_chain_holder' else 'OK'
        elif part:
            check = 'OK' if part['group'] in EXPECTED_GROUPS.get(folder, set()) | {'Nicht benötigt'} else 'ABWEICHUNG'
        else:
            check = 'NUR SOLID EDGE'
        note = CONFLICT_NOTES.get(name) or ONLY_SE.get(name, '')
        if part and check == 'ABWEICHUNG' and not note:
            note = f"SCHUTZWERK-Ordner {folder}, bei uns {part['group']}"
        if g and g.get('materials') and g['materials'] != ['Stahl'] and name not in CONFLICT_NOTES:
            note = (note + '; ' if note else '') + 'SE-Material: ' + ', '.join(g['materials'])
        rows.append({
            'Ordner': folder, 'Datei': path.name, 'Art': kind,
            'Fertigung laut Ordner': FOLDER_PROCESS[folder],
            'ID': part['id'] if part else '', 'Bezeichnung': part['name'] if part else '',
            'Menge Gesamtmodell': step_qty, 'Planmenge': part['quantity'] if part else '',
            'Unsere Gruppe': part['group'] if part else '',
            'Hülle mm': ' x '.join(f'{v:g}' for v in g['size_mm']) if g and g.get('size_mm') else '',
            'Volumen cm³': f"{g['volume_cm3']:g}" if g and 'volume_cm3' in g else '',
            'Abgleich': check, 'Hinweis': note,
            'Entscheidung': DECISION.get(name, '') if check == 'NUR SOLID EDGE' else '',
        })

    with (BOM / 'SolidEdge-Teileliste.csv').open('w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter=';')
        w.writeheader()
        w.writerows(rows)

    def table(subset, cols):
        lines = ['| ' + ' | '.join(cols) + ' |', '|' + '---|' * len(cols)]
        for r in subset:
            lines.append('| ' + ' | '.join(str(r[c]).replace('|', '/') for c in cols) + ' |')
        return '\n'.join(lines)

    cols = ['Datei', 'ID', 'Bezeichnung', 'Menge Gesamtmodell', 'Planmenge', 'Unsere Gruppe', 'Hülle mm', 'Volumen cm³', 'Abgleich', 'Hinweis']
    count = {k: sum(r['Abgleich'] == k for r in rows) for k in ('OK', 'ABWEICHUNG', 'NUR SOLID EDGE', 'Baugruppe')}
    L = ['# Solid-Edge-Teileliste (SCHUTZWERK-Original)', '',
         'Stand 26.10.2026. Quelle: SCHUTZWERK-CAD in [hardware/cad](../hardware/cad) (Solid Edge). '
         'Druck-, Mechanik- und Platinenteile wurden in Fusion importiert und vermessen '
         '([solidedge-geometry.json](evidence/solidedge-geometry.json)). Normteile sind nur über den Dateinamen zugeordnet. '
         '„Menge Gesamtmodell“ = Vorkommen in `proboter.stp`, „Planmenge“ und „Unsere Gruppe“ aus der [Teileliste](Teileliste.md). [CSV](SolidEdge-Teileliste.csv)', '',
         f"**Abgleich:** {count['OK']} Teile OK, {count['ABWEICHUNG']} Abweichungen, "
         f"{count['NUR SOLID EDGE']} Teile nur als Solid-Edge-Datei (nicht im Gesamtmodell), {count['Baugruppe']} Baugruppen.", '',
         '**Regel:** printed_parts = selbst drucken (PETG), mechanical_parts = Werkstatt/Zuschnitt oder Kaufprofil '
         '(Motorhalteplatten CAD-096/097 und Seitenplatten CAD-099/100 selbst gefräst), standard_parts = kaufen. '
         'Der Signal-Multiplexer ist kein Druck- oder Kaufteil mehr, sondern die Platine aus '
         '[hardware/signal-multiplexer](../hardware/signal-multiplexer) (Bestellung bei JLCPCB, Gerber `gerber1.1`).', '']
    sections = [('printed_parts', 'Druckteile (printed_parts)'), ('mechanical_parts', 'Mechanik und Werkstatt (mechanical_parts)'),
                ('standard_parts', 'Kaufteile (standard_parts)'), ('pcbs', 'Leiterplatten (pcbs)'), ('cad', 'Gesamtmodell')]
    for folder, title in sections:
        subset = [r for r in rows if r['Ordner'] == folder]
        in_model = [r for r in subset if r['Abgleich'] != 'NUR SOLID EDGE']
        only = [r for r in subset if r['Abgleich'] == 'NUR SOLID EDGE']
        L += [f'## {title}', '', table(in_model, cols), '']
        if only:
            L += [f'### Nur als Solid-Edge-Datei, nicht im Gesamtmodell ({len(only)})', '',
                  'Bedarf am 26.10.2026 mit Luis entschieden; benötigte Teile stehen als SYS-Positionen in der Teileliste.', '',
                  table(only, ['Datei', 'Hülle mm', 'Volumen cm³', 'Hinweis', 'Entscheidung']), '']
    (BOM / 'SolidEdge-Teileliste.md').write_text('\n'.join(L).rstrip() + '\n', encoding='utf-8')
    print(count)


if __name__ == '__main__':
    main()
