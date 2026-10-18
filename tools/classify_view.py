"""Split the parts of a saved Fusion view into ordered and self-made parts.

Input:  bom/views/<view>.json (tools/fusion_views.py), bom/teileliste.csv,
        bom/bestellliste.csv.
Output: bom/views/<view>-gruppen.json and <view>.md.
Run: python tools/classify_view.py [view]
"""
import csv
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOM = ROOT / 'bom'
TECHNIK = {'3D-Druck intern': '3D-Druck (PETG)',
           'Blech intern': 'Werkstatt: Platten aus Blech/Alu',
           'Weitere Fertigung': 'Werkstatt: Ablängen/Drehen aus Halbzeug',
           'CNC extern': 'CNC extern',
           'Ungeklärte Teile': 'noch offen (Fertigung ungeklärt)'}


def classify(part, orders):
    order = orders.get(part['cost_id'], {})
    if part['group'] == 'Kaufteile':
        return 'Bestellung', 'Kaufteil'
    if part['group'] == 'Weitere Fertigung' and order.get('price_kind') == 'Webpreis' and order.get('sku', 'offen') != 'offen':
        return 'Bestellung', 'Zuschnitt vom Händler'
    return 'Eigenfertigung', TECHNIK.get(part['group'], part['group'])


def main(view='onlyPassiveParts'):
    occurrences = json.loads((BOM / 'views' / f'{view}.json').read_text(encoding='utf-8'))['occurrences']
    with (BOM / 'teileliste.csv').open(encoding='utf-8-sig') as f:
        parts = {p['cad_name']: p for p in csv.DictReader(f) if p['cad_name']}
    with (BOM / 'bestellliste.csv').open(encoding='utf-8-sig') as f:
        orders = {o['id']: o for o in csv.DictReader(f)}
    counts = Counter(o['cad_name'] for o in occurrences)
    groups = []
    for name, n in sorted(counts.items()):
        part = parts[name]
        beschaffung, technik = classify(part, orders)
        groups.append(dict(cad_name=name, id=part['id'], name=part['name'], stueck_in_ansicht=n,
                           beschaffung=beschaffung, technik=technik, status=part['status']))
    (BOM / 'views' / f'{view}-gruppen.json').write_text(json.dumps(groups, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

    text = f'# Ansicht {view}\n\nSichtbare Teile der gespeicherten Fusion-Ansicht, gegliedert nach Beschaffung. Einblenden mit `tools/fusion_views.py`. Erzeugt von `tools/classify_view.py`.\n\n'
    order = [('Bestellung', None)] + [('Eigenfertigung', t) for t in sorted({g['technik'] for g in groups if g['beschaffung'] == 'Eigenfertigung'})]
    text += '| Gruppe | Positionen | Stück |\n| --- | --- | --- |\n'
    for b, t in order:
        sub = [g for g in groups if g['beschaffung'] == b and (t is None or g['technik'] == t)]
        text += f"| {b}{' – ' + t if t else ''} | {len(sub)} | {sum(g['stueck_in_ansicht'] for g in sub)} |\n"
    for b, t in order:
        sub = [g for g in groups if g['beschaffung'] == b and (t is None or g['technik'] == t)]
        text += f"\n## {b}{' – ' + t if t else ''}\n\n| ID / Teil | CAD-Name | Stück | Art | Status |\n| --- | --- | --- | --- | --- |\n"
        for g in sorted(sub, key=lambda g: g['id']):
            text += f"| [{g['id']}](../Teileliste.md#{g['id'].lower()}) {g['name']} | `{g['cad_name']}` | {g['stueck_in_ansicht']} | {g['technik']} | {g['status']} |\n"
    (BOM / 'views' / f'{view}.md').write_text(text, encoding='utf-8')
    for b, t in order:
        sub = [g for g in groups if g['beschaffung'] == b and (t is None or g['technik'] == t)]
        print(b, t or '', len(sub), sum(g['stueck_in_ansicht'] for g in sub))


if __name__ == '__main__':
    main(*sys.argv[1:])
