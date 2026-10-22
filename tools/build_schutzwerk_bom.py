"""Abgleich der Original-BOM von SCHUTZWERK (bom/BOM.ods) mit unserer Gesamtbestellliste.

Regel: Die SCHUTZWERK-BOM gilt. Jede SCHUTZWERK-Zeile wird übernommen; Positionen
unserer Recherche, die durch eine SCHUTZWERK-Zeile abgedeckt sind, entfallen.
Positionen, für die die SCHUTZWERK-BOM nichts enthält, werden als
Floronics-Recherche angehängt. Die Lieferbarkeit der SCHUTZWERK-Links wurde am
22.10.2026 auf den Shopseiten geprüft (Ergebnis unten in AVAILABILITY).

    python tools/build_schutzwerk_bom.py
"""
import csv
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ODS = ROOT / "bom" / "BOM.ods"
ORDER_LIST = ROOT / "bom" / "Gesamtbestellliste.csv"
OUTPUT = ROOT / "bom" / "BOM-SCHUTZWERK-Abgleich.csv"

CHECK_DATE = "22.10.2026"
PROBES = 4  # SCHUTZWERK: Vollausbau = Rahmen + 4 x Probe
NS = "urn:oasis:names:tc:opendocument:xmlns:"
TABLE = "{%stable:1.0}" % NS
TEXT_P = "{%stext:1.0}p" % NS

# Lieferbarkeit je Link-Merkmal: (nicht lieferbar, Status, ggf. neue URL)
OK_AMAZON = (False, "lieferbar (Amazon: Auf Lager)", "")
OOS_AMAZON = (True, "nicht lieferbar (Amazon: Derzeit nicht verfügbar, Wiederverfügbarkeit unbekannt)", "")
OK_DOLD = (False, "lieferbar (DOLD: sofort verfügbar)", "")
AVAILABILITY = {
    "B00Y211AFM": OK_AMAZON,
    "B071ZQ6VV6": OK_AMAZON,
    "B072Q68493": OK_AMAZON,
    "B06WVJJFX1": OK_AMAZON,
    "B01IMGYPJU": OK_AMAZON,
    "B07SX1N19C": (False, "lieferbar (Amazon: nur noch 17 auf Lager)", ""),
    "B01JOTURAK": OOS_AMAZON,
    "B07D4GCYXW": OOS_AMAZON,
    "B01LO0IGZU": OOS_AMAZON,
    "B077XSG86T": OOS_AMAZON,
    "B06Y4NYJWN": OOS_AMAZON,
    "B07P73VWHK": OOS_AMAZON,
    "B07PX8ZFXN": OOS_AMAZON,
    "B07Q9JKK23": (True, "nicht lieferbar (Amazon-Artikel entfernt, HTTP 404)", ""),
    "nanotec.com/produkte/446": (True, "nicht lieferbar (Produktseite entfernt, nur noch im Nanotec-Archiv)", ""),
    "Aluminiumprofil-30x30L": (False, "lieferbar (DOLD-Zuschnitt; SW-Link 404, Artikel unter neuer URL)",
                               "https://www.dold-mechatronik.de/Aluminiumprofil-30x30L-I-Typ-Nut-6-leicht-094kg-m-Zuschnitt-50-6000mm"),
    "Aluminiumprofil-30x60L": (False, "lieferbar (DOLD-Zuschnitt; SW-Link 404, Artikel unter neuer URL)",
                               "https://www.dold-mechatronik.de/Aluminiumprofil-30x60L-I-Typ-Nut-6"),
    "Aluminiumprofil-40x16E": (False, "lieferbar (DOLD-Zuschnitt; SW-Link 404, Artikel unter neuer URL)",
                               "https://www.dold-mechatronik.de/Aluminiumprofil-40x16E-I-Typ-Nut-8"),
    "Aluminiumprofil-40x16S": (False, "lieferbar (DOLD-Zuschnitt; SW-Link 404, Artikel unter neuer URL)",
                               "https://www.dold-mechatronik.de/Aluminiumprofil-40x16S-I-Typ-Nut-8"),
    "Wellenhalter-Flansch-SHF10": (True, "nicht lieferbar (DOLD: nicht auf Lager, Lieferzeit auf Anfrage)", ""),
    "Gewindebohrungen-M5x20": (False, "lieferbar (DOLD: auf Lager, 3–4 Werktage)", ""),
    "dold-mechatronik.de": OK_DOLD,
    "igus.de/product/847": (False, "lieferbar (igus: versandfertig ab 24 h)", ""),
    "motedis.com": (False, "lieferbar (Motedis: auf Lager)", ""),
    "teleskopschienen24.de": (False, "lieferbar (Teleskopschienen24: sofort verfügbar, Preis je Paar)", ""),
}
WRONG_LINK = {39: "nicht prüfbar (SW-Link zeigt auf den Nanotec-Motor, nicht auf die Spindel)"}

