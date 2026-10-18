"""Combined order list of all order positions, sorted by assembly module.

Input:  bom/bestellliste.csv, bom/data/pruefung.csv (review status, edited by hand), bom/montage/montage.csv, bom/montage/module.json.
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
review = {r['id']: r for r in csv.DictReader(open(f'{B}/data/pruefung.csv', encoding='utf-8-sig'), delimiter=';')}
status = lambda r: review.get(r['id'], {}).get('status') or 'offen'
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
    w.writerow(['Modul', 'Modulname', 'ID', 'Beschreibung', 'CAD/SYS-IDs', 'Distributor', 'Hersteller', 'Artikel-Nr.', 'Bedarf', 'Einheit', 'Bestellmenge', 'Brutto EUR', 'Optional', 'Prüfstatus', 'Prüfnotiz', 'Bestelllink'])
    for r in out:
        w.writerow([r['modul'], names.get(r['sort'], 'ohne Modul' if r['sort'] == 'allg.' else 'Versand und Gebühren'), r['id'], r['title'], r['part_ids'], r['supplier'], r['manufacturer'], r['sku'] or r['mpn'], num(r['need']), r['unit'], num(r['order_quantity']), num(r['gross_eur']), 'ja' if r['optional'] == 'True' else '', status(r), review.get(r['id'], {}).get('notiz', ''), r['url']])
L = ['# Gesamtbestellliste (alle Bestellpositionen)', '',
     f'Generiert aus `bestellliste.csv` + `montage/` · {len(out)} Positionen · sortiert nach Modul. '
     'Bei mehreren Modulen wird nach dem ersten einsortiert. „allg.“ = Systemteil ohne Modulzuordnung. [CSV](Gesamtbestellliste.csv)', '']
L += ['| Modul | Modulname | ID | Beschreibung | Distributor | Artikel | Stückzahl | Brutto | Prüfung | Link |',
      '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
for r in out:
    desc = r['title'].replace('|', '/') + (' *(optional)*' if r['optional'] == 'True' else '')
    art = ' / '.join(x for x in [r['manufacturer'], r['sku'] or r['mpn']] if x).replace('|', '/')
    link = f"[Link]({r['url']})" if r['url'].startswith('http') else '–'
    g = f"{float(r['gross_eur']):.2f} €".replace('.', ',') if r['gross_eur'] else 'offen'
    mname = names.get(r['sort'], 'ohne Modul' if r['sort'] == 'allg.' else 'Versand und Gebühren')
    L.append(f"| {r['modul']} | {mname} | {r['id']} | {desc} | {r['supplier'] or '–'} | {art or '–'} | {qty(r)} | {g} | {status(r)} | {link} |")
open(f'{B}/Gesamtbestellliste.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print(collections.Counter(r['sort'] for r in out))
