"""Run with Fusion MCP (readOnly=True); export geometry without editing the design.

Fusion internal length unit is cm; output dimensions and positions are mm.
Bounding boxes are axis-aligned, not manufacturing drawings or fit tolerances.
"""
import adsk.core
import adsk.fusion
import json
from pathlib import Path

OUTPUT = Path('C:/Users/luisk/Documents/GitHub/ProBoter/bom/evidence/fusion-inventory.json')


def box_data(box):
    lo, hi = box.minPoint, box.maxPoint
    return {'min_mm': [round(v * 10, 5) for v in (lo.x, lo.y, lo.z)],
            'max_mm': [round(v * 10, 5) for v in (hi.x, hi.y, hi.z)],
            'size_mm': [round(v * 10, 5) for v in (hi.x-lo.x, hi.y-lo.y, hi.z-lo.z)]}


def run(_context: str):
    app = adsk.core.Application.get()
    design = adsk.fusion.Design.cast(app.activeProduct)
    if not design:
        raise ValueError('Active document is not a Fusion design')
    root = design.rootComponent
    rows = []
    for occ in root.allOccurrences:
        comp = occ.component
        bodies = [{'name': b.name, 'volume_cm3': b.volume,
                   'material': b.material.name if b.material else None,
                   'local_box': box_data(b.boundingBox)} for b in comp.bRepBodies]
        rows.append({'path': occ.fullPathName, 'name': comp.name,
                     'children': occ.childOccurrences.count, 'visible': occ.isVisible,
                     'world_box': box_data(occ.boundingBox),
                     'transform': occ.transform2.asArray(), 'bodies': bodies})
    data = {'document': app.activeDocument.name, 'date': '2026-10-16',
            'length_unit': 'mm', 'volume_unit': 'cm3',
            'root_bodies': root.bRepBodies.count, 'occurrences': rows}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'file': str(OUTPUT), 'occurrences': len(rows),
                      'leaves': sum(r['children'] == 0 for r in rows),
                      'root_bodies': root.bRepBodies.count}))
