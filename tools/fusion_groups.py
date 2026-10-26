"""Sort every CAD part into five procurement groups for the Fusion copy "proboter Gruppen".

Priority (first match wins): 3D-Druck > DOLD-Angebot > Fertigung > SCHUTZWERK-BOM > nicht zugeordnet.
Inputs: bom/teileliste.csv, bom/bestellliste.csv, bom/BOM-SCHUTZWERK-Abgleich.csv,
bom/evidence/fusion-inventory.json. Output: bom/evidence/fusion-gruppen.csv (+ JSON for the Fusion script).
"""
import collections
import csv
import json
import re
from pathlib import Path

BOM = Path(__file__).resolve().parents[1] / 'bom'

GROUPS = ['1 3D-Druckteile', '2 Fertigung', '3 DOLD-Angebot', '4 SCHUTZWERK-BOM übrige', '5 Nicht zugeordnet']
FABRICATION = {'Blech intern', 'CNC extern', 'Weitere Fertigung', 'PCB extern'}

# DOLD offer AN2026-104489 (26.10.2026): CAD name -> offer article
DOLD = {
    'hinged_M6_40_dold': 'GF-K-10-PA-032 Gelenkfuß',
    'screw_on_bracket_30_6': '62392-BSA Winkel 30 I-Typ Nut 6',
    'handle_l100_dold': 'A-75873 Bügelgriff 100 mm',
    'base_frame_side': '63016-Z Profil 30x60L, 650 mm',
    'base_frame_short': '63009-Z Profil 30x30L, 350 mm',
    'base_vertical': '63009-Z Profil 30x30L, 350 mm',
    'base_frame_long_side': '63009-Z Profil 30x30L, 590 mm',
    'base_drawer_long_side': '63009-Z Profil 30x30L, 564 mm',
    'x_slide_stiffener_beam': '60879-Z Profil 40x16S, 436 mm',
    'x_round_rail': '32067-STL-GW-450 Präzisionswelle Ø10 h6, 450 mm',
    'rod_slide_d10_l19': '76993-VK igus RJMP-01-10',
    'cpc_MR12ML': 'MR12 MN-SS-V0-N Linearwagen',
    'hiwin_slide_MGN12CZ0H': 'MR12 MN-SS-V0-N Linearwagen (statt HIWIN MGN12)',
    'hiwin_rail_MGNR12R150HM': '78553-150 Linearführung MR12M, 150 mm',
    'pulley_gt2_z16_6mm': '46088 Zahnriemenrad GT2 16 Z',
    'return_pulley_gt2_z16_6mm': '46132 Umlenkrolle GT2 16 Z',
    'x_belt': '46194 Zahnriemen GT2 6 mm',
    'y_belt': '46194 Zahnriemen GT2 6 mm',
    'din_912_m3x10': 'DIN912-3x10',
    'din_912_m3x12': 'DIN912-3x12',
    'iso_8673_nut_m4': 'DIN934-M4 (CAD-Name ISO 8673 ist DIN 934)',
}
# Boards we have to have made count as fabrication
FABRICATION_EXTRA = {'signal_multiplexer_dummy': 'Multiplexer-Platine, JLCPCB (SYS-003/023)'}
# SCHUTZWERK BOM rows without a usable order ID in BOM-SCHUTZWERK-Abgleich.csv
SW_EXTRA = {
    'inductive_proximity_sensor_m8': 'Endschalter induktiv M8 / M12',
    'drag_chain_0_24m_E2i_10_10_028_0_4': 'Energieketten',
    'drag_chain_0_28m_E2i_10_20_028_0_igus': 'Energieketten',
    'z_pogo_pin': 'Probespitze',
    'mmcx_male_end': 'Kabel Probe',
    'mmcx_male_end_with_angle': 'Kabel Probe',
}


def schutzwerk_cad_names(parts):
    orders = {r['id']: r for r in csv.DictReader(open(BOM / 'bestellliste.csv', encoding='utf-8-sig'))}
    names = {}
    for r in csv.DictReader(open(BOM / 'BOM-SCHUTZWERK-Abgleich.csv', encoding='utf-8-sig'), delimiter=';'):
        if r['Quelle'] != 'Original SCHUTZWERK':
            continue
        for oid in re.findall(r'[A-Z]+-[A-Z]?-?[A-Z0-9-]*\d', r['Floronics-IDs (ersetzt/zugeordnet)']):
            for pid in (orders[oid]['part_ids'].split(';') if oid in orders else [oid]):
                p = parts.get(pid.strip())
                if p and p['cad_name']:
                    names.setdefault(p['cad_name'], r['Teil'])
    return {**SW_EXTRA, **names}


def classify():
    parts = {r['id']: r for r in csv.DictReader(open(BOM / 'teileliste.csv', encoding='utf-8-sig'))}
    by_name = {p['cad_name']: p for p in parts.values() if p['cad_name']}
    sw = schutzwerk_cad_names(parts)
    inv = json.loads((BOM / 'evidence' / 'fusion-inventory.json').read_text(encoding='utf-8'))
    count = collections.Counter(o['name'] for o in inv['occurrences'] if o['children'] == 0)
    rows = []
    for name, n in sorted(count.items()):
        p = by_name[name]
        if p['group'] == '3D-Druck intern':
            g, why = GROUPS[0], 'Teileliste: 3D-Druck intern'
        elif name in DOLD:
            g, why = GROUPS[2], 'Angebot AN2026-104489: ' + DOLD[name]
        elif p['group'] in FABRICATION or name in FABRICATION_EXTRA:
            g, why = GROUPS[1], FABRICATION_EXTRA.get(name, 'Teileliste: ' + p['group'])
        elif name in sw:
            g, why = GROUPS[3], 'SCHUTZWERK-BOM: ' + sw[name]
        else:
            g, why = GROUPS[4], 'Teileliste: ' + p['group']
        rows.append({'Gruppe': g, 'ID': p['id'], 'CAD-Name': name, 'Bezeichnung': p['name'],
                     'Vorkommen in Fusion': n, 'Begründung': why})
    return rows


def main():
    rows = classify()
    rows.sort(key=lambda r: (r['Gruppe'], r['ID']))
    with open(BOM / 'evidence' / 'fusion-gruppen.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter=';')
        w.writeheader()
        w.writerows(rows)
    mapping = {r['CAD-Name']: r['Gruppe'] for r in rows}
    (BOM / 'evidence' / 'fusion-gruppen.json').write_text(json.dumps(mapping, ensure_ascii=False, indent=1), encoding='utf-8')
    for g in GROUPS:
        sel = [r for r in rows if r['Gruppe'] == g]
        print(g, len(sel), 'Teiletypen,', sum(r['Vorkommen in Fusion'] for r in sel), 'Vorkommen')


if __name__ == '__main__':
    main()
