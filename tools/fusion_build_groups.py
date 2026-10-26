"""Run with Fusion MCP (readOnly=False) on an opened copy named "proboter Gruppen".

Flattens the copy into five group components from bom/evidence/fusion-gruppen.json
(tools/fusion_groups.py). Every leaf keeps its world position: transforms are chained
through the sub-assemblies because transform2 of a native occurrence is local.
Each part is first added as a component copy, because deleting the old sub-assemblies
also deletes the components defined inside them. Save afterwards in Fusion.
Keep lines short: the MCP script transport drops scripts with very long lines.
"""
import adsk.core
import adsk.fusion
import collections
import json
import traceback

MAPPING_FILE = 'C:/Users/luisk/Documents/GitHub/ProBoter/bom/evidence/fusion-gruppen.json'
GROUPS = ['1 3D-Druckteile', '2 Fertigung', '3 DOLD-Angebot',
          '4 SCHUTZWERK-BOM \u00fcbrige', '5 Nicht zugeordnet']


def walk(comp, parent, out):
    for i in range(comp.occurrences.count):
        occ = comp.occurrences.item(i)
        m = occ.transform2.copy()
        m.transformBy(parent)
        if occ.childOccurrences.count == 0:
            out.append((occ.component, m))
        else:
            walk(occ.component, m, out)


def run(_context: str):
    try:
        _run()
    except Exception:
        print(traceback.format_exc())


def _run():
    mapping = json.load(open(MAPPING_FILE, encoding='utf-8'))
    app = adsk.core.Application.get()
    doc = [d for d in app.documents if d.name == 'proboter Gruppen'][0]
    design = adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
    root = design.rootComponent
    if root.occurrences.item(0).component.name in GROUPS:
        print('already grouped')
        return
    leaves = []
    walk(root, adsk.core.Matrix3D.create(), leaves)
    old = [root.occurrences.item(i) for i in range(root.occurrences.count)]
    groups = {}
    for g in GROUPS:
        occ = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        occ.component.name = g
        groups[g] = occ.component
    copies = {}
    count = collections.Counter()
    for comp, m in leaves:
        g = mapping.get(comp.name, GROUPS[4])
        occs = groups[g].occurrences
        if comp.name in copies:
            occs.addExistingComponent(copies[comp.name], m)
        else:
            copies[comp.name] = occs.addNewComponentCopy(comp, m).component
        count[g] += 1
    for o in old:
        o.deleteMe()
    print('leaves', len(leaves), dict(count))