# Laufende Nummer der nichtleeren Zeilen in BOM.ods (0-basiert, beide Blätter) -> (Modul,
# ersetzte Floronics-IDs, Hinweis). "Zeile n" in Hinweisen meint ebenfalls diese Nummer;
# die Ausgabe ersetzt sie durch Blatt und echte Tabellenzeile.
SW_MAP = {
    3: ("M01", ["BUY-C052"], "Identisch mit Recherche (DOLD GF-K-10-PA-028); Shoppreis 18.10.: 2,47 €"),
    4: ("M01, M05", ["BUY-C081"], "CAD zählt 26 Winkel (18 Rahmen + 8 Schublade), SW nennt 22"),
    5: ("M05", ["BUY-C051"], "Recherche: DOLD A-75873, gleicher Bügelgriff 100 mm"),
    6: ("M01", ["N-034"], "M6×20 gesamt SW (Zeilen 6/16/33): 26 Stk DIN 912; CAD zeigt 22 Stk DIN 7991 Senkkopf"),
    7: ("M05", ["BUY-C084"], "Shop verkauft paarweise: 1 Paar = 2 Schienen wie im CAD; Recherche hatte DOLD HS-4613-350"),
    8: ("M05", [], "In Recherche ohne Gegenstück (dort Griff M5×35, Teleskopschienen ISO 7380 M4×8)"),
    9: ("M05", [], "Recherche nutzt Nutensteine M5 für Griff (SYS-044) und Abdeckungen (SYS-060); Mengen prüfen"),
    10: ("M01", ["MAT-003"], "SW: 30×60 L (leicht); Recherche: 30×60 S (schwer, 71370-Z)"),
    11: ("M01, M05", ["MAT-002"], "SW: 15 Zuschnitte 30×30 (Zeilen 11–13); CAD zählt 17 Profile (CAD-011/012/013/020)"),
    12: ("M01", ["MAT-002"], "siehe Zeile 11"),
    13: ("M05", ["MAT-002"], "siehe Zeile 11"),
    14: ("M05", ["OPEN-CAD-010"], "Schubladen-Dummyplatte (CAD-010), in Recherche offen"),
    15: ("M01", ["MAT-006 (teilweise)"], "Entspricht CAD-096/097; Laserteil (Laserteile4you), Recherche: Werkstattfertigung lt. Entscheidung 17.10."),
    16: ("M01", ["N-034"], "siehe Zeile 6"),
    17: ("M02", ["BUY-019"], "Identisch mit Recherche (Motedis MR12M-N-600)"),
    18: ("M02", [], "In Recherche nicht enthalten"),
    19: ("M02", ["N-035"], "DIN 912 M3×10 gesamt SW (Zeilen 19/30/51/109): 164 Stk; CAD zählt 76"),
    21: ("M02", [], "Spindelantrieb aus V1.0; im CAD X-Riemenantrieb mit NEMA17 (siehe BOM_2)"),
    22: ("M02", ["N-036"], "DIN 912 M3×12 gesamt SW (Zeilen 22/35/108): 52 Stk; CAD zählt 8"),
    23: ("M02", [], "Nur beim Spindelantrieb V1.0, nicht im CAD"),
    24: ("M07", ["BUY-SEN"], "SW: 16× M12 (Zeilen 24/43) + 8× M8 (BOM_2) = 24 Sensoren; CAD: 24× M8, Recherche: ELCO NI4-M08-ON6L-Q8"),
    26: ("M03", [], "Spindelantrieb V1.0; im CAD nur Riemenklemme TR10x2_GT2_belt_adapter (CAD-001)"),
    27: ("M03", [], "Spindelantrieb V1.0, nicht im CAD"),
    28: ("M03", [], "In Recherche nicht enthalten"),
    29: ("M02", ["BUY-018", "ALT-001"], "SW: MR12MN (Standardlänge); CAD/Recherche: MR12ML (lang)"),
    30: ("M03", ["N-035"], "siehe Zeile 19"),
    31: ("M02", ["MAT-007"], "Identisch mit Recherche (40×16S, 4×436 mm)"),
    32: ("M02", ["MAT-006 (teilweise)"], "Entspricht CAD-099/100 x_side_plate(_moving), im CAD 8 Stk"),
    33: ("M02", ["N-034"], "siehe Zeile 6"),
    34: ("M03", [], "Y-Spindelantrieb V1.0; Upgrade auf NEMA17 siehe BOM_2"),
    35: ("M03", ["N-036"], "siehe Zeile 22"),
    36: ("M03", [], "Nur beim Spindelantrieb V1.0, nicht im CAD"),
    37: ("M03", [], "In Recherche nicht enthalten"),
    38: ("M03", [], "SW ohne Link und Preis; Recherche-Budget Sicherungselemente BUD-S030"),
    39: ("M03", [], "SW-Link fehlerhaft; Spindel im CAD nicht vorhanden"),
    40: ("M03", ["MAT-004"], "SW: mit M6-Gewinde, Link zeigt Variante M5×20; Recherche: Zuschnitt-Los CAD-069/098"),
    41: ("M03", [], "In Recherche nicht enthalten"),
    42: ("M03", [], "In Recherche nicht enthalten"),
    43: ("M07", ["BUY-SEN"], "siehe Zeile 24"),
    45: ("M04", ["N-044"], "M4×20 gesamt SW (Zeile 45 DIN 7984 + BOM_2 Zeile 113 DIN 912): 18 Stk; CAD 20× DIN 912; SW-Link zeigt DIN 912"),
    46: ("M04", ["N-057"], "SW 8 Stk; CAD zählt 64 Muttern M4"),
    47: ("M03", ["BUY-022"], "SW: RJMP-01-10, Recherche: RJ4JP-01-10; gesamt SW mit BOM_2 Zeile 103: 24 Stk, CAD 16"),
    48: ("M03", [], "In Recherche nicht enthalten"),
    49: ("M04", [], "Spindelantrieb V1.0, nicht im CAD"),
    50: ("M04", ["BUY-015"], "Ersatz aus Recherche: STEPPERONLINE 14HS13-0804S (gleicher Typ wie BOM_2 Zeile 96)"),
    51: ("M04", ["N-035"], "siehe Zeile 19; SW-Link zeigt M3×12"),
    52: ("M04", ["BUY-006"], "SW: GT2 6 mm; CAD zeigt Z-Riemenscheibe 9 mm"),
    53: ("M04", [], "In Recherche nur als X/Y-Umlenkrolle (BUY-005)"),
    54: ("M04", ["BUY-017"], "SW: 6 mm, 1 m je Probe; CAD: Z-Riemen 9 mm"),
    55: ("M04", ["BUY-021", "ALT-002"], "Z-Führungswagen; CAD/Recherche: HIWIN MGN12C"),
    56: ("M04", [], "In Recherche nicht enthalten"),
    57: ("M07", ["BUY-009"], "4 Packungen à 6 = 24 Stk; CAD 4"),
    59: ("M04", ["BUY-020"], "Z-Schiene; CAD/Recherche: HIWIN MGNR12R150"),
    60: ("M09", [], "SW ohne Angabe; Konkretisierung aus Recherche siehe M09-Zeilen"),
    62: ("M07", ["BUY-016"], "SW-Link zeigt BIGTREETECH SKR V1.3 (kein Smoothieboard); Ersatz aus Recherche: SKR 1.4 Turbo RBS13645"),
    63: ("M07", ["BUY-002"], "Ersatz aus Recherche: TMC2130 RBS13024"),
    64: ("M07", ["BUY-001"], "Ersatz aus Recherche/CAD: Mean Well RSP-200-24 (Reichelt)"),
    65: ("M07", [], "Konkretisierung aus Recherche: BUD-S020"),
    66: ("M09", [], "Konkretisierung aus Recherche: BUD-S022, MMCX CAD-061/062"),
    67: ("M07", [], "SW ohne Angabe; in Recherche kein Gehäuse, nur Controller-Befestigung BUD-S032"),
    68: ("M06", [], "Konkretisierung aus Recherche: igus BUY-008/023/024/025"),
    69: ("M07", ["BUY-CAB"], "Recherche: 24× ifm EVC141 nur für ELCO-Steckersensoren; SW-Sensoren haben Festkabel"),
    70: ("M07", [], "Konkretisierung aus Recherche: BUD-S014/S015"),
    89: ("M07", ["BUY-016"], "Mit V1.0 (1 je Probe) zusammen 6 Boards; CAD 4"),
    90: ("M07", ["BUY-002"], "Mit V1.0 zusammen 6 Packungen = 24 Treiber; Recherche 16"),
    91: ("M02, M03", ["BUY-014"], "2×5 = 10 NEMA17; CAD/Recherche 12 (8 X + 4 Y), Recherche: Nanotec ST4118M1804-A"),
    92: ("M02, M03", ["BUY-004"], "2×6 = 12 Ritzel, wie Recherche"),
    93: ("M02, M03", ["BUY-005"], "2×5 = 10 Umlenkrollen; CAD 20"),
    94: ("M07", ["BUY-SEN"], "siehe Zeile 24"),
    95: ("M02, M03", ["BUY-007"], "Recherche: 20 m als Reserve"),
    96: ("M04", ["BUY-015"], "Gleicher Typ wie Recherche 14HS13-0804S, dort direkt bei STEPPERONLINE"),
    97: ("M02", ["N-042"], "SW: 32 benötigt; CAD zählt 52"),
    98: ("M02", ["N-031"], "SW: 32 benötigt; CAD zählt 32"),
    99: ("M07", ["BUY-012"], "4 Ports; Recherche: 7-Port aktiv (4 SKR, Kameras, MUX)"),
    100: ("M02, M05", ["BUY-003"], "8 Stk; CAD 16"),
    101: ("M02, M05", ["MAT-004"], "siehe Zeile 40"),
    102: ("M05", ["MAT-005 (teilweise)"], "Vermutlich CAD-070 pcb_holder_rect_rod (2 Stk)"),
    103: ("M03", ["BUY-022"], "siehe Zeile 47"),
    104: ("M04", [], "Zusätzlich zu Zeile 59"),
    105: ("M02", ["N-046"], "CAD zählt 32"),
    106: ("M02", ["N-032"], "CAD zählt 16"),
    107: ("M01", [], "Ersatzteller für Gelenkfuß"),
    108: ("M02", ["N-036"], "siehe Zeile 22"),
    109: ("M02", ["N-035"], "siehe Zeile 19"),
    110: ("M02", ["MAT-006 (teilweise)"], "siehe Zeile 32"),
    111: ("M04", ["N-040"], "CAD zählt 4"),
    112: ("M02", ["N-038"], "CAD zählt 28"),
    113: ("M02", ["N-044"], "siehe Zeile 45"),
    114: ("M02", ["N-045"], "CAD zählt 36"),
}

