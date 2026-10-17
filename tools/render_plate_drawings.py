"""Render workshop drawings (PDF), hole tables (CSV) and DXF for the M01 plates.

Input: bom/evidence/plate-geometry.json (tools/fusion_plate_geometry.py).
Coordinates: origin at the lower left corner of the plate bounding box, mm.
"""
import csv
import json
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Circle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'bom' / 'zeichnungen'
PLATES = [
    ('base_back_plate', 'CAD-003', 'Rückwand', 'Aluminium 3 mm (z. B. EN AW-5754)', 1),
    ('x_motor_plate', 'CAD-096', 'Motorplatte 1', 'Stahl oder Aluminium 5 mm', 1),
    ('x_motor_plate_2', 'CAD-097', 'Motorplatte 2', 'Stahl oder Aluminium 5 mm', 1),
]
COLORS = {'Durchgang': 'black', 'Senkung 90°': 'tab:blue', 'Senkung 90° für M6': 'tab:blue',
          'Gewinde M3 (Kernloch Ø2,5)': 'tab:red'}


def label(h):
    if h['kind'].startswith('Gewinde'):
        return 'M3 Gewinde (Kernloch Ø2,5)'
    if h['kind'].startswith('Senkung'):
        return f"Ø{h['d']:g} mit Senkung 90°"
    return f"Ø{h['d']:g} durch"


def dxf(path, plate):
    lines = ['0', 'SECTION', '2', 'ENTITIES']
    for poly in plate['outline']:
        for (x1, y1), (x2, y2) in zip(poly, poly[1:]):
            lines += ['0', 'LINE', '8', 'KONTUR', '10', f'{x1}', '20', f'{y1}', '11', f'{x2}', '21', f'{y2}']
    for h in plate['holes']:
        layer = 'GEWINDE_M3' if h['kind'].startswith('Gewinde') else ('SENKUNG' if h['kind'].startswith('Senkung') else 'BOHRUNG')
        lines += ['0', 'CIRCLE', '8', layer, '10', f"{h['x']}", '20', f"{h['y']}", '40', f"{h['d'] / 2}"]
    lines += ['0', 'ENDSEC', '0', 'EOF']
    path.write_text('\n'.join(lines) + '\n', encoding='ascii')


def page(pdf, name, cad_id, title, material, qty, plate):
    w, h, t = plate['size_mm']
    fig = plt.figure(figsize=(16.54, 11.69))  # A3 landscape
    ax = fig.add_axes([0.04, 0.30, 0.92, 0.62])
    for poly in plate['outline']:
        xs, ys = zip(*poly)
        ax.plot(xs, ys, color='black', lw=0.8)
    for hole in plate['holes']:
        ax.add_patch(Circle((hole['x'], hole['y']), hole['d'] / 2, fill=False, lw=0.6,
                            color=COLORS.get(hole['kind'], 'black')))
        if hole['kind'].startswith('Senkung'):
            ax.add_patch(Circle((hole['x'], hole['y']), hole['d'], fill=False, lw=0.4, ls='--', color='tab:blue'))
    ax.annotate('', (0, -12), (w, -12), arrowprops=dict(arrowstyle='<->', lw=0.6))
    ax.text(w / 2, -20, f'{w:g}', ha='center', va='top', fontsize=9)
    ax.annotate('', (-12, 0), (-12, h), arrowprops=dict(arrowstyle='<->', lw=0.6))
    ax.text(-20, h / 2, f'{h:g}', ha='right', va='center', rotation=90, fontsize=9)
    ax.plot(0, 0, 'k+', ms=12)
    ax.text(2, 2, 'Nullpunkt (0,0)', fontsize=7)
    ax.set_aspect('equal')
    ax.set_xlim(-35, w + 10)
    ax.set_ylim(-35, h + 10)
    ax.axis('off')

    groups = Counter(label(x) for x in plate['holes'])
    rows = [[k, n] for k, n in sorted(groups.items())]
    tab = fig.add_axes([0.04, 0.04, 0.42, 0.22])
    tab.axis('off')
    tab.table(cellText=rows, colLabels=['Bohrung', 'Anzahl'], loc='upper left', cellLoc='left',
              colWidths=[0.75, 0.2]).set_fontsize(9)
    tab.set_title('Bohrungen (Koordinaten siehe CSV/DXF)', fontsize=10, loc='left')

    block = fig.add_axes([0.52, 0.04, 0.44, 0.22])
    block.axis('off')
    info = [['Projekt', 'Floronics ProBoter-Nachbau, Modul M01 Grundgerüst'],
            ['Teil', f'{cad_id} {title} (CAD: {name})'],
            ['Maße', f'{w:g} × {h:g} × {t:g} mm'],
            ['Material', material],
            ['Menge', f'{qty} Stück'],
            ['Fertigung', 'Eigene Werkstatt'],
            ['Quelle', 'Aus dem STEP/Fusion-Modell abgeleitet, 17.10.2026'],
            ['Hinweis', 'Ungeprüfter Entwurf; Toleranzen, Kanten und Gewindetiefe in der Werkstatt festlegen']]
    block.table(cellText=info, loc='upper left', cellLoc='left', colWidths=[0.18, 0.8]).set_fontsize(9)
    fig.suptitle(f'{cad_id} {title}', fontsize=14, x=0.04, ha='left')
    pdf.savefig(fig)
    plt.close(fig)


def main():
    geometry = json.loads((ROOT / 'bom/evidence/plate-geometry.json').read_text(encoding='utf-8'))
    OUT.mkdir(parents=True, exist_ok=True)
    with PdfPages(OUT / 'M01-Platten.pdf') as pdf:
        for name, cad_id, title, material, qty in PLATES:
            plate = geometry[name]
            page(pdf, name, cad_id, title, material, qty, plate)
            dxf(OUT / f'{cad_id}-{name}.dxf', plate)
            with (OUT / f'{cad_id}-{name}-bohrungen.csv').open('w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(['Nr', 'X_mm', 'Y_mm', 'Bohrung'])
                for i, hole in enumerate(plate['holes'], 1):
                    writer.writerow([i, hole['x'], hole['y'], label(hole)])
    print('written', OUT)


if __name__ == '__main__':
    main()
