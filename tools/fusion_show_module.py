"""Run with Fusion MCP (not read-only): show only the parts of one assembly module.

Changes only occurrence visibility (light bulbs); geometry stays untouched.
Set MODULE below. Parts come from bom/montage/module.json.
"""
import json
from pathlib import Path

import adsk.core
import adsk.fusion

MODULE = 'M01'
SPEC = Path('C:/Users/luisk/Documents/GitHub/ProBoter/bom/montage/module.json')


def run(_context: str):
    module = next(m for m in json.loads(SPEC.read_text(encoding='utf-8'))['module'] if m['id'] == MODULE)
    keep = {(s, t['cad_name']) for t in module['teile'] for s in (t['scope'] if isinstance(t['scope'], list) else [t['scope']])}
    app = adsk.core.Application.get()
    root = adsk.fusion.Design.cast(app.activeProduct).rootComponent
    shown = {}
    for occurrence in root.allOccurrences:
        if occurrence.childOccurrences.count:
            occurrence.isLightBulbOn = True
            continue
        scope = occurrence.fullPathName.split('+')[0]
        visible = (scope, occurrence.component.name) in keep
        occurrence.isLightBulbOn = visible
        if visible:
            shown[occurrence.component.name] = shown.get(occurrence.component.name, 0) + 1
    app.activeViewport.fit()
    print(MODULE, module['name'], shown)
