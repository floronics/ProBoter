"""Run with Fusion MCP: save or apply named visibility views of the ProBoter model.

MODE 'save'  (readOnly=True): store every visible leaf occurrence of the
             current Fusion view under VIEW in bom/views/<VIEW>.json.
MODE 'apply' (not read-only): show only the occurrences listed in a view,
             optionally filtered by FILTER_KEY/FILTER_VALUE of the view's
             classification (bom/views/<VIEW>-gruppen.json).
Only light bulbs change; geometry is never modified.
"""
import json
from pathlib import Path

import adsk.core
import adsk.fusion

MODE = 'save'
VIEW = 'onlyPassiveParts'
FILTER_KEY = None      # e.g. 'beschaffung'
FILTER_VALUE = None    # e.g. 'Bestellung'
VIEWS = Path('C:/Users/luisk/Documents/GitHub/ProBoter/bom/views')


def leaves(root):
    return [o for o in root.allOccurrences if o.childOccurrences.count == 0]


def run(_context: str):
    app = adsk.core.Application.get()
    root = adsk.fusion.Design.cast(app.activeProduct).rootComponent
    path = VIEWS / f'{VIEW}.json'
    if MODE == 'save':
        visible = sorted((o.fullPathName, o.component.name) for o in leaves(root) if o.isVisible)
        VIEWS.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({'view': VIEW, 'document': app.activeDocument.name,
                                    'occurrences': [{'path': p, 'cad_name': n} for p, n in visible]},
                                   indent=1, ensure_ascii=False), encoding='utf-8')
        print(VIEW, 'gespeichert:', len(visible), 'sichtbare Teile')
        return
    entries = json.loads(path.read_text(encoding='utf-8'))['occurrences']
    if FILTER_KEY:
        groups = json.loads((VIEWS / f'{VIEW}-gruppen.json').read_text(encoding='utf-8'))
        allowed = {g['cad_name'] for g in groups if g[FILTER_KEY] == FILTER_VALUE}
        entries = [e for e in entries if e['cad_name'] in allowed]
    keep = {e['path'] for e in entries}
    shown = 0
    for occurrence in root.allOccurrences:
        if occurrence.childOccurrences.count:
            occurrence.isLightBulbOn = True
            continue
        occurrence.isLightBulbOn = occurrence.fullPathName in keep
        shown += occurrence.isLightBulbOn
    app.userInterface.activeSelections.clear()
    app.activeViewport.fit()
    print(VIEW, FILTER_VALUE or 'alle', 'eingeblendet:', shown)
