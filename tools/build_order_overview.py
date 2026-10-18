"""Combined order list of all order positions, sorted by assembly module.

Input:  bom/bestellliste.csv, bom/montage/montage.csv, bom/montage/module.json.
Output: bom/Gesamtbestellliste.md and bom/Gesamtbestellliste.csv.
Run: python tools/build_order_overview.py
"""
import csv
import json
import collections
from pathlib import Path

B = Path(__file__).resolve().parents[1] / 'bom'
m = list(csv.DictReader(open(f'{B}/montage/montage.csv', encoding='utf-8-sig')))
mods = collections.defaultdict(set)
for r in m: mods[r['id']].add(r['modul'])
# Systemteile ohne CAD aus den "zusatz"-Einträgen von module.json
extra = {'M07': [1] + list(range(9, 22)) + [25, 38, 32, 26], 'M08': [2, 33, 29],
         'M09': [3, 22, 23, 24], 'M06': [27, 28]}
for mod, nums in extra.items():
    for n in nums:
        sid = f'SYS-{n:03d}'
        if not mods[sid]: mods[sid].add(mod)
names = {x['id']: x['name'] for x in json.load(open(f'{B}/montage/module.json', encoding='utf-8'))['module']}
rows = list(csv.DictReader(open(f'{B}/bestellliste.csv', encoding='utf-8-sig')))
out = []
for r in rows:
    ps = [p.strip() for p in r['part_ids'].split(';') if p.strip()]
    ms = sorted(set().union(*[mods.get(p, set()) for p in ps])) if ps else []
    if not ps: key = 'Versand'
    elif not ms: key = 'allg.'
    else: key = ms[0]
    out.append(dict(modul=', '.join(ms) if ms else key, sort=key, **r))
order = lambda k: (0, k) if k.startswith('M') else (1 if k == 'allg.' else 2, k)
out.sort(key=lambda r: (order(r['sort']), r['id']))
def num(x): return x.replace('.', ',')
qty = lambda r: f"{num(r['need'])} {r['unit']}" + (f" → {r['order_packs']}×{r['pack_size']}" if r['order_packs'] and r['pack_size'] not in ('', '1') else '')
with open(f'{B}/Gesamtbestellliste.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['Modul', 'ID', 'Beschreibung', 'CAD/SYS-IDs', 'Distributor', 'Hersteller', 'Artikel-Nr.', 'Bedarf', 'Einheit', 'Bestellmenge', 'Brutto EUR', 'Optional', 'Bestelllink'])
    for r in out:
        w.writerow([r['modul'], r['id'], r['title'], r['part_ids'], r['supplier'], r['manufacturer'], r['sku'] or r['mpn'], num(r['need']), r['unit'], num(r['order_quantity']), num(r['gross_eur']), 'ja' if r['optional'] == 'True' else '', r['url']])
L = ['# Gesamtbestellliste (alle Bestellpositionen)', '',
     f'Generiert aus `bestellliste.csv` + `montage/` · {len(out)} Positionen · sortiert nach Modul. '
     'Bei mehreren Modulen wird nach dem ersten einsortiert. „allg.“ = Systemteil ohne Modulzuordnung. [CSV](Gesamtbestellliste.csv)', '']
cur = None
for r in out:
    if r['sort'] != cur:
        cur = r['sort']
        title = f"{cur} {names.get(cur, '')}" if cur.startswith('M') else ('Allgemein / ohne Modul' if cur == 'allg.' else 'Versand und Gebühren')
        L += ['', f'## {title}', '', '| Modul | ID | Beschreibung | Distributor | Artikel | Stückzahl | Brutto | Link |', '| --- | --- | --- | --- | --- | --- | --- | --- |']
    desc = r['title'].replace('|', '/') + (' *(optional)*' if r['optional'] == 'True' else '')
    art = ' / '.join(x for x in [r['manufacturer'], r['sku'] or r['mpn']] if x).replace('|', '/')
    link = f"[Link]({r['url']})" if r['url'].startswith('http') else '–'
    g = f"{float(r['gross_eur']):.2f} €".replace('.', ',') if r['gross_eur'] else 'offen'
    L.append(f"| {r['modul']} | {r['id']} | {desc} | {r['supplier'] or '–'} | {art or '–'} | {qty(r)} | {g} | {link} |")
open(f'{B}/Gesamtbestellliste.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(collections.Counter(r['sort'] for r in out))
