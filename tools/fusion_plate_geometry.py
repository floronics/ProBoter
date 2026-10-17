"""Run with Fusion MCP (readOnly=True): export 2D plate geometry for drawings.

For each plate the largest planar face is projected onto its plane: outer
contour as polylines, holes with centre, diameter and feature type
(countersink, threaded core hole, through hole). Output in mm.
"""
import json
from pathlib import Path

import adsk.core
import adsk.fusion

PLATES = ['base_back_plate', 'x_motor_plate', 'x_motor_plate_2']
OUTPUT = Path('C:/Users/luisk/Documents/GitHub/ProBoter/bom/evidence/plate-geometry.json')


def run(_context: str):
    design = adsk.fusion.Design.cast(adsk.core.Application.get().activeProduct)
    result = {}
    for component in design.allComponents:
        if component.name not in PLATES:
            continue
        body = component.bRepBodies.item(0)
        box = body.boundingBox
        size = [(box.maxPoint.asArray()[i] - box.minPoint.asArray()[i]) * 10 for i in range(3)]
        normal_axis = size.index(min(size))
        u, v = [i for i in range(3) if i != normal_axis]
        if size[u] < size[v]:
            u, v = v, u
        top = max((f for f in body.faces if isinstance(f.geometry, adsk.core.Plane)
                   and abs(abs(f.geometry.normal.asArray()[normal_axis]) - 1) < 1e-6), key=lambda f: f.area)

        def pt(p):
            a = p.asArray()
            return [round((a[u] - box.minPoint.asArray()[u]) * 10, 3), round((a[v] - box.minPoint.asArray()[v]) * 10, 3)]

        outline = []
        for loop in top.loops:
            if not loop.isOuter:
                continue
            for edge in loop.edges:
                ev = edge.evaluator
                _, p0, p1 = ev.getParameterExtents()
                _, strokes = ev.getStrokes(p0, p1, 0.005)
                outline.append([pt(q) for q in strokes])

        holes = {}
        for face in body.faces:
            g = face.geometry
            if isinstance(g, (adsk.core.Cylinder, adsk.core.Cone)) and abs(abs(g.axis.asArray()[normal_axis]) - 1) < 1e-6:
                key = tuple(pt(g.origin))
                entry = holes.setdefault(key, {'x': key[0], 'y': key[1], 'diameters': set(), 'cone': False})
                if isinstance(g, adsk.core.Cone):
                    entry['cone'] = True
                else:
                    entry['diameters'].add(round(g.radius * 20, 2))
        hole_list = []
        for h in holes.values():
            d = sorted(h['diameters'])
            if not d:
                continue
            small = d[0]
            kind = 'Gewinde M3 (Kernloch Ø2,5)' if abs(small - 2.46) < 0.1 else (
                'Senkung 90° für M6' if h['cone'] and abs(small - 6.6) < 0.2 else (
                    'Senkung 90°' if h['cone'] else 'Durchgang'))
            hole_list.append(dict(x=h['x'], y=h['y'], d=small, all_d=d, kind=kind))
        result[component.name] = dict(size_mm=[round(size[u], 2), round(size[v], 2), round(size[normal_axis], 2)],
                                      outline=outline, holes=sorted(hole_list, key=lambda h: (h['y'], h['x'])))
    OUTPUT.write_text(json.dumps(result, indent=1), encoding='utf-8')
    print({k: (v['size_mm'], len(v['holes']), len(v['outline'])) for k, v in result.items()})
