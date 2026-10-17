"""Run with Fusion MCP (readOnly=True); measure belts, Z drives and hole patterns.

Fusion internal length unit is cm; output values are mm. The design is not
modified. Belt pitch length assumes GT2 Z16 pulleys (pitch radius 5.093 mm).
"""
import json
import math
from pathlib import Path

import adsk.core
import adsk.fusion

OUTPUT = Path('C:/Users/luisk/Documents/GitHub/ProBoter/bom/evidence/fusion-measurements.json')
GT2_Z16_PITCH_RADIUS_MM = 16 * 2 / (2 * math.pi)
BELTS = {'x_belt': 6.0, 'y_belt': 6.0, 'z_drive_belt': 9.0}
HOLE_PARTS = ('handle_l100_dold', 'hinged_M6_40_dold', 'optical_endstop', 'x_guiding_cpc_MR12M',
              'hiwin_rail_MGNR12R150HM', 'cpc_MR12ML', 'hiwin_slide_MGN12CZ0H', 'usb_microscope',
              'mean_well_MHS-012_mounting_bracket', 'rod_slide_d10_l19', 'pulley_gt2_9mm')


def mm(values):
    return [round(v * 10, 3) for v in values]


def cylinders(bodies):
    found = {}
    for body in bodies:
        for face in body.faces:
            geometry = face.geometry
            if isinstance(geometry, adsk.core.Cylinder):
                found.setdefault(round(geometry.radius * 20, 3), set()).add(tuple(mm(geometry.origin.asArray())))
    return {str(d): sorted(points) for d, points in sorted(found.items())}


def belt(component, width):
    body = component.bRepBodies.item(0)
    planes = [f for f in body.faces if isinstance(f.geometry, adsk.core.Plane)]
    arcs = [f for f in body.faces if isinstance(f.geometry, adsk.core.Cylinder)]
    flat = sorted(planes, key=lambda f: -f.area)[:4]
    straight = sum(f.area * 100 for f in flat) / 4 / width
    ring = [f for f in planes if f.loops.count == 2]
    return dict(width_mm=width, straight_run_mm=round(straight, 2),
                closed_loop_in_cad=len(ring) == 2,
                arc_radii_mm=sorted({round(f.geometry.radius * 10, 3) for f in arcs}),
                pitch_length_mm=round(2 * straight + 2 * math.pi * GT2_Z16_PITCH_RADIUS_MM, 1))


def run(_context: str):
    design = adsk.fusion.Design.cast(adsk.core.Application.get().activeProduct)
    root = design.rootComponent
    components = {c.name: c for c in design.allComponents}
    result = dict(document=adsk.core.Application.get().activeDocument.name, unit='mm',
                  belts={n: belt(components[n], w) for n, w in BELTS.items()},
                  holes={n: cylinders(components[n].bRepBodies) for n in HOLE_PARTS})

    motors = {}
    for occurrence in root.allOccurrences:
        name = occurrence.component.name
        if name == 'nanotec_nema_14_ST3518M1004-A':
            top = occurrence.fullPathName.split('+')[0]
            shaft = [f.geometry for b in occurrence.bRepBodies for f in b.faces
                     if isinstance(f.geometry, adsk.core.Cylinder) and abs(f.geometry.radius * 10 - 2.5) < 1e-3]
            motors.setdefault(top, []).append(dict(path=occurrence.fullPathName,
                                                   shaft_axis_origin_mm=mm(shaft[0].origin.asArray()),
                                                   shaft_axis=[round(v, 3) for v in shaft[0].axis.asArray()]))
    pairs = {}
    for top, entries in motors.items():
        a, b = (e['shaft_axis_origin_mm'] for e in entries[:2])
        pairs[top] = dict(motors=entries, shaft_offset_mm=round(math.dist(a[1:], b[1:]), 2))
    result['nema14_pairs'] = pairs

    drives = {}
    for occurrence in root.allOccurrences:
        if occurrence.component.name == 'pulley_gt2_9mm':
            top = occurrence.fullPathName.split('+')[0]
            bore = [f.geometry for b in occurrence.bRepBodies for f in b.faces
                    if isinstance(f.geometry, adsk.core.Cylinder) and abs(f.geometry.radius * 10 - 2.5) < 1e-3]
            drives.setdefault(top, []).append(mm(bore[0].origin.asArray()))
    result['z_pulley_axes_mm'] = drives

    OUTPUT.write_text(json.dumps(result, indent=1), encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k in ('belts', 'nema14_pairs')}, indent=1))