# Floronics-Positionen, die nicht durch SW ersetzt werden, aber einen Hinweis brauchen
FLORONICS_NOTES = {
    "MAT-006": "Restumfang nach SW: Rückwand CAD-003, Adapterplatten CAD-016–019, Kamerahalter CAD-026 (Motor- und Seitenplatten siehe SW)",
    "MAT-005": "Restumfang nach SW: Distanzstäbe CAD-108 (Rechteckstange CAD-070 siehe SW BOM_2 Zeile 102)",
    "BUY-C059": "Nur nötig beim Mean-Well-Netzteil (Ersatz für nicht lieferbares SW-Netzteil)",
    "N-058": "SW-Sensoren werden mit Muttern geliefert; ggf. entbehrlich",
    "BUD-S014": "konkretisiert SW Zeile 70 (Motorkabel)",
    "BUD-S015": "konkretisiert SW Zeile 70 (Motorkabel)",
    "BUD-S020": "konkretisiert SW Zeile 65 (Schukokabel)",
    "BUD-S022": "konkretisiert SW Zeile 66 (Kabel Probe)",
    "BUD-S030": "enthält SW Zeile 38 (Sicherungsring D6)",
    "BUD-S032": "zu SW Zeile 67 (Gehäuse für Elektronik)",
    "OPEN-CAD-061": "konkretisiert SW Zeile 66 (Kabel Probe)",
    "OPEN-CAD-062": "konkretisiert SW Zeile 66 (Kabel Probe)",
    "BUY-008": "konkretisiert SW Zeile 68 (Energieketten)",
    "BUY-023": "konkretisiert SW Zeile 68 (Energieketten)",
    "BUY-024": "konkretisiert SW Zeile 68 (Energieketten)",
    "BUY-025": "konkretisiert SW Zeile 68 (Energieketten)",
    "BUY-PIN": "konkretisiert SW Zeile 60 (Probespitze)",
    "BUY-SYS-057": "konkretisiert SW Zeile 60 (Probespitze)",
    "OPEN-SYS-058": "konkretisiert SW Zeile 60 (Probespitze)",
    "OPEN-SYS-017": "Bei SW-Sensoren mit Festkabel prüfen, ob noch nötig",
    "BUY-SYS-044": "Gleiche Größe wie SW Zeile 9; Mengen prüfen",
    "BUY-SYS-060": "Gleiche Größe wie SW Zeile 9; Mengen prüfen",
    "OPT-001": "Option, nicht im Grundumfang",
}
# Keine Bauteile: Versand und Gebühren
EXCLUDED_PREFIXES = ("SHIP-", "FEE-")

