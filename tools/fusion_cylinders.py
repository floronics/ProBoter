"""Read native cylindrical faces via Fusion MCP; all distances exported in mm."""
import json
from pathlib import Path
import adsk.core
import adsk.fusion

OUTPUT=Path('C:/Users/luisk/Documents/GitHub/ProBoter/bom/evidence/cylindrical-features.json')
NAMES=['pulley_gt2_9mm','rod_slide_d10_l19','base_frame_side','base_frame_short',
       'pulley_gt2_z16_6mm','return_pulley_gt2_z16_6mm','probe_tip_pcb',
       'rod_holder_flange_d10_dold']

def run(_context: str):
    app=adsk.core.Application.get()
    design=adsk.fusion.Design.cast(app.activeProduct)
    if not design: raise ValueError('Active document must be a Fusion design')
    result={}
    for occurrence in design.rootComponent.allOccurrences:
        component=occurrence.component
        if component.name not in NAMES or component.name in result: continue
        faces=[]
        for body in component.bRepBodies:
            for face in body.faces:
                cylinder=adsk.core.Cylinder.cast(face.geometry)
                if cylinder:
                    faces.append({'diameter_mm':round(cylinder.radius*20,6),
                                  'axis':[round(v,6) for v in cylinder.axis.asArray()],
                                  'origin_mm':[round(v*10,6) for v in cylinder.origin.asArray()]})
        result[component.name]=faces
    if set(result)!=set(NAMES): raise ValueError('Missing expected components')
    OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'file':str(OUTPUT),'components':len(result)}))
