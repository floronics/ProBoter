"""Render the extracted STEP inventory as a German, reviewable parts list."""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path


TOKEN = {
    "base": "Basis", "back": "Rückseite", "frame": "Rahmen",
    "long": "lang", "short": "kurz", "side": "Seite", "top": "oben",
    "cover": "Abdeckung", "plate": "Platte", "adapter": "Adapter",
    "vertical": "vertikal", "drawer": "Schublade", "holder": "Halter",
    "cable": "Kabel", "chain": "Energiekette", "drag": "Schlepp",
    "slide": "Schlitten", "rod": "Stange", "rail": "Schiene",
    "round": "rund", "rect": "rechteckig", "guiding": "Führung",
    "glider": "Gleiter", "distance": "Abstand", "tube": "Rohr",
    "belt": "Riemen", "drive": "Antrieb", "tightener": "Spanner",
    "motor": "Motor", "moving": "beweglich", "mirrored": "gespiegelt",
    "camera": "Kamera", "compact": "kompakt", "probe": "Prüfspitze",
    "tip": "Spitze", "pcb": "Platine", "end": "Ende",
    "stop": "Anschlag", "trigger": "Auslöser", "switch": "Schalter",
    "power": "Stromversorgung", "flange": "Flansch", "stiffener": "Versteifung",
    "beam": "Träger", "flat": "flach", "wing": "Flügel",
    "screw": "Schraube", "on": "an", "bracket": "Winkel",
    "x": "X-Achse", "y": "Y-Achse", "z": "Z-Achse",
    "left": "links", "right": "rechts", "inductive": "induktiv",
    "endstop": "Endschalter", "endschalter": "Endschalter",
    "pruefspitze": "Prüfspitze", "signal-multiplexer": "Signal-Multiplexer",
    "nut": "Mutter", "square": "Vierkant", "knurled": "Rändel",
    "high": "hoch", "nema": "NEMA", "to": "auf", "gt2": "GT2",
}