HEADER = [
    "Nr", "Quelle", "SW-Blatt", "SW-Zeile", "SW-Abschnitt", "Modul", "Teil",
    "Menge laut SW", "je Probe", "Menge Vollausbau", "Einheit", "Preis brutto/Stk EUR",
    "Summe brutto EUR", "Lieferant", "Artikel-Nr.", "Link", "nicht lieferbar",
    f"Lieferstatus {CHECK_DATE}", "Floronics-IDs (ersetzt/zugeordnet)", "Abgleich / Hinweis",
]


def read_ods(path):
    root = ET.fromstring(zipfile.ZipFile(path).read("content.xml"))
    rows = []
    for table in root.iter(TABLE + "table"):
        sheet = table.get(TABLE + "name")
        row_no = 0
        for row in table.iter(TABLE + "table-row"):
            row_no += int(row.get(TABLE + "number-rows-repeated", "1"))
            cells = []
            for cell in row:
                repeat = min(int(cell.get(TABLE + "number-columns-repeated", "1")), 20)
                text = " ".join("".join(p.itertext()) for p in cell.iter(TEXT_P)).strip()
                cells += [text] * repeat
            while cells and not cells[-1]:
                cells.pop()
            if cells:
                rows.append((sheet, row_no, cells))
    return rows


