"""Reconcile Fusion geometry with the STEP inventory; do not infer purchase approval."""
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def analyze():
    raw = ROOT / 'bom/evidence/fusion-inventory.json'
    data = json.loads(raw.read_text(encoding='utf-8'))
    groups = defaultdict(list)
    for row in data['occurrences']:
        if not row['children']:
            groups[row['name']].append(row)
    source = list(csv.DictReader((ROOT/'bom/cad-inventory.csv').open(encoding='utf-8-sig')))
    rows = []
    for i, row in enumerate((r for r in source if r['kind'] == 'leaf'), 1):
        g = groups.get(row['cad_name'], [])
        bodies = g[0]['bodies'] if g else []
        if bodies:
            lo = [min(b['local_box']['min_mm'][k] for b in bodies) for k in range(3)]
            hi = [max(b['local_box']['max_mm'][k] for b in bodies) for k in range(3)]
            size = [round(hi[k]-lo[k], 3) for k in range(3)]
        else:
            size = []
        rows.append({'id': f'CAD-{i:03}', 'cad_name': row['cad_name'],
                     'step_qty': int(row['quantity']), 'fusion_qty': len(g),
                     'visible_qty': sum(r['visible'] for r in g),
                     'local_aabb_mm': ' x '.join(str(v) for v in size),
                     'solid_volume_cm3': round(sum(b['volume_cm3'] for b in bodies), 6) if bodies else '',
                     'imported_material': '; '.join(sorted({b['material'] or '' for b in bodies})),
                     'sample_path': g[0]['path'] if g else '',
                     'count_agrees': len(g) == int(row['quantity'])})
    with (ROOT/'bom/evidence/cad-geometry.csv').open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    manifest = {'date':'2026-10-16', 'fusion_document':data['document'],
                'step_sha256':hashlib.sha256((ROOT/'hardware/3d_models/proboter.stp').read_bytes()).hexdigest(),
                'fusion_export_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),
                'step_leaf_names':len(rows), 'step_occurrences':sum(r['step_qty'] for r in rows),
                'fusion_occurrences':sum(r['fusion_qty'] for r in rows),
                'mismatches':[r['cad_name'] for r in rows if not r['count_agrees']]}
    (ROOT/'bom/evidence/manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(json.dumps(manifest,indent=2))


if __name__ == '__main__':
    analyze()