EXACT = {
    "bigtreetech_skr_v1_3": ("BIGTREETECH SKR V1.3 Steuerplatine", "MODELL BELEGT", "TMC2130-Treibermodule separat einplanen"),
    "mean_well_RSP-200-24": ("Mean Well RSP-200-24, 24-V-Netzteil", "MODELL BELEGT", "Netzanschluss, Absicherung und Leistungsauslegung prüfen"),
    "nanotec_nema_17_ST4118M1804-A": ("Nanotec ST4118M1804-A, NEMA-17-Schrittmotor", "MODELL BELEGT", "Motorzahl mit vier Achseinheiten abgleichen"),
    "nanotec_nema_14_ST3518M1004-A": ("Nanotec ST3518M1004-A, NEMA-14-Schrittmotor", "KLÄREN", "Nur im Nanotec-Archiv gefunden; Verfügbarkeit/Ersatz prüfen"),
    "hiwin_rail_MGNR12R150HM": ("HIWIN MGNR12R150HM Führungsschiene", "KLÄREN", "Ausführung und Schienenlänge/Endbearbeitung bestätigen"),
    "hiwin_slide_MGN12CZ0H": ("HIWIN MGN12CZ0H Führungswagen", "KLÄREN", "Exakte Suffixvariante und Paarung zur Schiene bestätigen"),
    "cpc_MR12ML": ("CPC MR12ML Miniatur-Führungswagen", "KLÄREN", "Vorspannung/Genauigkeitsklasse und Schiene festlegen"),
    "x_guiding_cpc_MR12M": ("CPC MR12M X-Führungsschiene", "KLÄREN", "Länge und genaue Ausführung fehlen im Namen"),
    "mean_well_MHS-012_mounting_bracket": ("Mean Well MHS-012 Montagewinkel", "KLÄREN", "Modellzuordnung und Bestellbarkeit prüfen"),
    "inductive_proximity_sensor_m8": ("Induktiver Näherungsschalter M8", "KLÄREN", "Schaltabstand, PNP/NPN, Versorgung und Stecker fehlen"),
    "optical_endstop": ("Optischer Endschalter", "KLÄREN", "Bauform, Versorgung, Anschluss und Schaltlogik fehlen"),
    "usb_microscope": ("USB-Mikroskop", "KLÄREN", "Auflösung, Optik, Haltermaß und reale Anzahl prüfen"),
    "probe_tip_pcb": ("Prüfspitzen-Platine", "KLÄREN", "Keine Gerber/Schaltpläne im Upstream; Fertigung offen"),
    "signal_multiplexer_dummy": ("Multiplexer-Platzhalter im CAD", "PLATZHALTER", "Echte Multiplexer-Platine samt Schaltplan/BOM fehlt"),
    "pcb_dummy": ("Prüfobjekt-Platzhalter im CAD", "PLATZHALTER", "Kein Maschinenteil; nicht bestellen"),
    "base_drawer_dummy_plate": ("Schubladen-Dummyplatte", "PLATZHALTER", "Prüfen, ob reale Schubladenplatte benötigt wird"),
    "plug_sleeve_P75-2_W": ("Prüfkontakt-Hülse P75-2 W", "KLÄREN", "Hersteller, Einbaumaß und passender Kontakt fehlen"),
    "z_pogo_pin": ("Federkontakt für Z-Prüfspitze", "KLÄREN", "Federweg, Spitzenform und Kontaktierung fehlen"),
    "mmcx_male_end": ("MMCX-Stecker, gerade", "KLÄREN", "Kabeltyp und konkrete Steckerbauform fehlen"),
    "mmcx_male_end_with_angle": ("MMCX-Stecker, gewinkelt", "KLÄREN", "Kabeltyp und konkrete Steckerbauform fehlen"),
    "vandalism_switch_d19": ("Vandalismussicherer Schalter Ø19 mm", "KLÄREN", "Schaltfunktion, Beleuchtung und Spannung fehlen"),
    "telescopic_bar_tsaa514613-350": ("Teleskopschiene TSAA514613-350", "KLÄREN", "Hersteller, Traglast und Lieferform bestätigen"),
    "handle_l100_dold": ("Schubladengriff L100", "KLÄREN", "Befestigungsabstand und Lieferant bestätigen"),
    "hinged_M6_40_dold": ("Gelenkfuß M6/40", "KLÄREN", "Fußdurchmesser, Gewindelänge und Lieferant bestätigen"),
    "screw_on_bracket_30_6": ("Anschraubwinkel 30/6", "KLÄREN", "Profilserie und Lochbild bestätigen"),
    "rod_holder_flange_d10_dold": ("Flanschhalter für Ø10-mm-Stange", "KLÄREN", "Lochbild und Bauform bestätigen"),
    "rod_slide_d10_l19": ("Gleitlager für Ø10 mm, L19", "KLÄREN", "Material und Außenmaß bestätigen"),
    "pulley_gt2_9mm": ("GT2-Riemenscheibe für 9-mm-Riemen", "KLÄREN", "Zähnezahl, Bohrung und Befestigung fehlen"),
    "pulley_gt2_z16_6mm": ("GT2-Riemenscheibe 16 Zähne / 6 mm", "KLÄREN", "Bohrung und Befestigung fehlen"),
    "return_pulley_gt2_z16_6mm": ("GT2-Umlenkrolle 16 Zähne / 6 mm", "KLÄREN", "Lager/Bohrung und Befestigung fehlen"),
    "x_belt": ("GT2-Riemen X-Achse", "KLÄREN", "Breite und Länge aus Konstruktion ermitteln"),
    "y_belt": ("GT2-Riemen Y-Achse", "KLÄREN", "Breite und Länge aus Konstruktion ermitteln"),
    "z_drive_belt": ("GT2-Riemen Z-Achse", "KLÄREN", "Breite und Länge aus Konstruktion ermitteln"),
}

CATEGORIES = [
    "Elektronik, Kameras und Prüfkontakte", "Antriebe und Linearführungen",
    "Energieketten, Riemen und Kaufmechanik", "Normteile und Befestigung",
    "CAD-Fertigungsteile", "Platzhalter und Modell-Dummys",
]


def humanize(name: str) -> str:
    clean = (name.removesuffix(".psm").replace("end_stop", "endschalter")
             .replace("probe_tip", "pruefspitze")
             .replace("signal_multiplexer", "signal-multiplexer"))
    if clean.startswith("base_"):
        return "Grundgestell: " + humanize(clean[5:])
    return " ".join(TOKEN.get(part.lower(), part.upper() if part.lower() in {"m3", "m4", "m5", "m6", "m8"} else part)
                    for part in clean.split("_"))