def sheet_label(sheet):
    return "BOM V1.0" if sheet == "BOM" else "BOM_2 Probe Upgrade"


def resolve_refs(text, rows):
    """Ersetzt \"Zeile n\"-Verweise auf laufende Nummern durch Blatt und echte Tabellenzeile."""
    def expand(match):
        refs = []
        for part in match.group(2).split("/"):
            bounds = [int(n) for n in part.split("–")]
            refs += range(bounds[0], bounds[-1] + 1)
        return ", ".join(f"{rows[i][0]} Zeile {rows[i][1]}" for i in refs)
    return re.sub(r"(?:BOM_2 )?(Zeilen?) (\d+(?:[/–]\d+)*)", expand, text)


def parse_number(text):
    try:
        return float(text.replace(".", "").replace(",", "."))
    except ValueError:
        return None


def fmt(value):
    if value is None:
        return ""
    if float(value).is_integer():
        return str(int(value))
    return f"{value:.2f}".replace(".", ",")


def supplier_of(url):
    for key, name in [("dold", "DOLD"), ("amazon", "Amazon"), ("nanotec", "Nanotec"), ("igus", "igus"),
                      ("motedis", "Motedis"), ("teleskopschienen24", "Teleskopschienen24")]:
        if key in url:
            return name
    return ""


def availability(index, name, url):
    if index in WRONG_LINK:
        return False, WRONG_LINK[index], ""
    if not url:
        if "gelasert" in name:
            return False, "Fertigungsteil (Laserteile4you lt. SW, Website erreichbar)", ""
        return False, "nicht prüfbar (kein Link in SW-BOM)", ""
    for key, result in AVAILABILITY.items():
        if key in url:
            return result
    raise KeyError(f"Keine Lieferbarkeitsprüfung für {url}")


