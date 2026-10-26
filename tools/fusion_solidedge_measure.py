"""Run with Fusion MCP (readOnly=False: opens and closes documents, saves nothing).

Measures the SCHUTZWERK Solid Edge parts uploaded to the Fusion folder
SolidEdge-Original/{printed_parts,mechanical_parts,pcbs}. Resumable: 35 parts per run.
"""
import adsk.core, adsk.fusion, json, os
OUT = r'C:\Users\luisk\Documents\GitHub\ProBoter\bom\evidence\solidedge-geometry.json'
SUBS = ['printed_parts', 'mechanical_parts', 'pcbs']
def run(_context: str):
    app = adsk.core.Application.get()
    top = app.data.activeProject.rootFolder.dataFolders.itemByName('SolidEdge-Original')
    data = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    done = 0
    for sub in SUBS:
        for df in top.dataFolders.itemByName(sub).dataFiles:
            key = sub + '/' + df.name
            if key in data: continue
            doc = app.documents.open(df, False)
            try:
                d = adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
                bodies = list(d.rootComponent.bRepBodies) + [b for o in d.rootComponent.allOccurrences for b in o.bRepBodies]
                vis = [b for b in bodies if b.isSolid]
                box = None
                for b in vis:
                    bb = b.boundingBox
                    box = bb.copy() if box is None else box; box is bb or box.combine(bb)
                size = [round((box.maxPoint.x-box.minPoint.x)*10, 2), round((box.maxPoint.y-box.minPoint.y)*10, 2), round((box.maxPoint.z-box.minPoint.z)*10, 2)] if box else None
                data[key] = {'file': df.name, 'folder': sub, 'solid_bodies': len(vis), 'all_bodies': len(bodies),
                             'size_mm': size, 'volume_cm3': round(sum(b.volume for b in vis), 3),
                             'area_cm2': round(sum(b.area for b in vis), 2),
                             'materials': sorted({b.material.name for b in vis if b.material}),
                             'holes': sum(1 for b in vis for f in b.faces if f.geometry.surfaceType == adsk.core.SurfaceTypes.CylinderSurfaceType)}
            except Exception as e:
                data[key] = {'file': df.name, 'folder': sub, 'error': str(e)}
            finally:
                doc.close(False)
            done += 1
            if done >= 35: break
        if done >= 35: break
    json.dump(data, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
    print('measured', done, 'total', len(data))