def classify(name: str) -> tuple[str, str, str, str]:
    if name in EXACT:
        description, status, note = EXACT[name]
    elif name.startswith(("din_", "iso_")):
        description = humanize(name).replace("x", "×")
        description = re.sub(r"\bm(\d+)", r"M\1", description)
        description = description.replace("din ", "DIN ").replace("iso ", "ISO ")
        description = description.replace("Rändel Mutter", "Rändelmutter").replace("Vierkant Mutter", "Vierkantmutter")
        status = "KLÄREN"
        note = ("Werkstoff/Festigkeitsklasse und Liefermenge prüfen" if "nut" in name
                else "Werkstoff/Festigkeitsklasse, Kopfvariante und Liefermenge prüfen")
    elif name.startswith("drag_chain_"):
        length = ".".join(name.split("_")[2:4]).replace("m", " m")
        description = "igus E2i.10 Energieketten-Abschnitt " + length
        status, note = "KLÄREN", "Gliederzahl, Länge und Endanschlüsse bestätigen"
    elif name.startswith(("base_", "x_", "y_", "z_", "pcb_holder_", "belt_tightener_", "TR10x2_")) or name in {
        "camera_holder", "camera_holder_top", "cable_cover", "power_switch_holder",
        "signal_multiplexer_holder",
    }:
        description = humanize(name)
        status, note = "FERTIGEN", "Einzelteil aus STEP separieren; Material, Toleranz und Verfahren festlegen"
    else:
        description = humanize(name)
        status, note = "KLÄREN", "Konkrete Bestellnummer oder Fertigungsangaben fehlen"

    if status == "PLATZHALTER":
        category = CATEGORIES[5]
    elif name.startswith(("din_", "iso_")):
        category = CATEGORIES[3]
    elif status == "FERTIGEN":
        category = CATEGORIES[4]
    elif name.startswith(("bigtreetech", "mean_well_RSP", "inductive", "optical", "usb_", "probe_tip", "plug_sleeve", "z_pogo", "mmcx", "vandalism", "signal_multiplexer")):
        category = CATEGORIES[0]
    elif name.startswith(("nanotec", "hiwin", "cpc_", "x_guiding", "rod_slide")):
        category = CATEGORIES[1]
    else:
        category = CATEGORIES[2]
    return category, description, status, note


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inventory", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    rows = list(csv.DictReader(args.inventory.open(encoding="utf-8-sig", newline="")))
    leaves = [row for row in rows if row["kind"] == "leaf"]
    if len(leaves) != 120:
        raise ValueError(f"Expected 120 CAD leaf names, found {len(leaves)}")

    grouped: dict[str, list[tuple[str, str, str, str, str]]] = defaultdict(list)
    for row in leaves:
        category, description, status, note = classify(row["cad_name"])
        grouped[category].append((row["cad_name"], row["quantity"], description, status, note))

    lines = [
        "# CAD-Teileliste (vollständige Rohinventur)", "",
        "Stand: 16.10.2026. Quelle: `hardware/3d_models/proboter.stp` "
        "(SCHUTZWERK, 19.04.2022). Die Mengen sind **Vorkommen im STEP-Modell**, "
        "keine geprüften Bestellmengen. Die 31 Baugruppen sind nicht zusätzlich zu bestellen.", "",
        "**Status:** `MODELL BELEGT` = Hersteller/Modell aus CAD und Herstellerquelle nachvollziehbar; "
        "`KLÄREN` = konkrete Variante oder Menge offen; `FERTIGEN` = Sonderteil mit "
        "Fertigungsangaben offen; `PLATZHALTER` = vor Bestellung durch reales Teil ersetzen/prüfen.", "",
        "Die Prioritäten und nicht im CAD enthaltenen Positionen stehen in [Bestellliste](Bestellliste.md).", "",
    ]
    for category in CATEGORIES:
        items = grouped.get(category, [])
        if not items:
            continue
        lines += [f"## {category} ({len(items)} Positionen)", "", "| CAD-Name | Stück | Beschreibung | Status | Vor Bestellung |", "|---|---:|---|---|---|"]
        for name, quantity, description, status, note in items:
            lines.append(f"| `{name}` | {quantity} | {description} | **{status}** | {note} |")
        lines.append("")

    lines += [
        "## Abgrenzung", "",
        "Alle 120 Blattteil-Namen aus dem Modell sind oben aufgeführt. Die zusätzliche "
        "[CSV-Inventur](cad-inventory.csv) enthält auch 14 Baugruppennamen (31 Vorkommen), "
        "damit keine Baugruppe doppelt gezählt wird. Die Klassifikation ist eine "
        "Beschaffungshilfe; sie ersetzt keine technische Freigabe des CAD-Modells.", "",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