def schutzwerk_rows(rows):
    refs = [(sheet_label(sheet), row_no) for sheet, row_no, _ in rows]
    out, section = [], ""
    for index, (sheet, row_no, cells) in enumerate(rows):
        if index not in SW_MAP:
            if sheet == "BOM" and len(cells) == 1 and index > 1 and not cells[0].startswith("BOM"):
                section = cells[0]
            continue
        module, replaced, note = SW_MAP[index]
        name = cells[0]
        url = next((c for c in cells if c.startswith("http")), "")
        if sheet == "BOM":
            qty, price = cells[2] if len(cells) > 2 else "", cells[3] if len(cells) > 3 else ""
            per_probe = len(cells) > 5 and cells[5] == "x"
            sec = section
        else:
            qty, price = cells[1] if len(cells) > 1 else "", cells[2] if len(cells) > 2 else ""
            per_probe = False
            sec = "Probe Upgrade"
        qty_n, price_n = parse_number(qty), parse_number(price)
        total_qty = qty_n * (PROBES if per_probe else 1) if qty_n is not None else None
        not_avail, status, new_url = availability(index, name, url)
        hint = resolve_refs(note, refs) + (f"; aktueller Link: {new_url}" if new_url else "")
        out.append({
            "Quelle": "Original SCHUTZWERK", "SW-Blatt": sheet_label(sheet), "SW-Zeile": str(row_no),
            "SW-Abschnitt": sec, "Modul": module, "Teil": name, "Menge laut SW": qty,
            "je Probe": "x" if per_probe else "", "Menge Vollausbau": fmt(total_qty),
            "Einheit": "Stück" if qty else "", "Preis brutto/Stk EUR": price if price_n is not None else price,
            "Summe brutto EUR": fmt(total_qty * price_n) if total_qty is not None and price_n is not None else "",
            "Lieferant": supplier_of(url) or ("Laserteile4you" if "gelasert" in name else ""),
            "Artikel-Nr.": "", "Link": url, "nicht lieferbar": "x" if not_avail else "",
            f"Lieferstatus {CHECK_DATE}": status,
            "Floronics-IDs (ersetzt/zugeordnet)": ", ".join(replaced), "Abgleich / Hinweis": hint,
        })
    return out


def floronics_rows(replaced_ids, rows):
    with open(ORDER_LIST, encoding="utf-8-sig", newline="") as handle:
        positions = list(csv.DictReader(handle, delimiter=";"))
    out = []
    for pos in positions:
        pid = pos["ID"]
        if pid in replaced_ids or pid.startswith(EXCLUDED_PREFIXES):
            continue
        notes = [resolve_refs(FLORONICS_NOTES.get(pid, ""), rows)]
        if pos["Bestellmenge"] != pos["Bedarf"]:
            notes.append(f"Bestellmenge {pos['Bestellmenge']} {pos['Einheit']} (Packung/Los)")
        if pos["Prüfnotiz"]:
            notes.append(pos["Prüfnotiz"])
        out.append({
            "Quelle": "Floronics-Recherche", "SW-Blatt": "", "SW-Zeile": "", "SW-Abschnitt": "",
            "Modul": pos["Modul"], "Teil": pos["Beschreibung"], "Menge laut SW": "", "je Probe": "",
            "Menge Vollausbau": fmt(parse_number(pos["Bedarf"])), "Einheit": pos["Einheit"], "Preis brutto/Stk EUR": "",
            "Summe brutto EUR": pos["Brutto EUR"], "Lieferant": pos["Distributor"],
            "Artikel-Nr.": pos["Artikel-Nr."], "Link": pos["Bestelllink"], "nicht lieferbar": "",
            f"Lieferstatus {CHECK_DATE}": "nicht neu geprüft (Recherche-Stand 16.–18.10.2026)",
            "Floronics-IDs (ersetzt/zugeordnet)": f"{pid} ({pos['CAD/SYS-IDs']})" if pos["CAD/SYS-IDs"] else pid,
            "Abgleich / Hinweis": "; ".join(n for n in notes if n),
        })
    return out


def main():
    ods_rows = read_ods(ODS)
    sw = schutzwerk_rows(ods_rows)
    replaced = {pid for _, ids, _ in SW_MAP.values() for pid in ids if "(teilweise)" not in pid}
    rows = sw + floronics_rows(replaced, [(sheet_label(s), n) for s, n, _ in ods_rows])
    for number, row in enumerate(rows, 1):
        row["Nr"] = str(number)
    with open(OUTPUT, "w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER, delimiter=";")
        writer.writeheader()
        writer.writerows(rows)
    print(f"{OUTPUT.relative_to(ROOT)}: {len(sw)} SCHUTZWERK-Zeilen, {len(rows) - len(sw)} Floronics-Zeilen, "
          f"{sum(r['nicht lieferbar'] == 'x' for r in sw)} nicht lieferbar")


if __name__ == "__main__":
    main()
