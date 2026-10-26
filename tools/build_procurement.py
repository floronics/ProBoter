"""Build the auditable four-probe procurement snapshot (standard library only).

Curated decisions below are deliberately separate from immutable CAD counts.
Prices live in bom/data/offers.json. Never interpret a missing price as zero.
Run from any directory: python tools/build_procurement.py
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from decimal import Decimal, ROUND_CEILING, ROUND_HALF_UP
from pathlib import Path

from render_cad_inventory import classify

ROOT = Path(__file__).resolve().parents[1]
BOM = ROOT / 'bom'
DATE = '2026-10-16'
D = Decimal
VAT = D('0.19')
CENT = D('.01')
BLOG = 'https://www.schutzwerk.com/en/blog/proboter-02/'
THESIS = '../publications/PROBoter_thesis.pdf'
FIRMWARE = '../firmware/Marlin/Configuration.h'
SOFTWARE = '../software/hardware-control/proboter/cli.py'
CAD = 'evidence/cad-geometry.csv'

SUPPLIER_URL = {
    'DOLD': 'https://www.dold-mechatronik.de/',
    'RBS': 'https://www.roboter-bausatz.de/',
    'REICHELT': 'https://www.reichelt.de/',
    'TME': 'https://www.tme.eu/de/',
    'SCHRAUBEN': 'https://schrauben-expert.de/',
    'NANOTEC': 'https://www.nanotec.com/eu/de/produkte/363-st4118m1804-a',
    'CPC': 'https://cpc-europe.com/',
    'HIWIN': 'https://www.hiwin.de/',
    'XOMETRY': 'https://xometry.eu/de/faq/',
    'BETA': 'https://de.beta-layout.com/leiterplatten/',
    'IGUS': 'https://www.igus.de/',
    'EISEN2000': 'https://www.eisenwaren2000.de/',
    'BEFFUCHS': 'https://www.befestigungsfuchs.de/',
    'MOTEDIS': 'https://www.motedis.com/de/',
    'DAMEN': 'https://www.damencnc.com/',
    'DIGIKEY': 'https://www.digikey.de/',
    'TINYTRONICS': 'https://www.tinytronics.nl/',
    'STEPPERONLINE': 'https://www.omc-stepperonline.com/de/',
    'RS': 'https://de.rs-online.com/',
    'AUTOMATION24': 'https://www.automation24.de/',
    'ELCO': 'https://shop.elco-automation.de/',
    'VOELKNER': 'https://www.voelkner.de/',
    'ELP': 'https://www.elpcctv.com/',
    'DOMOTICX': 'https://domoticx.net/',
    'PLATTENZUSCHNITT24': 'https://www.plattenzuschnitt24.de/',
    'JLCPCB': 'https://jlcpcb.com/',
    'OFFEN': '',
}

def money(v):
    return D(v).quantize(CENT, rounding=ROUND_HALF_UP)

def prose(text):
    """Separate compact notation used in the curated definitions for reading."""
    text=re.sub(r'(?<=[a-zäöüß])(?=[A-ZÄÖÜ])', ' ', str(text))
    text=re.sub(r'(?<=[a-zäöüß])(?=\d)', ' ', text)
    text=re.sub(r'(?<=\d)(?=(?:mm\b|cm³\b|m\b|kg\b|g\b|EUR\b|V\b|A\b|Stück|Stäbe|Motor|Controller|Wagen|Paare|Einheiten|Schienen|Vierer|Rollen|Flansch|NEMA|TMC|SHF|SKR|HIWIN|CPC|LED|USB|Verläufe|Abschnitt|Verbindung|induktiv|optisch|beweg|fest|Kamera|Paar|Enden|Ende|Sensor|Board|Kanäle|Riemen|Millimeter))',' ',text)
    for a,b in {'AlleTeile':'Alle Teile','jedeoffene':'jede offene','auchteilweisebekannte':'auch teilweise bekannte',
                'Eineunbekannte':'Eine unbekannte','lässtsichnichtaus eineräußeren':'lässt sich nicht aus einer äußeren',
                'keinefreigegebenen':'keine freigegebenen','alsMaterialvorschlagpreislichbestimmt':'als Materialvorschlag preislich bestimmt',
                'besitzenkonkrete':'besitzen konkrete','benötigenaber diejeweilsgenannte':'benötigen aber die jeweils genannte',
                'sindnochkeine':'sind noch keine','beweistkeine':'beweist keine','Druckteile sindnoch':'Druckteile sind noch',
                'unterLinux':'unter Linux','nichtversandt':'nicht versandt','ankeine':'an keine',
                'weiterenMikroskope':'weiteren Mikroskope','dreiweitere':'drei weitere',
                'Originalschaltpläne/BOM/Gerber':'Originalschaltpläne/BOM/Gerber',
                'einevierachsige':'eine vierachsige','mechanisch/elektrischverifizieren':'mechanisch/elektrisch verifizieren',
                'anbietenlassen':'anbieten lassen','keineMischungungeprüfter':'keine Mischung ungeprüfter',
                'Mikroskopbei':'Mikroskop bei','undstatische':'und statische','Halterdanachfestlegen':'Halter danach festlegen',
                'Fertigungszeichnungenmit':'Fertigungszeichnungen mit','aufeineSoftwareversionfestlegen':'auf eine Softwareversion festlegen',
                'Kabelwegeund':'Kabelwege und','undWarenkörbe':'und Warenkörbe','Bruttoangenommen':'Brutto angenommen',
                'bruttoangenommen':'brutto angenommen','Steuerbasisim':'Steuerbasis im','nicht imGrundtotal':'nicht im Grundtotal',
                'jeAnbieter':'je Anbieter','vorhandeneBestände':'vorhandene Bestände',
                'Filamentistals Materialvorschlagpreislichbestimmt':'Filament ist als Materialvorschlag preislich bestimmt',
                'einschließlichungeprüfter':'einschließlich ungeprüfter','desbezifferten':'des bezifferten',
                'nochunbezifferte':'noch unbezifferte','mitbeobachtetem':'mit beobachtetem','undübrige':'und übrige',
                'fürgeplant':'für geplant','ausgestattete':'ausgestattete','keine Developmentkosten':'keine Entwicklungskosten',
                '8Umlenk':'8 Umlenk','20Umlenk':'20 Umlenk','4Steuer':'4 Steuer','12X/Y':'12 X/Y',
                '17Original':'17 Original','14Z-Motor':'14 Z-Motor','1.3oder':'1.3 oder','je Teil':'je Teil',
                'proPackung':'pro Packung','brutto19%':'brutto 19%',
                'fürsonstige':'für sonstige','Steuerbasisoffen':'Steuerbasis offen',
                '0,41822':'0,41830','diese Höhen':'diese Höhen',
                'vorhandene SKR-Ausgang':'vorhandene SKR-Ausgang',
                'sindnichtdiese':'sind nicht diese','nichtEndflächenhöhe':'nicht Endflächenhöhe',
                'alleinausden':'allein aus den','ausder':'aus der','auseiner':'aus einer',
                'aufden':'auf den','anden':'an den','desRasters':'des Rasters',
                'keinevollständige':'keine vollständige','inSoftware':'in Software',
                'undin':'und in','sindverschiedene':'sind verschiedene',
                'vierre':'vier re','viererhöhte':'vier erhöhte','vieräußere':'vier äußere','vierweiße':'vier weiße',
                'undvier':'und vier','abM8':'ab M8','KeineDevelopmentkosten':'Keine Entwicklungskosten',
                'keinebeliebigen':'keine beliebigen','undreale':'und reale','4Hamming':'4 Hamming',
                'unbeziffertenPositionen':'unbezifferten Positionen'}.items(): text=text.replace(a,b)
    return text

def pack_count(need, size, minimum=1):
    if need is None:
        return None
    return max(int(minimum), int((D(str(need))/D(str(size))).to_integral_value(rounding=ROUND_CEILING)))

def ids(*numbers):
    return [f'CAD-{n:03}' for n in numbers]

# Routing decisions. These are proposals unless the part's evidence says otherwise.
SHEET = ids(3,96,97,99,100)
CNC = []  # adapter plates moved to the workshop (decision 17.10.2026)
WORKSHOP = ids(3,96,97,99,100)
# In SCHUTZWERK's Solid Edge folder printed_parts, so printed (decision 26.10.2026)
PRINTED_SE = ids(16,17,18,19,26)
MILLED = ids(96,97,99,100)
STOCK = ids(9,11,12,13,14,20,69,70,93,94,98,103,108)
PCB = ids(75)
UNIDENTIFIED = ids(10)
EXCLUDED = ids(66,82)
NORM = ids(*range(28,49),56,57,58)
NORM_RESERVE = 'Planmenge = CAD-Menge +10 %, mindestens +2 (Entscheidung 17.10.2026).'

def offers_by_cad():
    rows=json.loads((BOM/'data/offers.json').read_text(encoding='utf-8'))
    return {o['cad']:o for o in rows if o.get('cad')}

def with_reserve(quantity):
    return max(int((D(quantity)*D('1.1')).to_integral_value(rounding=ROUND_CEILING)), quantity+2)

# id -> (precise description, open question / evidence, preferred supplier)
DETAIL = {
23: ('Steuerplatine, ERSATZ: BIGTREETECH SKR 1.4 Turbo statt SKR V1.3', 'ORIGINAL AUSGETAUSCHT (Entscheidung Luis 17.10.2026): SKR V1.3 neu nicht lieferbar. SKR 1.4 Turbo: 110×85 mm, Löcher 102×76 (V1.3: 101,85×76,10), LPC1769, 5 Treibersteckplätze mit SPI. Marlin muss auf BOARD_BTT_SKR_V1_4_TURBO umgestellt werden; Endstop-, Treiber-CS- und SPI-MOSI-Pins ändern sich.', 'RBS'),
27: ('CPC MR12ML Führungswagen', '8 Wagen MR12MLSSV0N für 2×600-mm-Schienen. CPC-Katalog SS-Ausführung: L 47,6, Körperhöhe 10, Breite 27, Lochbild 20×20 M3 = CAD und Fusion-Messung. Lieferbarkeit bei Motedis prüfen.', 'MOTEDIS'),
49: ('igus E2i.10.10.028.0, 16 kurze Abschnitte', 'Teilung 20 mm, Außenbreite 17,4, Einbauhöhe 71 bei R28 = CAD. 0,24 m = 12 Glieder, zusammen 192 Glieder. Anschlüsse siehe SYS-027.', 'IGUS'),
50: ('igus E2i.10.20.028.0, 8 lange Abschnitte', 'Teilung 20 mm, Außenbreite 27,4, Einbauhöhe 71 = CAD. 0,28 m = 14 Glieder, zusammen 112 Glieder. Anschlüsse siehe SYS-028.', 'IGUS'),
51: ('Schubladengriff DOLD A-75873, Lochabstand 100 mm', 'Fusion-Messung: Bohrungen Ø5,5 durchgehend (29 mm) = Variante mit Befestigungsbohrungen A-75873 (Ø5,4, 112 statt 113 mm lang). Entscheidung Luis 17.10.2026. Befestigung SYS-044/045.', 'DOLD'),
52: ('Gelenkfuß M6×20 / Teller Ø40 mm', 'DOLD GF-K-10-PA-028: M6, Teller Ø40 = CAD; Fusion-Messung Gewindelänge 20 mm = Variante M6×20. Traglast vom Händler nicht angegeben.', 'DOLD'),
53: ('HIWIN MGNR12R150HM, Z-Schiene 150 mm', 'HIWIN-Katalog: 12×8, Teilung 25, Bohrung Ø3,5/Ø6; 150 mm mit 6 Bohrungen und Endabstand 12,5 = Fusion-Messung. Bezug Damen CNC (NL), Zuschnitt.', 'DAMEN'),
54: ('HIWIN MGN12CZ0HM Z-Führungswagen', 'Bestellschlüssel: Z0 spielfrei, H hohe Genauigkeit, M Edelstahl. Breite 27, Körperhöhe 10, Lochbild 20×15 M3 = CAD; Katalog-Länge 34,7 statt CAD 35,7.', 'DAMEN'),
55: ('Induktiver Näherungsschalter ELCO NI4-M08-ON6L-Q8 (AUSWAHL, Original unbekannt)', 'Spezifikation aus CAD und Firmware: M8, nicht bündig, NPN-Schließer (HIT_STATE LOW mit Pull-up), M8-Stecker. Gewählt (17.10.2026, günstigste passende Option): ELCO NI4-M08-ON6L-Q8, Sn 4 mm, 59,6 mm (CAD 60 mm), 10,44 EUR netto. Teurere Alternative SICK IME08-04NNSZT0S (RS). Datenblatt und Muttern im Lieferumfang noch prüfen.', 'ELCO'),
59: ('Mean Well MHS012 Montagewinkel', '4 Winkel für RSP-200. Mean-Well-Zeichnung 15×16,2×19,5 mm = CAD (Abweichung höchstens 0,3 mm). Reichelt MHS-012.', 'REICHELT'),
60: ('Mean Well RSP-200-24 Netzteil,24V/8,4A', 'Originalmodell,215×115×30mm. Lastbilanz, Absicherung, Berührungsschutz und Schutzleiter separat.', 'REICHELT'),
61: ('MMCX-Stecker gerade mit RG316, offenes Ende', 'Fusion: MMCX-Stecker mit Kabel Ø2,5 = RG316. rf-connectors.pl liefert MMCX-Pigtails RG316 offen nur bis 30 cm; 1 m nur mit SMA-Gegenstecker (abschneiden) oder als Sonderanfertigung. Länge an Kette/Messgerät festlegen.', 'OFFEN'),
62: ('MMCX-Stecker gewinkelt mit RG316, offenes Ende', 'rf-connectors.pl PT_MMCX MLS030Q: gewinkelt, RG316, offen, 30 cm, 33,95 zł. Für 1–1,5 m Sonderlänge anfragen oder MMCX–SMA 1 m kürzen.', 'OFFEN'),
63: ('NEMA14 Z-Motor, ERSATZ: STEPPERONLINE 14HS13-0804S statt Nanotec ST3518M1004-A', 'ORIGINALMOTOR AUSGETAUSCHT (Entscheidung Luis 17.10.2026). Original nur im Nanotec-Archiv. Ersatz 34,8 mm statt 36 mm lang, Welle Ø5×24 mit D-Abflachung, 0,8 A statt 1,0 A, 18 statt 14 Ncm, Litzen ohne Stecker. Motorstrom in der Firmware auf 0,8 A begrenzen. Fusion-Messung: nur 2,8 mm Luft zum Endschalter, kürzerer Motor passt.', 'STEPPERONLINE'),
64: ('Nanotec ST4118M1804-A NEMA17 X/Y-Motor', 'Originalmodell, aktuelle Nanotec-Serie: 1,8 A, 0,28 Nm, 38 mm, Welle Ø5×24, Litzen 300 mm mit JST XHP-4. 12 laut STEP (8 X + 4 Y), im Fusion-Import fehlend. Verfügbarkeit beim Hersteller anfragen.', 'NANOTEC'),
65: ('Optischer Endschalter 11×35 mm', 'RBS12901: 35×11 mm und Lochabstand 28 mm stimmen mit der Fusion-Messung überein. VCC/GND/SIG, 2,7–5 V, HIGH bei Unterbrechung. Pinfolge am SKR-Stecker vor dem Anschluss prüfen.', 'RBS'),
73: ('Aufnahmehülse R75 mit Drahtende (CAD: P75-2_W)', 'Fusion-Messung: Ø1,2 × 25,4 mm, Drahtende Ø0,6 × 5 mm = R75-Aufnahmehülse für P75 (Bohrung ca. 1,4 mm). Kein EU-Angebot mit Preis gefunden; Peaktest R75-Serie nur auf Anfrage.', 'OFFEN'),
75: ('Prüfspitzen-PCB, unbestückt', '4 Stück; CAD nur Quader 26,67×10,96×1,6 mm ohne Daten. Entscheidung Luis 17.10.2026: Originaldaten bei SCHUTZWERK angefragt (Anfrage durch Luis versendet, Antwort offen).', 'BETA'),
76: ('GT2-Zahnscheibe Z16 / 9 mm / Bohrung 5 mm, ANPASSUNG', 'Exaktes Teil (Ø18×11) in der EU nicht lieferbar. RBS12867 (Ø13×19,5, für 10-mm-Riemen) wird verwendet; Y-Schlitten-Druckteil und Umlenkachse müssen angepasst werden (Entscheidung Luis 17.10.2026). Fusion-Messung: Umlenkscheibe hat nur 3 mm Luft zum Schlitten.', 'RBS'),
77: ('GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm', '12 X/Y-Antriebe. RBS10278: Bordscheibe Ø14 statt CAD Ø13; Fusion-Messung zeigt 4,6 mm Abstand zum nächsten Teil, passt.', 'RBS'),
78: ('GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm', '20 Stück. Tinytronics 002225: Bohrung 3, Ø13, Breite 8,5 mm = CAD exakt (Rollen sitzen paarweise ohne Luft zwischen den Spannerflügeln).', 'TINYTRONICS'),
79: ('SHF10 Flanschhalter fürØ10mm Welle', '16 Stück.43×24×10mm undØ5,5-Befestigung stimmen mitDOLD11260 überein. Liefertermin27.11.2026 angekündigt.', 'DOLD'),
80: ('Lineargleitbuchse Ø10 innen / Ø19 außen / Länge 29 mm', 'igus RJ4JP-01-10: d 10, D 19, B 29, Nut Ø18 = CAD und Fusion-Messung. iglidur J4, LM10UU-Bauform.', 'DOLD'),
81: ('Anschraubwinkel 30 / Nut 6', 'DOLD 62378 (I-Typ Nut 6) 28×28×28 = CAD; bestellt als Satz 62385-BS mit Schrauben und Nutensteinen.', 'DOLD'),
84: ('Teleskopschiene 350 mm, Vollauszug', 'DOLD HS-4613-350 (CAD-Name enthält 4613): 350×45,7×12,7 (CAD 45,5), 1 Paar = die 2 CAD-Schienen. Vollauszug 354 mm.', 'DOLD'),
85: ('Bewegliches USB-Mikroskop Toolcraft 2 MP (AUSWAHL, ANPASSUNG)', 'Original unbekannt. Gewählt (Luis 17.10.2026): Toolcraft USB-Mikroskop 2 MP, Ø33×110 mm, Fokus 0–150 mm; CAD-Halter ist für Ø36 → 1,5-mm-Hülse oder Halter anpassen. UVC/Linux vor Einbau testen. Plan 1 Stück, 3 optional.', 'VOELKNER'),
86: ('Netzschalter Ø19 ONPOW LAS1A-ZG24, rastend', 'Funktion Netzschalter rastend (Luis 17.10.2026). Reichelt VS LAS1A-ZG24: Ø19, 5 A/250 V AC, Ring-LED 24 V. Rastend aus Typcode abgeleitet, vor Bestellung bestätigen.', 'REICHELT'),
87: ('GT2-Riemen X, 6 mm breit', '8 Verläufe, offen mit Spanner an beiden Enden. Fusion-Messung: 699 mm Trum, Teillänge 1.430 mm je Verlauf; Zuschnitt mit 2×40 mm Klemmzugabe ca. 1,51 m. Summe X+Y ca. 16,5 m aus zwei 10-m-Rollen.', 'DOLD'),
95: ('CPC MR12M Führungsschiene 600 mm', '2 Stück MR12M-N-600: 12×7,5 mm, Teilung 25, 24 Bohrungen Ø3,5/Ø6, Endabstand 12,5 = CAD. Nicht mit HIWIN MGN mischen.', 'MOTEDIS'),
104: ('GT2-Riemen Y, 6 mm breit', '4 Verläufe. Fusion-Messung: 492 mm Trum, Teillänge 1.016 mm; Zuschnitt mit 2×40 mm Klemmzugabe ca. 1,10 m. Einkauf gemeinsam mit CAD-087, nicht doppelt rechnen.', 'DOLD'),
113: ('GT2-Riemen Z, 9 mm breit', '4 Verläufe, offen am Z-Riemenhalter geklemmt. Fusion-Messung: Achsabstand 108 mm, Teillänge 248 mm; Zuschnitt mit 2×35 mm Klemmzugabe ca. 0,32 m, zusammen 1,3 m. RBS14040 als Meterware.', 'RBS'),
115: ('Federkontakt P75-B1 (Nadelspitze, wie CAD)', 'Fusion-Messung: Ø1,0 × 16,6 mm, 30°-Spitze = Standard P75-B1. Domoticx 0,18 EUR/Stück. Spitzenauswahl ergänzt: P75-E2 Kegel (SYS-057) und Flachspitze (SYS-058).', 'DOMOTICX'),
}

# Explicit non-CAD system inventory. Quantities are planning values, not discoveries.
# key, description, quantity, unit, group, supplier, specification/gap, source
SYSTEM = [
('001','TMC2130 SPI Treibermodule',16,'Stück','Kaufteile','RBS','4 je SKR für X/X2/Y/Z. RBS13024: 4 Treiber mit Kühlkörpern und Kabel, SPI-Pins laut Fotos vorgelötet. Revision nicht angegeben; SPI-Modus laut Datenblatt per Lötbrücke CFG4/CFG5 prüfen.',FIRMWARE),
('002','Stationäre Übersichtskamera ELP-USBFHD01M-H100',1,'Stück','Kaufteile','ELP','Gewählt (Luis 17.10.2026): ELP-USBFHD01M-H100, 1080p, UVC, 100°, Preis auf Anfrage; Lochraster beim Kauf bestätigen. Fusion-Messung: Halter CAD-025 hat 4 M2-Bohrungen im Raster 28×28 mm = 32×32-mm-USB-Platinenkamera (z. B. ELP, 1080p, UVC, M12-Objektiv), keine Webcam (Entscheidung Luis 17.10.2026). Logitech C920 passt nicht.',BLOG),
('003','Signal-Multiplexer, unbestückte Leiterplatte',1,'Stück','PCB extern','JLCPCB','SCHUTZWERK-Original: 4 Lagen, Gerber hardware/signal-multiplexer/hardware/gerber1.1/gerber1.1.zip (deckungsgleich mit mux.kicad_pcb, geprüft 26.10.2026). Bei JLCPCB bestellen.','../hardware/signal-multiplexer/hardware/mux.kicad_pcb'),
('004','Kalibrier-Referenzplatte, Alu schwarz',1,'Stück','Weitere Fertigung','OFFEN','WERKSTATT (Entscheidung Luis 18.10.2026): Alu gefräst/gebohrt, schwarz eloxiert oder lackiert. Dicke 5,1 mm (cli.py); Größe ca. 130×110 mm aus software/docu/images/calibration_plate_top.png geschätzt. 4 Türme für die erhöhten Stifte; Marker eingraviert. Zeichnung aus den Software-Maßen erstellen.','../software/hardware-control/proboter/cli.py'),
('005','Innere Messing-Referenzzylinder Ø7/8/9/10',4,'Stück','Weitere Fertigung','OFFEN','WERKSTATT aus Messing-Rundstab (Entscheidung Luis 18.10.2026): je 1× Ø7/8/9/10 mm, Raster 11,95×19,95 mm, Endfläche bündig mit der Plattenoberfläche. Länge = Plattendicke 5,1 mm plus Einpresstiefe.','../software/hardware-control/proboter/tasks/utils/reference_board.py'),
('006','Kalibriermarker, in die Platte graviert',1,'Satz','Weitere Fertigung','OFFEN','Hamming-Marker IDs 1/3/6/12 (mtracker-Format), je 18,2×18,2 mm, Raster 60×80 mm; weiß in die schwarze Platte lasern/gravieren (Entscheidung Luis 18.10.2026).','../software/hardware-control/proboter/tasks/utils/reference_board.py'),
('007','Weißer 24-V-LED-Streifen LUXULA LX700101',1.9,'m','Kaufteile','REICHELT','Rundum oben innen am Rahmen (Entscheidung Luis 18.10.2026): 2×590 + 2×350 mm ≈ 1,9 m aus 5-m-Rolle. 4500 K, 28 W je 5 m ⇒ ca. 10,6 W / 0,44 A bei 1,9 m. PWM-Flimmern mit der Kamera testen.',BLOG),
('008','LED-Aluprofile Barthelme BARdolino mit Diffusor, Kappen, Klammern',1,'Satz','Kaufteile','REICHELT','2 Profile 1 m flach, 2 Abdeckungen opal, 4 Endkappen, 6 Klammern; Klammern auf die Rahmenprofile schrauben (Entscheidung Luis 18.10.2026).',BLOG),
('009','LED-Anschluss an den Heizbett-Ausgang der Licht-Steuerplatine',1,'Satz','Kaufteile','REICHELT','Configuration_adv.h:4396 setzt PROBOTER_LIGHT_CONTROL_PIN auf HEATER_BED_PIN; M376 steuert Helligkeit. Kein separater USB-LED-Controller nötig. Stecker/Leitungen, Strom und Flimmern prüfen; keine zusätzliche MOSFET-Platine pauschal kaufen.','../firmware/Marlin/Configuration_adv.h'),
('010','USB-Hub7Port aktiv',1,'Stück','Kaufteile','REICHELT','Steuergeräte am Hub; zwei separate Kamera-Hostports vorausgesetzt. Netzteil und Hubkabel enthalten.',SOFTWARE),
('011','USB-Kabel für4SKR',4,'Stück','Kaufteile','REICHELT','HostUSB-A auf BoardUSB-B bestätigen; Länge vorläufig2m jeBoard, Ports/Verlegung prüfen.',FIRMWARE),
('012','USB-Kabel für MUX/UART/Zielversorgung',3,'Stück','Kaufteile','REICHELT','3 Verbindungen aus Softwarekonfiguration, Geräteseite und enthaltene Kabel offen; nur nach Geräteauswahl kaufen.',SOFTWARE),
('013','Bewegliche Kameraleitung / USB-Verlängerung',1,'Stück','Kaufteile','REICHELT','Schleppkettengeeignete Leitung/Länge/Stecker offen; Kamera-Beipack gegenrechnen.',BLOG),
('014','Motorleitungen4adrig',32,'m','Kaufteile','TME','Plan16×2m; Schleppkettenradius, Querschnitt/Strom, Aderfarben und reale Wege offen.',FIRMWARE),
('015','Motor-Gegenstecker und Crimpkontakte',32,'Satz','Kaufteile','TME','Plan2Enden je16Motoren. Board-/Motorhersteller-Raster und Kontaktzahl prüfen; beiliegende Kabel abziehen.',FIRMWARE),
('016','Sensorleitungen / Verlängerungen',24,'Stück','Kaufteile','TME','Für24 induktive Sensoren; enthaltene Anschlussleitungen zuerst prüfen. Optische1m-Kabel sind beiO-009 enthalten.',CAD),
('017','Sensor-Gegenstecker und Kontakte',28,'Satz','Kaufteile','TME','24induktiv+4optisch; bei steckerfertigem Beipack reduzieren. Keine generischen JST/Dupont ohne Rasterprüfung.',CAD),
('018','24-V-Verteilung, Sicherungen, Klemmen, Leitungen',1,'Satz','Kaufteile','REICHELT','4Controller+Sensoren+LED; Last/Stromlaufplan, Aderquerschnitte und Sicherungswerte bestimmen.',FIRMWARE),
('019','Sensor-Pegelanpassung / Eingangsschutz',24,'Kanäle','PCB extern','BETA','Bedarf abhängig von M8-Ausgang; 24V/3,3V-Interface. Keine Schaltung/BOM vorhanden; nicht blind24Module bestellen.',FIRMWARE),
('020','Netzeinspeisung, Leitung, Sicherung und Zugentlastung',1,'Satz','Kaufteile','REICHELT','230V-Anschluss an offenes Netzteil: Anschlussmodul, Netzleitung, Sicherungshalter und geschützter Kabelweg planen.',CAD),
('021','Schutzleiter, Ringkabelschuhe und Klemmenabdeckung',1,'Satz','Kaufteile','REICHELT','Metallrahmen/Netzteil erden; Querschnitt, Anschlusspunkte und Prüfverfahren in Stromlaufplan dokumentieren.',CAD),
('022','Messkoax und instrumentenseitige Adapter',4,'Kanäle','Kaufteile','TME','Vorhandene Messgeräte verwenden; BNC/SMA/MMCX und Impedanz gerätespezifisch. CAD-MM CX-Stecker61/62 sind separat, hier nur Kabel und Instrumentadapter.',SOFTWARE),
('023','Signal-Multiplexer Bestückung',1,'Baugruppe','PCB extern','JLCPCB','Board-BOM hardware/signal-multiplexer/hardware/mux.csv (76 Bauteile, u. a. 6 Relais TE 6-1462037-3, SMA, USB-B, DB9). Bestückung bei JLCPCB oder selbst; MPNs/LCSC-Nummern noch zuordnen.','../hardware/signal-multiplexer/hardware/mux.csv'),
('024','Prüfspitzen-PCB Bestückung',4,'Baugruppen','PCB extern','BETA','CAD-MM CX/Federkontakte separat; zusätzliche Buchsen und Bauteile erst aus Schaltplan. Unbestückte PlatineCAD-075 nicht erneut zählen.',CAD),
('025','USB-UART-Adapter',1,'Stück','Kaufteile','TME','Software setzt Adapter voraus; Pegel, Isolation, Pinout und Zielversorgung prüfen; Laborausstattung ggf. gegenrechnen.',SOFTWARE),
('026','Zielplatinen-Versorgungscontroller',1,'Baugruppe','PCB extern','BETA','Softwareziel /dev/proboter_target-power-controller; Schaltung, Firmware/Hardware und Kabel fehlen. Separat vom RSP-Netzteil.',SOFTWARE),
('027','Energieketten-Endanschlüsse schmal',16,'Sätze','Kaufteile','DIGIKEY','igus E2.100.10.34PZ, beidseitig schwenkbar mit Zugentlastung; Breite 17,4 = Anschlusskörper im CAD (Fusion-Messung).',CAD),
('028','Energieketten-Endanschlüsse breit',8,'Sätze','Kaufteile','DIGIKEY','igus E2.100.20.34PZ; Breite 27,4 = Anschlusskörper im CAD (Fusion-Messung).',CAD),
('029','Profil-Nutensteine und Zusatzbefestigung',1,'Satz','Kaufteile','DOLD','Nut6/Profilserie klären; 26Winkel plus Halter. CAD-Vierkantmuttern29/30 und mitgelieferte Winkelsätze abziehen.',CAD),
('030','Scheiben, Sicherungselemente, Distanzteile',1,'Satz','Kaufteile','SCHRAUBEN','Ergänzungsbedarf je Verschraubung/Idler; CAD-Normteile und Sensor-Beipack abziehen. Stückzahlen noch offen.',CAD),
('031','Lötzinn, Schrumpfschlauch, Binder, Labels, Kleber',1,'Satz','Kaufteile','REICHELT','Verbrauchsmaterialbudget; vorhandene Bestände später abziehen. Werkzeuge nicht enthalten.',CAD),
('032','Controller-Befestigung und Kühlung',1,'Satz','Kaufteile','RBS','Abstandshalter, Isolierung, ggf.Lüfter; SKR/TMC-Beipack und thermische Auslegung prüfen.',FIRMWARE),
('033','Zusätzliche bewegliche Kameras',3,'Stück','Optional','REICHELT','Optional zur Vollbestückung aller4CAD-Halter; zusätzliche USB-Ports/Bandbreite/Kabel separat dimensionieren.',CAD),
('034','Host-PC, Messgeräte und Werkzeuge',1,'Bestand','Nicht benötigt','OFFEN','Vom Käufer vorhanden; Kosten ausgeschlossen. Software nennt PicoScopePS5000a; bestehendes Gerät/Hostkompatibilität prüfen.',SOFTWARE),
('035','Z-Antriebsriemenscheibe / integrierter Adapter',0,'Stück','Nicht benötigt','OFFEN','Entfällt: Fusion-Messung zeigt die Antriebsrolle als CAD-076 koaxial auf der Ø5-Motorwelle. CAD-001/002 sind keine Riemenscheiben.',FIRMWARE),
('036','USB-/Versorgungsanschlüsse der Kalibrierung',1,'Prüfung','Nicht benötigt','OFFEN','Passive Referenzplatte benötigt nach veröffentlichtem Konzept keine eigene USB-Elektronik; kein zusätzliches Gerät.',BLOG),
('037','Weiße äußere Kalibrierreferenzen Ø10',4,'Stück','Weitere Fertigung','OFFEN','WERKSTATT aus weißem POM-Rundstab, Ø ca. 10 mm aus der Abbildung geschätzt (Entscheidung Luis 18.10.2026). Raster 109,9×89,8 mm, bündig.','../software/hardware-control/proboter/model/reference_board_config.py'),
('038','Kalibrier-Kontaktleitungen und gemeinsame Messreferenz',1,'Satz','Kaufteile','TME','4SKR-Zentriereingänge P0_17 mitPull-up/aktivLow sowie Referenzkörper/Kontaktkreis verdrahten. Netzplan, Stecker, Länge undBezugspotenzial mitMultiplexer klären; keineVerbindung ungeprüft festlegen.','../firmware/Marlin/src/module/proboter.cpp'),
('039','Erhöhte Messing-Referenzzylinder',4,'Stück','Weitere Fertigung','OFFEN','WERKSTATT aus Messing-Rundstab Ø7 (Entscheidung Luis 18.10.2026): Raster 59,6×39,9 mm, Endflächen 6/8/10/12 mm über der Plattenoberfläche, in Türmen der Platte.','../software/hardware-control/proboter/tasks/utils/reference_board.py'),
('040','Äußere flache Messing-Referenzzylinder Ø7',4,'Stück','Weitere Fertigung','OFFEN','WERKSTATT aus Messing-Rundstab Ø7 (Entscheidung Luis 18.10.2026): Mittelpunkte (±54,95; 0) und (0; ±44,9) mm, bündig.','../software/hardware-control/proboter/tasks/utils/reference_board.py'),
('041','Nutenstein I-Typ Nut 6, M6, Motorplatten',0,'Stück','Nicht benötigt','OFFEN','Entfällt (Luis 18.10.2026): Fusion-Messung zeigt die 8 Senkschrauben M6×20 der Motorplatten in den Stirnseiten der 60×30-Profile auf den Kernbohrungen, nicht in der Nut. M6-Gewinde intern, siehe CAD-014.',CAD),
('042','Nutenstein I-Typ Nut 6, M4, Rückwand',6,'Stück','Kaufteile','DOLD','Fusion-Kontaktanalyse M01: 6 Bohrungen Ø4,5 der Rückwand liegen auf den langen Profilen; im CAD keine Befestigung.',CAD),
('043','Zylinderschraube DIN 912 M4×10 A2, Rückwand',6,'Stück','Kaufteile','SCHRAUBEN','Zu SYS-042; 3 mm Rückwand plus Nutenstein.',CAD),
('044','Nutenstein I-Typ Nut 6, M5, Griff',2,'Stück','Kaufteile','DOLD','Griff A-75873 mit Durchgangsbohrungen wird von vorn ins Schubladenprofil geschraubt.',CAD),
('045','Zylinderschraube DIN 912 M5×35 A2, Griff',2,'Stück','Kaufteile','SCHRAUBEN','Länge aus 29 mm Griffbein plus Nutenstein; Schrauben.Expert 912 5 35 A2.',CAD),
('046','Zylinderschraube DIN 912 M4×10 A2, Wellenhalter',7,'Stück','Kaufteile','SCHRAUBEN','Fusion-Messung: 4 Wellenhalter mit je 2 Bohrungen Ø4,5 über der Nut der Schubladen-Querprofile; 1 von 8 Schrauben im CAD.',CAD),
('047','Nutenstein I-Typ Nut 6, M4, Wellenhalter',8,'Stück','Kaufteile','DOLD','Gegenstück zu den 8 Wellenhalter-Schrauben.',CAD),
('048','Linsenkopfschraube ISO 7380-1 M4×8 A2, Teleskopschienen',12,'Stück','Kaufteile','SCHRAUBEN','ANNAHME (Luis 17.10.2026): je Schiene 3 Schrauben zum Rahmen und 3 zur Schublade; im CAD keine Befestigung. Linsenkopf ISO 7380-1, Kopfhöhe 2,2 mm.',CAD),
('049','Nutenstein I-Typ Nut 6, M4, Teleskopschienen',12,'Stück','Kaufteile','DOLD','ANNAHME, Gegenstück zu SYS-048.',CAD),
('050','Zylinderschraube DIN 912 M3×8 A2, Kabelhalter M3',4,'Stück','Kaufteile','EISEN2000','Fusion: Kabelhalter 3,4 mm dick auf den M3-Gewinden des Kettenhalter-Profils (Wand 3,8 mm). Planmenge mit Reserve +10 %, mindestens +2.',CAD),
('051','Zylinderschraube DIN 912 M3×10 A2, igus-Kettenanschlüsse',106,'Stück','Kaufteile','EISEN2000','ANNAHME: 48 Anschlusselemente mit je 2 Bohrungen Ø3,2 (Fusion), je eine M3×10 mit Mutter; davon 16 am Kettenadapter (Wand 5,2 mm). Planmenge mit Reserve +10 %, mindestens +2.',CAD),
('052','Zylinderschraube DIN 912 M3×12 A2, Z-Kabelhalter',6,'Stück','Kaufteile','EISEN2000','ANNAHME: Kabelhalter 3,4 mm an der Z-Schiene, mit Mutter. Planmenge mit Reserve +10 %, mindestens +2.',CAD),
('053','Sechskantmutter DIN 934 M3 A2, Kabelführung',111,'Stück','Kaufteile','SCHRAUBEN','Muttern zu SYS-051 und SYS-052. Planmenge mit Reserve +10 %, mindestens +2.',CAD),
('054','Linsenkopfschraube ISO 7380-1 M4×8 A2, Kabelführung',11,'Stück','Kaufteile','SCHRAUBEN','1× Kabelhalter M4 auf dem Rahmenprofil (4,5 mm + Nutenstein), 8× Kettenadapter auf dem Versteifungsträger (ANNAHME, Gegenstück hängt vom Profil CAD-103 ab). Planmenge mit Reserve +10 %, mindestens +2.',CAD),
('055','Nutenstein I-Typ Nut 6, M4, Kabelhalter',3,'Stück','Kaufteile','DOLD','Für den Kabelhalter M4 am Rahmenprofil. Planmenge mit Reserve +10 %, mindestens +2.',CAD),
('056','Zylinderschraube DIN 912 M5×10 A2, Kabelhalter M5',6,'Stück','Kaufteile','SCHRAUBEN','Fusion: Kabelhalter 5,5 mm auf der Seitenplatte des X-Wagens (M5-Gewinde). Planmenge mit Reserve +10 %, mindestens +2.',CAD),
('057','Prüfstifte P75-E2 Kegelspitze (Spitzenauswahl)',10,'Stück','Kaufteile','DOMOTICX','Spitzenauswahl nach Wunsch Luis (17.10.2026): zusätzlich Kegelspitzen; 8 + Reserve.',CAD),
('058','Prüfstifte P75 Flachspitze zum Bestromen von Pads (Spitzenauswahl)',10,'Stück','Kaufteile','OFFEN','Wunsch Luis (17.10.2026). Flachspitzen-Code uneinheitlich (Peaktest: F flach, A konkav, D2 Kuppe); kein Lagerangebot gefunden, Spitzenzeichnung beim Händler anfordern.',CAD),
('059','Zylinderschraube DIN 912 M5×10 A2, Abdeckungen',18,'Stück','Kaufteile','SCHRAUBEN','Abdeckungen aus Acrylglas: beim Aufbau anzeichnen und bohren, je Platte 4 Schrauben (Entscheidung Luis 18.10.2026). Unterlegscheiben für Acryl empfohlen.',CAD),
('060','Nutenstein I-Typ Nut 6, M5, Abdeckungen',18,'Stück','Kaufteile','DOLD','Gegenstück zu SYS-059.',CAD),
]

def make_parts():
    global NORM_OFFERS
    NORM_OFFERS = offers_by_cad()
    with (BOM/CAD).open(encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    result = []
    for g in rows:
        key, name = g['id'], g['cad_name']
        old_group, title, _, note = classify(name)
        group, supplier = 'Kaufteile', 'DOLD'
        status = 'teilweise geklärt'
        material = 'nicht belegt'
        process_evidence = 'nicht zutreffend'
        if old_group == 'CAD-Fertigungsteile':
            group, status, supplier = '3D-Druck intern', 'Fertigung noch offen', 'RBS'
            material = 'PETG vorgeschlagen; Importmaterial Stahl ist kein Nachweis'
            process_evidence = 'vorgeschlagen; Blog beschreibt 3D-Druck komplexer Halter'
            note = 'Geometrie vorhanden; Druckorientierung, Passungen, Befestigung und Belastbarkeit festlegen. Volumen siehe CSV; kein Slicerbedarf.'
        if key in SHEET:
            group, supplier, status = 'Blech intern', 'DOLD', 'Fertigung noch offen'
            material = 'Stahl S235 vorgeschlagen; Abdeckungen alternativ Alublech, nicht freigegeben'
            process_evidence = 'vorgeschlagen'
            note = 'Hüllmaß siehe Geometrie. Blechdicke, Bohrbild/Gewinde, Biegeradius, Abwicklung und Kantenbearbeitung noch als Zeichnung festlegen.'
            if key in ids(96,97,99,100):
                process_evidence = 'Laserschneiden belegt: Blog Basis; Thesis PDF-Seite67 Seitenteile'
                material = ('Stahl für Basisplatten belegt; Sorte vorgeschlagen S235' if key in ids(96,97)
                            else 'Werkstoff nicht eindeutig belegt; S235 vorgeschlagen')
                note = '5mm geometrische Dicke; Kontur und Bohrungen aus CAD, Gewinde/Senkungen und Bezugs-/Lagetoleranzen fehlen. Entgraten vor Montage.'
            if key in ids(119,120):
                note = 'CAD .psm und dünner Körper sprechen für Blech; Dicke, Biegung und Sensor-Triggerwirkung nachweisen. Hüllmaß ist keine Abwicklung.'
        if key in PRINTED_SE:
            group, status, supplier = '3D-Druck intern', 'Fertigung noch offen', 'RBS'
            material = 'PETG; SCHUTZWERK-Original liegt in printed_parts (hardware/cad)'
            note = 'Druckteil laut SCHUTZWERK-Solid-Edge-Ordner printed_parts (Entscheidung Luis 26.10.2026, vorher Werkstattplatte). Geometrie aus hardware/cad bzw. STEP.'
        if key in ids(7,8):
            group, status, supplier = 'Kaufteile', 'bestellfähig', 'PLATTENZUSCHNITT24'
            material='Acrylglas/PMMA XT 5 mm klar (Entscheidung Luis 18.10.2026)'
            note='Fusion-Messung: Rechteckplatte '+('660×135,5' if key=='CAD-007' else '656×182,5')+'×5 mm ohne Bohrungen. Zuschnitt bei plattenzuschnitt24 (C10000-AC05); Befestigungslöcher beim Aufbau bohren (SYS-059/060).'
        if key=='CAD-024':
            group, status, supplier = '3D-Druck intern', 'Fertigung noch offen', 'RBS'
            material = 'PETG (Entscheidung Luis 17.10.2026); Original Blech 3 mm'
            note = 'Kabelabdeckung 22×58×3 mm mit 16 Bohrungen Ø4, als PETG-Druckteil statt Blech.'
        if key=='CAD-109':
            group, status, supplier = '3D-Druck intern', 'Fertigung noch offen', 'RBS'
            material = 'PETG (Entscheidung Luis 17.10.2026)'
        if key in ids(119,120):
            group, status, supplier = '3D-Druck intern', 'Fertigung noch offen', 'RBS'
            material = 'PETG (Entscheidung Luis 17.10.2026); Original Blechteil'
            note = 'Auslöser für den optischen Z-Endschalter, keine Last. Statt Blech als PETG-Druckteil (Entscheidung 17.10.2026).'
        if key in CNC:
            group, supplier, status = 'CNC extern','XOMETRY','Fertigung noch offen'
            material, process_evidence = 'EN AW-6082 T6 vorgeschlagen', 'CNC-Fräsen vorgeschlagen; Originalverfahren nicht belegt'
            note = 'PRÜFEN: Verfahren ungeklärt. Fusion-Messung zeigt 10 mm Platten mit Stufen auf 5 mm Tiefe und 90°-Senkungen; möglicherweise Kauf-Adapterplatten oder zwei 5-mm-Laserteile statt CNC. Material, Lochtabelle und Passungen festlegen.'
        if key in STOCK:
            group, supplier, status = 'Weitere Fertigung','DOLD','Fertigung noch offen'
            material, process_evidence = 'je Teil vorgeschlagen, siehe Fertigung.md', 'Zuschnitt/Nachbearbeitung vorgeschlagen'
            note = 'Querschnitt und Länge aus CAD; Profilserie, Toleranzen, Endbearbeitung/Bohrungen festlegen.'
        if key in PCB:
            group, status = 'PCB extern','Fertigung noch offen'
            material, process_evidence = 'FR4 1,6mm vorgeschlagen; Dicke geometrisch belegt', 'PCB erforderlich; Fertigungsdaten fehlen'
        if key in UNIDENTIFIED:
            group, status = 'Ungeklärte Teile','nicht identifiziert'
        if key in EXCLUDED:
            group, status, supplier = 'Nicht benötigt','nicht benötigt','OFFEN'
            note = 'CAD-Prüfobjekt, kein Maschinenteil.' if key=='CAD-066' else 'Nur Platzhalter; reale Multiplexer-Platine (hardware/signal-multiplexer) und Bestückung unter SYS-003/023 erfasst.'
        if int(key[-3:]) in DETAIL:
            title, note, supplier = DETAIL[int(key[-3:])]
        if key in NORM:
            offer = NORM_OFFERS[key]
            material = 'Edelstahl A2 (Entscheidung 17.10.2026); Festigkeitsklasse A2-70 im Shop nicht ausgewiesen'
            if key=='CAD-028': material = 'Edelstahl A1; A2 in DIN 466 nicht gefunden'
            if key=='CAD-058': material = 'Edelstahl A4-80 statt A2; A2 in M8×1 nicht gefunden'
            supplier = offer['supplier']
            title = offer['title'] if key in ids(56,57) else title
            note = f"Norm und Maße mit CAD abgeglichen; Artikel {offer['sku']}. {offer['fit'].split(' Preisstaffel')[0]} {NORM_RESERVE}"
            if key in ids(56,57):
                note += ' CAD-Name ISO 8673 ist ein Bibliotheksfehler: ISO 8673 beginnt erst bei M8, die CAD-Maße entsprechen ISO 4032/DIN 934.'
            if key=='CAD-058':
                note += ' ISO 8673 M8×1 passt zu den M8×1-Gewinden der induktiven Sensoren. Sensoren liefern meist 2 Muttern mit; dann nur Reserve kaufen.'
        quantity = int(g['step_qty'])
        if key in NORM: quantity = with_reserve(quantity)
        if key=='CAD-063': quantity=4
        if key=='CAD-085': quantity=1
        if key in EXCLUDED: quantity=0
        if key in ids(11,12,13,14,20,23,27,51,55,85,115,63,86,93,94,103,69,76,77,78,98,49,50,52,53,54,59,60,64,65,79,80,81,84,87,95,104,113) or (key in NORM and key!='CAD-058'): status='bestellfähig'
        if key=='CAD-080': title='GleitbuchseØ10 innen / Ø19 außen / Länge29mm'
        if key=='CAD-001': title='Y-Riemenklemme (CAD-Name TR10x2 GT2 Adapter)'
        if key=='CAD-002': title='Y-Riemenklemme, Deckel'
        if key=='CAD-010':
            note='Schubladen-Dummy564×410×12mm: unklar, ob reale Platte benötigt und welches Material. Nicht stillschweigend ausschließen oder aus Stahl fertigen.'
        if group=='3D-Druck intern':
            status='Fertigung spezifiziert'
            process_evidence='3D-Druck intern, PETG, Geometrie als STL aus dem CAD (Entscheidung Luis 17.10.2026)'
        if key in MILLED:
            material='Stahl- oder Aluminiumplatte 5 mm, Werkstattentscheidung'
            process_evidence='WERKSTATT: selbst gefräst (Luis 26.10.2026); Rohteil-Modell *_raw in hardware/cad/mechanical_parts'
            note=('5 mm Motorhalteplatte 550×135 mm.' if key in ids(96,97) else '5 mm Seitenplatte des X-Wagens 55×166,5 mm.')+' Fräszeichnung aus hardware/cad (.par/.dft) ableiten.'
        if key=='CAD-070':
            note='ABWEICHUNG (Entscheidung Luis 17.10.2026): CAD-Vierkantrohr 11,5×11,5×1,5×205 mm (Fusion-Messung) wird durch Alu-Vierkantrohr 12×12×1 mm ersetzt (keine Last; 12×12×1,5 in DE/EU nicht gefunden); gedruckte Schieber CAD-067 auf 12 mm anpassen. Bezugsquelle z. B. eBay metalexpres (AlMgSi0,5, ab 500 mm), Preis und Lager noch prüfen.'
            material='Aluminium-Vierkantrohr 12×12×1 (AlMgSi0,5)'
        if key in ids(93,94):
            material='Stahl Ø8 h6, magnetisch (Cf53), kein Edelstahl A2'
            note='Fusion-Messung: Rundstab Ø8 × '+('125' if key=='CAD-093' else '75')+' mm; Auslöser für die induktiven Sensoren, daher magnetischer Stahl. Zuschnitt kaufen (Luis 17.10.2026); Anbieter mit Preis noch offen (z. B. Motedis Cf53 h6).'
            note='Halterplatte der Übersichtskamera, 104×56,6×5 mm, 4 Bohrungen Ø5,5. Zeichnung aus CAD ableiten.'
        if key=='CAD-108':
            note='Fusion-Messung: massiver Rundstab Ø4×70 mm, Fasen an beiden Enden, ohne Gewinde. Werkstatt: aus Ø4-h6-Silberstahl (1.2210) ablängen und anfasen (Entscheidung Luis 17.10.2026).'
            material='Silberstahl 1.2210 Ø4 h6'; status='Fertigung spezifiziert'; process_evidence='WERKSTATT: Ablängen und Anfasen'
        if key=='CAD-009':
            status='teilweise geklärt'; material='Aluminium, DOLD I-Typ Nut 8'
            note='Fusion-Messung: Alu-Flachprofil 16×80×650 mm (932 mm², 2 Kerne Ø5) mit 18 M3-Gewinden. Kandidat DOLD 80x16S I-Typ Nut 8 (60886-Z), gleiche Serie wie CAD-103, aber 813 mm² und laut Produktseite M8-Kern. Kerngröße an der DOLD-Zeichnung prüfen; M3-Gewinde in der Werkstatt.'
        if key=='CAD-103':
            material='Aluminium, DOLD 40x16S I-Typ Nut 8'
            note='DOLD 40x16S I-Typ Nut 8 schwer (60879-Z) im Zuschnitt: 1,178 kg/m ≈ 436 mm² (CAD 446 mm²), Kern Ø5 für M6 = CAD. M6-Gewinde in die Stirnseiten selbst schneiden.'
        if key=='CAD-003':
            material='Aluminium 3 mm (Entscheidung 17.10.2026), z. B. EN AW-5754'
            process_evidence='WERKSTATT: eigene Fertigung aus Blech oder Aluminium (Entscheidung Luis 17.10.2026)'
            note='650×270×3 mm, 54 Bohrungen Ø3,4, 10 Bohrungen Ø4,5, 1 Bohrung Ø8. 6 Ø4,5-Bohrungen sitzen auf den langen Profilen (M4 + Nutenstein, siehe M01). Zuschnitt und Bohrungen intern; Zeichnung aus CAD ableiten.'
        if key in ids(96,97):
            process_evidence='WERKSTATT: selbst gefräst (Luis 26.10.2026); Rohteil-Modell *_raw in hardware/cad/mechanical_parts; Original lasergeschnitten (Blog)'
            material='Stahl- oder Aluminiumplatte 5 mm, Werkstattentscheidung'
            note='5 mm Stahl, 550×135 mm. Fusion-Messung: 16 Kernlöcher Ø2,46 für M3-Gewinde (Riemenspanner), Senkungen für M6 und Ø22-Durchbrüche für die Motoren. Kontur und Bohrungen aus CAD; Gewinde und Senkungen intern. Zeichnung mit Lagetoleranzen der Führungsbohrungen fehlt.'
        if key=='CAD-014':
            note='Querschnitt und Länge aus CAD (2×650 mm). Beide Stirnseiten je 2× M6-Gewinde in die Kernbohrungen Ø5 (15/45 mm) für die Senkschrauben M6×20 der Motorplatten, ≥ 16 mm tief, intern schneiden (Entscheidung Luis 18.10.2026).'
        if key=='CAD-020':
            note='Querschnitt und Länge aus CAD (4×350 mm). Unten M6-Gewinde in die Kernbohrung Ø5 für die Gelenkfüße, intern schneiden (Entscheidung 17.10.2026). Profilserie siehe M01.'
        if key=='CAD-109':
            note='Fusion-Messung: Hülse Ø3/Ø4,8 × 3 mm (Name sagt 2 mm). Als PETG-Druckteil (Entscheidung Luis 17.10.2026); kein passender Kaufartikel gefunden.'
        if key in ids(107,110,111,112,116,117):
            process_evidence='3D-Druck belegt (Thesis PDF-Seite67); Druckparameter/Werkstoff vorgeschlagen'
        result.append(dict(id=key,name=title,cad_name=name,cad_quantity=g['step_qty'],fusion_quantity=g['fusion_qty'],
                           quantity=quantity,unit='Stück',group=group,status=status,geometry_mm=g['local_aabb_mm'],
                           solid_volume_cm3=g['solid_volume_cm3'],material=material,process_evidence=process_evidence,
                           supplier=supplier,issue=note,source=CAD+'; '+BLOG,cost_id=''))
    for key,title,qty,unit,group,supplier,note,source in SYSTEM:
        status='teilweise geklärt'
        if group in ['PCB extern','3D-Druck intern','Weitere Fertigung']: status='Fertigung noch offen'
        if group=='Ungeklärte Teile': status='nicht identifiziert'
        if group=='Nicht benötigt': status='nicht benötigt'
        if key in ('005','006','037','039','040'): status='Fertigung spezifiziert'
        if key in ('007','008','016','027','028','057','059','060','042','043','044','045','046','047','048','049','050','051','052','053','054','055','056'): status='bestellfähig'
        result.append(dict(id='SYS-'+key,name=title,cad_name='',cad_quantity='',fusion_quantity='',quantity=qty,
                           unit=unit,group=group,status=status,geometry_mm='',solid_volume_cm3='',
                           material='nicht belegt',process_evidence='Planungsbedarf; '+source,
                           supplier=supplier,issue=note,source=source,cost_id=''))
    for p in result:
        for k in ['name','material','process_evidence','issue']:
            if not p[k].startswith('http'): p[k]=prose(p[k])
    return result

def make_orders(parts):
    offers = {o['id']:o for o in json.loads((BOM/'data/offers.json').read_text(encoding='utf-8'))}
    byid = {p['id']:p for p in parts}
    orders=[]
    cad_offers={o['cad']:o['id'] for o in offers.values() if o.get('cad')}
    def add(key, title, part_ids, need, unit='Stück', offer=None, estimate=None, pack=1,
            supplier=None, note='', optional=False, source=None, basis='gross', spec=''):
        assert all(i in byid for i in part_ids),part_ids
        o=offers.get(offer,{})
        sup=supplier or o.get('supplier') or byid[part_ids[0]]['supplier']
        price=o.get('price') if offer and o.get('price') is not None else estimate
        price_basis=o.get('basis',basis)
        size=o.get('pack',pack)
        packs=pack_count(need,size)
        q=None if packs is None else D(str(size))*packs
        if price is None or packs is None:
            net=gross=None
        else:
            value=D(str(price))*packs
            gross=money(value if price_basis=='gross' else value*(1+VAT))
            net=money(value/(1+VAT) if price_basis=='gross' else value)
        row=dict(id=key,title=title,part_ids=';'.join(part_ids),need=need,unit=unit,pack_size=size,
                 order_packs=packs,order_quantity=q,price_per_pack=price,price_basis=price_basis,
                 currency='EUR',vat_percent=19,net_eur=net,gross_eur=gross,
                 price_kind='Webpreis' if offer and o.get('price') is not None else ('Schätzung' if estimate is not None else 'offen'),
                 optional=optional,supplier=sup,manufacturer=o.get('manufacturer','nicht festgelegt'),
                 sku=o.get('sku','offen'),mpn=o.get('mpn','offen'),date=DATE,
                 stock=o.get('stock','nicht bestätigt; Angebot/Checkout erforderlich'),
                 url=o.get('url') or source or SUPPLIER_URL[sup],
                 specification=spec or o.get('fit') or '; '.join(byid[i]['issue'] for i in part_ids),
                 note=note)
        orders.append(row)
        if not optional:
            for i in part_ids:
                assert not byid[i]['cost_id'],f'Double counted {i}'
                byid[i]['cost_id']=key
        return row

    add('BUY-001','Netzteil24V',ids(60),1,offer='O-001')
    add('BUY-002','16TMC2130 aus4Viererpacks',['SYS-001'],16,offer='O-002')
    add('BUY-003','16FlanschhalterSHF10',ids(79),16,offer='O-003')
    add('BUY-004','12X/Y-Antriebsriemenscheiben',ids(77),12,offer='O-004')
    add('BUY-005','20 Umlenkrollen 6 mm, 8,5 mm breit',ids(78),20,offer='O-063')
    add('BUY-006','8 Z-Zahnscheiben 9 mm, Ersatz mit Halteranpassung',ids(76),8,offer='O-006')
    add('BUY-007','X/Y-Riemen6mm,2Rollen à10m',ids(87,104),20,unit='m',offer='O-007',note='Zuschnitt aus Fusion-Messung: 8×1,51 m + 4×1,10 m = 16,5 m inklusive Klemmzugabe; zwei 10-m-Rollen decken den Bedarf.')
    add('BUY-008','Kurze Energieketten, 192 Glieder',ids(49),192,unit='Glied',offer='O-008',note='16 Abschnitte à 12 Glieder (0,24 m).')
    add('BUY-009','4optischeEndstops inkl1mKabel',ids(65),4,offer='O-009')
    printed=[p for p in parts if p['group']=='3D-Druck intern']
    solid=sum(D(p['solid_volume_cm3'])*D(str(p['quantity'])) for p in printed if p['solid_volume_cm3'])
    kg=solid*D('1.27')*D('1.20')/1000 + D('1')
    add('MAT-001','PETG fürCAD-Druckteile plusKalibrierkörper',[p['id'] for p in printed],kg,unit='kg',offer='O-010',note=f'{solid:.3f}cm³ CAD-Vollvolumen × angenommene1,27g/cm³ ×1,20 +1kg Kalibrier-/Probedruckbudget. Auf ganze1kg-Rollen gerundet. Kein Slicerresultat.')
    add('BUY-010','Übersichtskamera ELP-USBFHD01M-H100',['SYS-002'],1,offer='O-088',estimate=None)
    add('BUY-011','USB-Mikroskop Toolcraft 2 MP (AUSWAHL, ANPASSUNG Halter)',ids(85),1,offer='O-087')
    add('BUY-012','Aktiver7Port-USB-Hub',['SYS-010'],1,offer='O-013')
    add('BUY-013','LED-Streifen 5-m-Rolle für 1,9 m',['SYS-007'],D('1.9'),unit='m',offer='O-014')
    add('ALT-001','MR12MLVergleich, keine bestätigteCPC-Paarung',ids(27),8,offer='O-015',optional=True)
    add('ALT-002','MGN12CNachbauvergleich, keinHIWIN',ids(54),4,offer='O-016',optional=True)
    add('OPT-001','3zusätzlicheMikroskope',['SYS-033'],3,offer='O-012',optional=True,note='Nur Kamerapreis; zusätzliche Kabel, Halteränderung und USB-Topologie nicht kalkuliert.')

    # Own rough budget assumptions; not supplier quotations or promises of fit.
    add('BUY-014','12 NEMA17 Originalmotoren',ids(64),12,offer='O-041')
    add('BUY-015','4 NEMA14 Z-Motoren, ERSATZ STEPPERONLINE 14HS13-0804S',ids(63),4,offer='O-065',estimate='8',basis='net',note='Shoppreis 8,48 USD, als 8 EUR netto geschätzt; EUR-Preis und Versandlager im Checkout prüfen.')
    add('BUY-016','4 Steuerplatinen SKR 1.4 Turbo (ERSATZ)',ids(23),4,offer='O-043',note='Firmware-Migration auf SKR 1.4 Turbo nötig (Arbeitszeit nicht kalkuliert).')
    add('BUY-018','8 CPC-Führungswagen MR12ML',ids(27),8,offer='O-045')
    add('BUY-019','2 CPC-Schienen MR12M 600 mm',ids(95),2,offer='O-046')
    add('BUY-020','4 HIWIN-Schienen 150 mm',ids(53),4,offer='O-047')
    add('BUY-021','4 HIWIN-Wagen MGN12C',ids(54),4,offer='O-048')
    add('BUY-022','16 Gleitbuchsen RJ4JP-01-10',ids(80),16,offer='O-052')
    add('BUY-023','Lange Energieketten, 112 Glieder',ids(50),112,unit='Glied',offer='O-049',note='8 Abschnitte à 14 Glieder (0,28 m).')
    add('BUY-024','16 Anschlusssätze E2.10 schmal',['SYS-027'],16,unit='Satz',offer='O-050')
    add('BUY-025','8 Anschlusssätze E2.10 breit',['SYS-028'],8,unit='Satz',offer='O-051')
    add('BUY-017','Z-Riemen 9 mm',ids(113),D('1.28'),unit='m',offer='O-044',note='Zuschnitt aus Fusion-Messung 4×0,32 m.')
    add('BUY-SYS-057','10 Prüfstifte P75-E2',['SYS-057'],10,offer=cad_offers['SYS-057'])
    for key in ['SYS-0'+str(k) for k in list(range(42,57))+[59,60]]:
        add('BUY-'+key,byid[key]['name'],[key],byid[key]['quantity'],offer=cad_offers[key])
    add('MAT-007','Aluprofil 40x16S Nut 8, Zuschnitt',ids(103),1,unit='Los',offer=cad_offers['CAD-103'])
    add('MAT-008','Aluprofil 80x16S Nut 8, Zuschnitt, Kandidat',ids(9),1,unit='Los',offer=cad_offers['CAD-009'])
    add('MAT-009','Auslöserstäbe Ø8 Cf53, Zuschnitt',ids(93,94),1,unit='Los',offer=cad_offers['CAD-093'])
    add('BUY-SEN','24 induktive Sensoren ELCO NI4-M08-ON6L-Q8',ids(55),24,offer=cad_offers['CAD-055'])
    add('BUY-SW','Netzschalter Ø19 ONPOW LAS1A',ids(86),1,offer=cad_offers['CAD-086'])
    add('BUY-CAB','24 Sensorleitungen ifm EVC141',['SYS-016'],24,offer=cad_offers['SYS-016'])
    add('BUY-PIN','Prüfstifte P75-B1 (CAD-Spitze)',ids(115),10,offer=cad_offers['CAD-115'])
    add('MAT-010','Acrylglas-Abdeckungen, Zuschnitt-Los',ids(7,8),1,unit='Los',offer=cad_offers['CAD-007'],estimate='31',note='Schätzung ca. 74 EUR/m² × 0,418 m² (zwischen 4- und 6-mm-Preis); exakter Preis im Konfigurator.')
    add('BUY-LEDP','LED-Profilsatz BARdolino',['SYS-008'],1,unit='Satz',offer=cad_offers['SYS-008'])
    for n in (51,52,59,81,84):
        p=byid[f'CAD-{n:03}']
        add(f'BUY-C{n:03}',p['name'],[p['id']],p['quantity'],offer=cad_offers[p['id']])
    for key in NORM:
        p=byid[key]
        add('N-'+key[-3:],p['name'],[key],p['quantity'],offer=cad_offers[key],
            note='Nur kaufen, wenn die Sensoren keine Muttern mitbringen.' if key=='CAD-058' else '')
    profiles=ids(11,12,13,20)
    add('MAT-002','30×30 Nut 6 Aluprofil, Zuschnitt-Los',profiles,1,unit='Los',offer='O-058')
    add('MAT-003','60×30 Nut 6 Aluprofil schwer, Zuschnitt',ids(14),1,unit='Los',offer='O-059')
    add('MAT-004','Präzisionswellen Ø10, Zuschnitt-Los',ids(69,98),1,unit='Los',offer='O-064')
    add('MAT-005','Versteifungsprofile40×16 undHalte-/Distanzstäbe',ids(70,108),1,unit='Los',estimate='100',note='Eigenes100EUR-Bruttobudget fürProfile4×436mm, Rechteck2×205mm, Ø8Trigger4×125+4×75mm, Ø4Stäbe8×70mm und4Distanzteile. Material/Profile noch klären.')
    add('MAT-006','Blechrohmaterial undVerschnitt',[p['id'] for p in parts if p['group']=='Blech intern'],1,unit='Los',estimate='200',note='Eigener200EUR-Bruttobudgettopf für3/5mmPlatten und noch nicht abgewickelteTeile. Kein Händlerangebot; Material/Flachzuschnitte noch nicht bestellfähig. InterneArbeits-/Maschinenzeit ausgeschlossen.')
    for key,amount in [('011','20'),('012','15'),('013','15'),('014','64'),('015','25'),('018','60'),('020','35'),('021','15'),('022','60'),('025','20'),('029','35'),('030','20'),('031','35'),('032','30')]:
        p=byid['SYS-'+key]
        add('BUD-S'+key,p['name'],[p['id']],1,unit='Los',estimate=amount,note='Eigener Gesamt-Budgetansatz fürden inTeileliste genanntenBedarf; kein konkretesArtikelangebot. Beipack undvorhandeneBestände abziehen.')
    # All remaining required rows remain explicit and unpriced, never implicit zeroes.
    for p in parts:
        if not p['cost_id'] and p['status']!='nicht benötigt' and p['group']!='Optional':
            add('OPEN-'+p['id'],p['name'],[p['id']],p['quantity'],unit=p['unit'],note='Preis und/oderBestellvariante offen. Nicht im numerischenZwischentotal enthalten.')
    # Shipping is a separate cost owner; no fabricated zero freight.
    add('SHIP-RBS','RBS SammelversandDeutschland',[],1,unit='Sendung',estimate=None,supplier='RBS',source='https://www.roboter-bausatz.de/c/information/versand-und-zahlung/',note='Kostenlos ab99EUR brutto; geplanterRBS-Warenkorb liegt darüber.')
    orders[-1].update(price_kind='Webpreis',price_per_pack='0.00',net_eur=D('0.00'),gross_eur=D('0.00'))
    add('SHIP-REICHELT','Reichelt DHL Deutschland bis10kg',[],1,unit='Sendung',estimate=None,supplier='REICHELT',source='https://www.reichelt.de/versandkosten',note='ÖffentlicherDHL-Tarif bis10kg:5,95EURbrutto. Gewichtunter10kg fürgeplanteElektronik angenommen; endgültigenWarenkorb prüfen.')
    orders[-1].update(price_kind='Webpreis',price_per_pack='5.95',net_eur=D('5.00'),gross_eur=D('5.95'))
    add('FEE-001','RechnungskaufgebührSchrauben.Expert',[],1,unit='Gebühr',estimate='5',supplier='SCHRAUBEN',source='https://schrauben-expert.de/Zahlungsmoeglichkeiten',note='Öffentlich5EUR; bruttoangenommen,SteuerbasisimCheckoutprüfen. Ab3.qualifizierterBestellung entfallend.')
    add('SHIP-EISEN2000','Eisenwaren2000 Versand Deutschland',[],1,unit='Sendung',estimate=None,supplier='EISEN2000',source='https://www.eisenwaren2000.de/',note='Versandkostenfrei ab 59 EUR; geplanter Normteile-Warenkorb ca. 92 EUR.')
    orders[-1].update(price_kind='Webpreis',price_per_pack='0.00',net_eur=D('0.00'),gross_eur=D('0.00'))
    add('SHIP-BEFFUCHS','Befestigungsfuchs Versand Deutschland',[],1,unit='Sendung',estimate='5.95',supplier='BEFFUCHS',source='https://www.befestigungsfuchs.de/',note='5,95 EUR laut Shop; nur nötig, falls M8×1-Muttern bestellt werden.')
    add('SHIP-SCHRAUBEN','Schrauben.Expert Versand Deutschland',[],1,unit='Sendung',estimate='4',supplier='SCHRAUBEN',source='https://schrauben-expert.de/',note='Versand nach Gewicht; Produktfeed nennt 4 EUR, Warenkorb ca. 54 EUR liegt unter der 100-EUR-Freigrenze.')
    add('SHIP-REST','Frachtreserve fürübrigeLieferanten',[],1,unit='Budget',estimate='150',supplier='OFFEN',note='Eigene150EUR-Bruttoreserve fürDOLD/TME/Normteile/Motoren/Führungen/CNC/PCB. Tatsächliche Fracht jeAnbieter offen; kein bestätigterVersandpreis. Reichelt/RBS separat.')
    for o in orders:
        for k in ['title','note','specification']:
            o[k]=prose(o[k])
    return orders

COMPONENT_CSV = 'evidence/component-inventory.csv'
FUSION = 'evidence/fusion-inventory.json'
COMPONENT_TITLE = {
    'base': 'Grundgestell mit X-Antrieben, Platinen- und Kamerahalter',
    'x_slide': 'X-Wagen einer Prüfeinheit',
    'y_slide': 'Y-Schlitten',
    'y_slide_mirrored': 'Y-Schlitten, gespiegelt',
    'z_slide': 'Z-Achse',
    'z_slide_long': 'Z-Achse, lange Ausführung',
}
COMPONENT_ORDER = ['base','x_slide','y_slide','y_slide_mirrored','z_slide','z_slide_long']
NOT_IN_CAD = 'K14 Nicht im CAD-Modell'

def fusion_name(path):
    return re.sub(r'( \(\d+\))?:\d+$','',path).lower()

def make_components(parts):
    """One row per (top-level component, direct subassembly, part); SYS parts form K14.

    STEP placements are matched to Fusion's top-level paths by definition name
    and order, so the third x_slide in STEP becomes Fusion's x_slide:3.
    """
    with (BOM/COMPONENT_CSV).open(encoding='utf-8-sig') as f:
        step=list(csv.DictReader(f))
    occurrences=json.loads((BOM/FUSION).read_text(encoding='utf-8'))['occurrences']
    fusion_tops=[o['path'] for o in occurrences if '+' not in o['path']]
    fusion_leaves=Counter((o['path'].split('+')[0],o['name']) for o in occurrences if o['children']==0)
    by_name={}
    for path in fusion_tops: by_name.setdefault(fusion_name(path),[]).append(path)
    placement={}
    for r in step:
        if r['component_index'] not in placement:
            name=r['component'].lower()
            placement[r['component_index']]=by_name[name][sum(fusion_name(v)==name for v in placement.values())]
    assert sorted(placement.values())==sorted(fusion_tops)
    tops=sorted(fusion_tops,key=lambda t:(COMPONENT_ORDER.index(fusion_name(t)),t))
    number={t:f'K{i:02}' for i,t in enumerate(tops,1)}
    byname={p['cad_name']:p for p in parts if p['cad_name']}
    step_leaves=Counter()
    for r in step: step_leaves[(placement[r['component_index']],r['cad_name'])]+=int(r['quantity'])
    rows=[]
    for r in step:
        top=placement[r['component_index']];part=byname[r['cad_name']]
        complete=fusion_leaves[(top,part['cad_name'])]==step_leaves[(top,part['cad_name'])]
        rows.append(dict(component=f'{number[top]} {top}',fusion_path=top,title=COMPONENT_TITLE[fusion_name(top)],
                         subassembly=r['subassembly'],id=part['id'],name=part['name'],cad_name=part['cad_name'],
                         quantity=int(r['quantity']),unit='Stück',in_fusion='ja' if complete else 'fehlt im Fusion-Import',
                         group=part['group'],status=part['status']))
    for part in parts:
        if not part['cad_name']:
            rows.append(dict(component=NOT_IN_CAD,fusion_path='',title='Systemteile ohne CAD-Körper',subassembly='',
                             id=part['id'],name=part['name'],cad_name='',quantity=part['quantity'],unit=part['unit'],
                             in_fusion='nein',group=part['group'],status=part['status']))
    rows.sort(key=lambda r:(r['component'],r['subassembly'],r['id']))
    return rows

def write_csv(path,rows):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def euro(v):
    return 'offen' if v is None else f'{v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')+' €'

def qty(v):
    if v is None or v=='': return 'offen'
    return format(D(str(v)).quantize(D('.001')).normalize(),'f').replace('.',',')

def table(headers,rows):
    def cell(x):
        # Preserve exact URLs and code tokens while formatting ordinary text.
        tokens=re.split(r'(https?://[^\s)]+|`[^`]+`)',str(x))
        value=''.join(t if t.startswith(('http','`')) else prose(t) for t in tokens)
        return value.replace('|','/').replace('\n',' ')
    return '\n'.join(['| '+' | '.join(cell(h) for h in headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+['| '+' | '.join(cell(v) for v in r)+' |' for r in rows])+'\n'

def component_sections(parts,components):
    byid={p['id']:p for p in parts}
    names=sorted({r['component'] for r in components})
    anchor=lambda n:'komp-'+n.split()[0][1:]
    text='# Teile nach Komponente\n\n'
    text+='Die 13 übergeordneten Komponenten sind die obersten Einbauten im Fusion-Modell; K14 sammelt die Teile ohne CAD-Körper. Teile aus Unterbaugruppen bleiben bei ihrer Komponente, die Unterbaugruppe steht in der zweiten Spalte. Die Stückzahlen sind STEP-Mengen je Komponente; die Planmenge gilt für die ganze Maschine und steht in den Details. [CSV je Komponente](teileliste-komponenten.csv)\n\n'
    text+=table(['Komponente','Inhalt','Positionen','Stück laut CAD'],[
        [f'[{n}](#{anchor(n)})',[r for r in components if r['component']==n][0]['title'],
         len({r['id'] for r in components if r['component']==n}),
         sum(r['quantity'] for r in components if r['component']==n) if n!=NOT_IN_CAD else '–'] for n in names])+'\n'
    def note(r):
        p=byid[r['id']];extra=[r['status']]
        if str(p['quantity'])!=str(p['cad_quantity']): extra.append(f"Plan gesamt {qty(p['quantity'])} statt {p['cad_quantity']}")
        if r['in_fusion']!='ja': extra.append(r['in_fusion'])
        return '; '.join(extra)
    for n in names:
        rows=[r for r in components if r['component']==n]
        text+=f'<a id="{anchor(n)}"></a>\n\n## {n} – {rows[0]["title"]}\n\n'
        if n==NOT_IN_CAD:
            text+=table(['ID / Teil','Planmenge','Beschaffungsart','Status'],[
                [f"[{r['id']}](#{r['id'].lower()}) {r['name']}",f"{qty(r['quantity'])} {r['unit']}",r['group'],r['status']] for r in rows])+'\n'
        else:
            text+=table(['ID / Teil','Unterbaugruppe','CAD-Name','Stück','Status'],[
                [f"[{r['id']}](#{r['id'].lower()}) {r['name']}",f"`{r['subassembly']}`" if r['subassembly'] else 'direkt',
                 f"`{r['cad_name']}`",r['quantity'],note(r)] for r in rows])+'\n'
    return text

def render(parts,orders,components):
    required=[o for o in orders if not o['optional']]
    web=[o for o in required if o['price_kind']=='Webpreis']
    estimates=[o for o in required if o['price_kind']=='Schätzung']
    missing=[o for o in required if o['gross_eur'] is None]
    sums=lambda rows,key:sum((r[key] for r in rows if r[key] is not None),D(0))
    totals={k:{'net':str(sums(v,'net_eur')),'gross':str(sums(v,'gross_eur'))} for k,v in [('web',web),('estimates',estimates),('provisional',web+estimates)]}
    totals.update(date=DATE,parts=len(parts),cad_positions=sum(p['id'].startswith('CAD-') for p in parts),unpriced=[o['id'] for o in missing],status_counts=dict(Counter(p['status'] for p in parts)))
    (BOM/'kosten.json').write_text(json.dumps(totals,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    intro='# Teileliste für einen PROBoter mit vier Prüfeinheiten\n\nStand16.10.2026. **Planungsstückliste mit expliziten Lücken, keine bestätigte Original-BOM.**\n\nCAD/Fusion-Mengen bleiben unverändert; die Planmenge ist eine getrennte Entscheidung. Alle Maße in mm. `CAD-xxx` sind stabile IDs dieses Inventurstandes; `SYS-xxx` ergänzen Systembedarf. Änderungen von IDs nur mit Migration. [Bestellübersicht](Bestellliste.md) · [Fertigung](Fertigung.md) · [CSV](teileliste.csv) · [CAD-Beweise](CAD-Pruefung.md).\n\n'
    intro+='**Status:** bestellfähig = Modell und Bezugsquelle eindeutig (Liefertermin trotzdem prüfen); teilweise geklärt = Familie bekannt, mindestens eine Passungs-/Mengenfrage offen; Fertigung spezifiziert = Material, Zeichnung und Verfahren freigegeben; Fertigung noch offen = mindestens eine dieser Angaben fehlt; nicht identifiziert = erforderliche genaueIdentität unbekannt; nicht benötigt = begründeter Ausschluss. Aktuell erreicht kein Sonderteil den Status Fertigung spezifiziert.\n\n'
    intro+=component_sections(parts,components)
    intro+='# Details nach Beschaffungsart\n\n'
    groups=['Kaufteile','3D-Druck intern','Blech intern','CNC extern','Weitere Fertigung','PCB extern','Ungeklärte Teile','Optional','Nicht benötigt']
    for group in groups:
        subset=[p for p in parts if p['group']==group]
        intro+=f'## {group}\n\n'
        intro+=table(['ID / Teil','CAD / Fusion / Plan','Status','Geometrie / Werkstoff','Quelle und konkreterKlärbedarf'],[
            [f"<a id=\"{p['id'].lower()}\"></a>**{p['id']}** {p['name']}"+(f"<br>`{p['cad_name']}`" if p['cad_name'] else ''),
             f"{p['cad_quantity'] or '–'} / {p['fusion_quantity'] or '–'} / **{qty(p['quantity'])} {p['unit']}**",
             p['status'],(p['geometry_mm'] or 'offen')+'; '+p['material'],
             p['issue']+f"<br>[Beleg]({p['source'].split('; ')[0]}); Kostenzeile `{p['cost_id'] or 'ausgeschlossen/optional'}`"] for p in subset])+'\n'
    (BOM/'Teileliste.md').write_text(intro.rstrip()+'\n',encoding='utf-8')

    ordertext='# Bestellliste und Einstieg\n\n**Stand16.10.2026 · ein PROBoter / vier Prüfeinheiten · Bildungseinrichtung Deutschland.**\n\n'
    ordertext+='3D-Druck und Blechbearbeitung intern; CNC/PCB extern. Host-PC, Messgeräte und Werkzeuge vorhanden. Arbeitszeit, Maschinenkosten, Softwaremigration und Elektronikentwicklung sind ausgeschlossen. Die Grundkonfiguration enthält **ein bewegliches Mikroskop und eine Übersichtskamera**, dreiweitereMikroskope sind optional.\n\n'
    ordertext+='## Kostenstand\n\n'
    ordertext+=table(['Ergebnis','netto','brutto19%'],[
        ['1. Summe belegterWebpreise beiPlanmengen (einschließlichungeprüfterKandidaten)',euro(sums(web,'net_eur')),euro(sums(web,'gross_eur'))],
        ['Zusätzliche eigeneBudgetschätzungen inklusiveFrachtreserve',euro(sums(estimates,'net_eur')),euro(sums(estimates,'gross_eur'))],
        ['2. VorläufigerGesamtbedarf desbeziffertenUmfangs',euro(sums(web+estimates,'net_eur')),euro(sums(web+estimates,'gross_eur'))],
        [f'3. {len(missing)} nochunbezifferteBestellpositionen','offen','offen']])
    ordertext+='\n**Das vorläufigeTotal ist kein vollständiger Baupreis.** Die unbezifferten Platinen, Prüfkontakte, Sensoren und Kalibrierteile kommen hinzu. Ein vorhandenerShoppreis beweistkeineAustauschbarkeit. [Kostenmethodik](Kosten.md) trennt Preise, Mengenannahmen und offeneBedarfe.\n\n'
    ordertext+='## Dokumente\n\n- [AlleTeile undMengen](Teileliste.md) / [CSV](teileliste.csv)\n- [Fertigung nachVerfahren undAngebotsanforderungen](Fertigung.md)\n- [NichtidentifizierteTeile undübrigeLücken](Ungeklaert.md)\n- [Lieferanten, Rechnungskauf undVersand](Lieferanten.md)\n- [Bestell-CSV mitPackungsrechnung](bestellliste.csv), [Kosten-JSON](kosten.json), [Angebotsquellen](data/offers.json)\n- [CAD-/Fusion-Abgleich](CAD-Pruefung.md), [Reproduktion](Reproduktion.md)\n\n'
    ordertext+='## Bereits eindeutig beschaffbar\n\n- **CAD-060:1×MeanWellRSP-200-24** – Originalmodell; Netzanschluss/Verteilung separat planen.\n- **CAD-079:16×SHF10,DOLD11260** – Hauptmaße bestätigt; aktuell angekündigterWareneingang27.11.2026.\n\nTMC2130, Rollen, Lager undKamerakandidaten besitzenkonkreteBezugsquellen, benötigenaber diejeweilsgenanntePassungsprüfung. FilamentistalsMaterialvorschlagpreislichbestimmt; Druckteile sindnochkeinefreigegebenenFertigungsaufträge.\n\n'
    for kind,heading in [('Webpreis','Shopartikel mitbeobachtetemPreis'),('Schätzung','VorläufigeBudgetansätze – keineShopangebote'),('offen','NochunbezifferteBestellpositionen')]:
        subset=[o for o in required if o['price_kind']==kind]
        ordertext+=f'## {heading}\n\n'
        ordertext+=table(['ID / Bedarf','Bedarf → Bestellung','Anbieter / Artikel','Preis proPackung','Summe netto / brutto','Passung / Vorbehalt'],[
            [f"**{o['id']}** {o['title']}<br>{o['part_ids']}",f"{qty(o['need'])} {o['unit']} → {qty(o['order_packs'])} × {qty(o['pack_size'])}",
             (f"[{o['supplier']}]({o['url']}) / {o['sku']}"+
              (f"<br>{o['manufacturer']}: {o['mpn']}<br>{o['stock']}" if o['price_kind']=='Webpreis' else '')) if o['url'] else 'noch festzulegen',
             (euro(D(str(o['price_per_pack'])))+' '+{'gross':'brutto','net':'netto'}[o['price_basis']]) if o['price_per_pack'] is not None else 'offen',
             euro(o['net_eur'])+' / '+euro(o['gross_eur']),o['specification']+' '+o['note']] for o in subset])+'\n'
    ordertext+='## Optionen undVergleiche – nicht imGrundtotal\n\n'
    ordertext+=table(['ID','Artikel / Quelle','Menge','brutto','Einschränkung'],[[o['id'],f"[{o['title']}]({o['url']})",qty(o['order_quantity']),euro(o['gross_eur']),o['specification']+' '+o['note']] for o in orders if o['optional']])
    ordertext+='\nLieferstatus, Hersteller/MPN undPreisdatum stehen vollständig in der [Bestell-CSV](bestellliste.csv) und [Angebotsdatei](data/offers.json). Sämtliche Webpreise sind EUR; Versand proLieferant siehe [Lieferanten](Lieferanten.md). Es wurden keineBestellungen ausgelöst.\n'
    # Only normalize headings/plain paragraphs here: product URLs and IDs are untouched.
    ordertext='\n'.join(prose(line) if not ('http' in line or line.startswith('|')) else line for line in ordertext.split('\n'))
    (BOM/'Bestellliste.md').write_text(ordertext,encoding='utf-8')

    unknown='# OffeneTeile undKlärungsbedarf\n\nDie Liste enthältjedeoffenePosition, auchteilweisebekannteStandardteile. EineunbekannteSchaltung lässtsichnichtaus eineräußerenSTEP-Hülle rekonstruieren.\n\n'
    for status in ['nicht identifiziert','Fertigung noch offen','teilweise geklärt']:
        unknown+=f'## {status}\n\n'+table(['ID / Teil','Bedarf','NächsterkonkreterSchritt'],[[p['id']+' '+p['name'],qty(p['quantity'])+' '+p['unit'],p['issue']] for p in parts if p['status']==status and p['group']!='Optional'])+'\n'
    unknown+='## Reihenfolge zumSchließen derLücken\n\n1. Originalschaltpläne/BOM/Gerber fürMultiplexer, Prüfspitzen undZielversorgung beschaffen oderNeu-Entwicklungfestlegen; darausSensorinterface, GegensteckerundKabel ableiten.\n2. NEMA14-Alternativlagen prüfen; einevierachsigeProbe mechanisch/elektrischverifizieren. SKR1.3-Verfügbarkeit bzw.Firmwaremigration entscheiden.\n3. Original-CPC/HIWIN-Paarungen undMotorlieferbarkeit anbietenlassen; keineMischungungeprüfterNachbauten.\n4. Mikroskopbei100mmArbeitsabstand undstatischeKamera unterLinux prüfen; Halterdanachfestlegen.\n5. FertigungszeichnungenmitWerkstoffen/Passungen erstellen; Kalibrierboardgeometrie aufeineSoftwareversionfestlegen.\n6. KabelwegeundKettenbelegung messen, Stromlaufplan abschließen, Beipack-Normteile abgleichen undWarenkörbe finalisieren.\n\nAnfragen wurdennichtversandt.\n'
    unknown='\n'.join(prose(line) if 'http' not in line else line for line in unknown.split('\n'))
    (BOM/'Ungeklaert.md').write_text(unknown,encoding='utf-8')
    fabrication(parts)
    costs(parts,orders)
    return totals

def costs(parts,orders):
    required=[o for o in orders if not o['optional']]
    ready={p['cost_id'] for p in parts if p['status']=='bestellfähig'}
    web=[o for o in required if o['price_kind']=='Webpreis']
    estimate=[o for o in required if o['price_kind']=='Schätzung']
    missing=[o for o in required if o['gross_eur'] is None]
    total=lambda rows,key:sum((o[key] for o in rows if o[key] is not None),D(0))
    text='''# Kosten und Kalkulationsgrenzen

**Preisstand16.10.2026; EUR. Ein PROBoter mit vier Prüfeinheiten.**
Öffentliche Seiten bzw. Suchindexanzeigen sind Preisbeobachtungen, keine bindenden
Angebote. Bestand und Preis können gegenüber dem Index geändert sein. Vor einer
Bestellung den Artikel, die Mengenstaffel, die Rechnungsfreigabe und das Lieferdatum
im Shop bestätigen. Kein Warenkorb wurde bestellt.

## Drei getrennte Ergebnisse

'''
    text+=table(['Umfang','netto','brutto'],[
        ['1. Beobachtete Webpreise × geplante Bestellpackungen',euro(total(web,'net_eur')),euro(total(web,'gross_eur'))],
        ['Davon Positionen mit Status bestellfähig',euro(total([o for o in web if o['id'] in ready],'net_eur')),euro(total([o for o in web if o['id'] in ready],'gross_eur'))],
        ['Davon übrige Material-/Kandidatenpreise mit offenen Prüfungen',euro(total([o for o in web if o['id'] not in ready],'net_eur')),euro(total([o for o in web if o['id'] not in ready],'gross_eur'))],
        ['Eigene Budgetschätzungen zusätzlich',euro(total(estimate,'net_eur')),euro(total(estimate,'gross_eur'))],
        ['2. Vorläufiger Gesamtbedarf des bezifferten Umfangs',euro(total(web+estimate,'net_eur')),euro(total(web+estimate,'gross_eur'))],
        [f'3. Noch unbezifferte Positionen: {len(missing)}','nicht berechenbar','nicht berechenbar']])
    text+='''
**Der Gesamtpreis eines funktionierenden Nachbaus bleibt offen.** Die Summe unter2
deckt nur bezifferte Positionen ab. Entwicklung von Elektronik/Firmware, interne
Arbeitszeit, Maschinenkosten, Host-PC, Messgeräte und Werkzeuge sind ausgeschlossen.
Einzelne Budgetansätze können nach Konstruktion stark abweichen; sie sind weder
Preisobergrenzen noch Angebote. Es wurde kein pauschaler Gewinn-/Risikozuschlag aufgeschlagen.

## Rechenregeln

- Steuerbasis:19% deutsche Umsatzsteuer als Planannahme für die Lieferung nachDE.
  Keine Vorsteuerabzugsberechtigung oder innergemeinschaftliche Steuerbefreiung unterstellt.
  Bei einem EU-Lieferanten die tatsächliche Rechnungsbehandlung prüfen.
- Bruttopreise: Zeilenbrutto = Packungen × Packungspreis; netto = brutto/1,19.
  Nettopreise: Zeilennetto = Packungen × Packungspreis; brutto = netto×1,19.
  Auf Zeilenebene kaufmännisch aufCent gerundet; Summen addieren diese Zeilen.
  Daher kann die Umrechnung der Gesamtsumme um wenigeCent abweichen.
- Packungen = aufgerundeter Bedarf/Packungsinhalt. VierTreiber jePackung,
 10m beiGT2-6mm,5m beiLED und1kg beiFilament sind dokumentiert.
  Normteil-Zehnerpackungen und Profil-Recheneinheiten sind **Planannahmen**,
  keine behaupteten Händler-Mindestmengen. Stückbedarf bleibt inTeileliste sichtbar.
- Internes Druckmaterial nach Vollvolumen und Zuschlag; Blech als eigener
  Budgettopf. CNC-Budget enthält Material bereits. Keine erneute Berechnung
  der einzelnen Druck-/Blechteile oder des CNC-Rohmaterials.
- Baugruppen nicht zusätzlich zu ihren Blattteilen kalkuliert.
  X/Y-Riemen teilen einen Kostenposten. Führungswagen undSchienen imBudget
  als abgestimmte Sätze. Multiplexer-Dummy ausgeschlossen; echtePlatine und
  Bestückung getrennt und unbeziffert.
- Enthaltene optischeEndstop-Kabel sowie Hub-Netzteil/-Kabel nicht doppelt
  kalkuliert.48M8-Sensormuttern zunächst offen, da möglicherweiseBeipack.
  Kettenendstücke sind nur ein Budget, bis der Lieferumfang geklärt ist.
- Optionen/Vergleiche `ALT-*` und `OPT-*` sind aus Grundsummen ausgeschlossen.
  Ein Nachbauwagen ist keine bestätigte Alternative für eineOriginalschiene.
- Fehlende Preise sind inCSV leereZellen und inJSON/Code null/None, niemals0.
  Nur RBS-Versand ist ausdrücklich0, weil der geplanteSammelwarenkorb99EUR
  übersteigt. Die150EUR fürsonstigeFracht sind eine eigeneBudgetreserve.
  RechnungsgebührSchrauben.Expert zusätzlich5EUR bruttoangenommen, Steuerbasisoffen.

## Budget nach Lieferant

Nur die numerisch bezifferten Grundpositionen; darunter befinden sich Schätzungen.
Die bevorzugten Ansprechpartner für unbezifferte Zeilen stehen in der Bestellliste.

'''
    text+=table(['Lieferant','Webpreise brutto','Schätzungen brutto','Summe beziffert brutto'],[
        [s,euro(total([o for o in web if o['supplier']==s],'gross_eur')),euro(total([o for o in estimate if o['supplier']==s],'gross_eur')),euro(total([o for o in web+estimate if o['supplier']==s],'gross_eur'))]
        for s in sorted({o['supplier'] for o in web+estimate})])
    text+='\n## Noch unbeziffert – Auswirkung auf die Vollständigkeit\n\n'
    text+=table(['Bestellzeile','Benötigter Umfang','Warum Preis fehlt'],[[o['id'],o['title'],o['specification']] for o in missing])
    text+='''
## Größte Kostenrisiken

Die fehlenden PCB-Entwürfe bestimmen Bestückung, Sensorinterface und Anschlussplan.
Ein Einkauf einzelner Platinenrohlinge löst diesen Entwicklungsbedarf nicht.
Originalmotoren undSKR1.3 können Beschaffungs- oder Umkonstruktionskosten verursachen.
Vier zusätzlicheNEMA14 statt derPlanmenge4 würden imreinenMotorbudget weitere
238EUR brutto erfordern; daraus folgt nochkein funktionierenderAntriebsplan.
Kamerakandidaten können nach demOptiktest entfallen oder einenanderenHalter benötigen.
Die historischenProjektkosten imBlog sind keinePreisgrundlage dieserKalkulation.

Maschinenlesbar: [Bestell-CSV](bestellliste.csv), [Summen-JSON](kosten.json).
Rechenweg undPrüfung: [Reproduktion](Reproduktion.md).
'''
    text='\n'.join(prose(line) if 'http' not in line else line for line in text.split('\n'))
    (BOM/'Kosten.md').write_text(text,encoding='utf-8')

def fabrication(parts):
    text='''# Fertigungsliste und Anforderungen für Angebote

**Alle Sonderteile benötigen noch eine Freigabe von Werkstoff, Passungen und Zeichnung.**
Die folgende Einteilung ist eine begründete Fertigungsplanung. Originalbelege und
Vorschläge stehen getrennt in der Tabelle. Maße sind lokale CAD-Hüllmaße in mm,
keine tolerierten Fertigungszeichnungen und bei Biegeteilen keine Flachzuschnitte.
Der Fusion-Import setzt nahezu überall „Stahl“; das ist kein Materialbeleg.

[Teileliste](Teileliste.md) · [Kosten](Kosten.md) · [CAD-Messdaten](evidence/cad-geometry.csv)

'''
    descriptions={
        '3D-Druck intern': '''PETG als nichtleitender Ausgangsvorschlag; bei wärmeren Motorhaltern ggf. temperaturfesteren Werkstoff testen. Originalwerkstoff unbekannt. 0,2-mm-Schichthöhe, vier Außenwände und 40–60% Infill sind ausschließlich Versuchsvorschläge. Führungs-/Lagersitze mit Probekörper und gegebenenfalls Nacharbeit qualifizieren; Gewinde/Inserts nur nach Zeichnung. Druckrichtung nach Kraftfluss, Stützen und Bauräumen festlegen. Keine pauschale Passung aus Hüllmaßen ableiten.

Materialkalkulation: Summe der CAD-Vollvolumen × Planmenge × angenommene Dichte1,27g/cm³, plus20% für Stützen/Fehldrucke; zusätzlich1kg für Kalibrierkörper/Versuche. Auf volle1kg-Rollen gerundet. Das ist ein bewusst konservativer Budgetansatz, kein Slicerresultat. Der echte Materialbedarf hängt von Infill, Wänden und Orientierung ab. Arbeitszeit/Maschinenkosten sind ausgeschlossen.''',
        'Blech intern': '''Die Basis-Motorplatten und Schlitten-Seitenteile sind durch Blog/Thesis als Laserteile belegt; andere Verfahren/Materialien bleiben Vorschläge. Für Basisplatten Stahl, z.B.S235, vorschlagen; Sorte und Beschichtung sind nicht belegt. Abdeckungen können andere Werkstoffe erfordern. Dicke beiCAD-003 geometrisch3mm, CAD-007/008/096/097/099/100 geometrisch5mm. Motorhalteplatten CAD-096/097 und Seitenplatten CAD-099/100 werden selbst gefräst (Luis 26.10.2026). CAD-024 ist3mm dick; Kettenhalter und Trigger benötigen eine gesonderte Dicken-/Biegeprüfung.

Für jede Variante: Flachkontur/DXF, Lochliste, Gewinde/Senkungen, Biegeradien/-winkel, Bezugsflächen, Entgratung und Korrosionsschutz festlegen. Die beiden5mm-Motorplatten und8Seitenteile belegen zusammen mindestens0,22176m² rechteckige Hüllfläche; die beidenSeitendeckel undTopdeckel weitere0,41822m².3mm-Rückwand0,17550m², vierKabeldeckel0,005104m². Das sind Flächen ohne Verschachtelung, Schnittfugen, weitereBleche oder Biegeabwicklungen. Der200EUR-Materialansatz ist eine eigene Schätzung, keine Zuschnittbestellung.''',
        'CNC extern': '''Vier Varianten, je2Stück =8Adapterplatten. CNC-Fräsen aus ENAW-6082T6,10mm-Ausgangsdicke ist ein Vorschlag. Prüfen, ob Lasern/Wasserstrahl plus Nacharbeit technisch genügt; dadurch kann sich der Preis ändern.

Angebotspaket: separate STEP-Datei jeCAD-ID,2D-PDF mit Datumsstand/Revision, Material, Rohmaß inklusive Aufmaß, Loch-/Gewindetabelle, Bezugsflächen, Funktionspassungen, Ebenheit/Parallelität und Oberfläche. ISO2768-m allenfalls als zu bestätigender Allgemeintoleranzvorschlag, keine pauschale Freigabe kritischer Führungssitze. Kanten entgraten.8Teile getrennt ausweisen, Prüfmaße dokumentieren, Fertigung inDE/EU verlangen. [Xometry](https://xometry.eu/de/faq/) ist ein möglicher Anbieter; noch kein Angebot angefragt. Budget100EUR netto jeTeil inklusiveRohmaterial, ohneTransport.''',
        'Weitere Fertigung': '''**Profile:** CAD-011/012/013/020:30×30,2×564+3×590+12×350 =7098mm netto. CAD-014:60×30,2×650 =1300mm. Nut6/I-Typ ist ein Kandidat; Nutgeometrie/Winkel/Nutensteine gegen CAD prüfen. Rohmaterialansatz8m bzw.1,4m enthält Reserve, garantiert aber bei noch unbekannten Lieferstangen keinen optimierten Schnittplan. Schnittfuge, Rechtwinkligkeit, Stirngewinde und zusätzliche Bohrungen separat angeben.

**Wellen:** CAD-098:8×Ø10×450 undCAD-069:2×Ø10×356,8 =4313,6mm netto. CF53h6 als Vorschlag, gehärtet/geschliffen nur passend zur gewählten Buchse. Enden entgraten; Längentoleranzen festlegen.5m Budgetmaterial. CAD-103:4×40×16×436mm Profilhülle; Hohlquerschnitt/Material noch identifizieren. CAD-070:2×11,5×11,5×205mm, CAD-108:8×Ø4×70mm, CAD-093/094: je4Triggerstäbe Ø8×125/75mm. CAD-109:4Distanzteile, Name2mm gegen geometrisch3mm auflösen.

**Kalibrierung:** Messingzylinder drehen/ablängen und Stirnflächen vermessen. Der aktuelle ReferenceBoard-Code unterscheidet vier innere ZylinderØ7/8/9/10, viererhöhteØ7 (Höhenniveaus6/8/10/12mm) undvieräußereØ7 aufGrundniveau; zusätzlich vierweißeReferenzen. Siehe SYS-005/037/039/040. Durchmesser7mm deräußerenGruppen kommen ausderCode-Skizze, nicht auseinerFertigungszeichnung. Thesis und spätererSoftwarestand sindverschiedeneVersionen. `inner_brass_pin_width=11.95`, `height=19.95` sowie `raised_brass_pin_width=59.6`, `height=39.9` sindRaster-/Abstandswerte, keineZylinderdurchmesser. ÄußereMessingpins liegenaufdenAchsen, weißePins andenEcken desRasters109,9×89,8mm. Marker18,2×18,2 undMarker-Raster60×80mm, Hamming-IDs1/3/6/12. Gesamtlänge/Einstecktiefe ist nichtEndflächenhöhe. TatsächlicheGeometrie vermessen undinSoftware hinterlegen; keinevollständigeFertigungszeichnung alleinausdenParametern behaupten.''',
        'PCB extern': '''**Signal-Multiplexer:** SCHUTZWERK-KiCad-Projekt mit Gerber liegt in `hardware/signal-multiplexer` (Bestellstand gerber1.1, Fertigung bei JLCPCB). **Für die übrigen Platinen keine Gerber/Schaltpläne gefunden.** STEP enthält äußerePlattenkörper, keine Leiterbahnen. Betroffen: vierPrüfspitzen-PCBs, eventuell24KanäleSensorinterface und der inSoftware konfigurierteZielversorgungscontroller. Platinen undBestückung sind eigeneZeilen; CAD-082 alsDummy wirdnichtnochmals bestellt. CAD-Stecker/Federkontakte nicht nochmals inPCBA-Budget aufnehmen.

[BetaLAYOUT](https://de.beta-layout.com/leiterplatten/) als deutscherFertiger. VorAngebot nötig: geprüfterSchaltplan, Gerber/Bohrdaten oder nativesPCB-Projekt, Lagenaufbau/Kupfer/Dicke, Bestückungs-BOM mitMPNs, Positionsdatei/CPL, Polungen, Panel-/Mengenangaben, E-Test undFunktionsprüfvorschrift. FR4/1,6mm ist nur einVorschlag (Prüfspitzen-Dicke geometrisch1,6mm); Lagenzahl/Kupferstärke fehlen. BareBoards, Stencil, Bauteile, Rüstkosten undBestückung getrennt anbietenlassen. KeineDevelopmentkosten oderPCBA-Preise erfunden.'''
    }
    for group,desc in descriptions.items():
        text+=f'## {group}\n\n'+desc+'\n\n'
        subset=[p for p in parts if p['group']==group]
        text+=table(['ID / Teil','Planmenge','CAD-Hülle mm / Volumen jeTeil','Verfahren / Werkstoffbeleg','Offen'],[
            [p['id']+' '+p['name'],qty(p['quantity'])+' '+p['unit'],(p['geometry_mm'] or 'offen')+' / '+(p['solid_volume_cm3']+'cm³' if p['solid_volume_cm3'] else 'offen'),p['process_evidence']+'; '+p['material'],p['issue']] for p in subset])+'\n'
    text='\n'.join(prose(line) if 'http' not in line else line for line in text.split('\n'))
    (BOM/'Fertigung.md').write_text(text.rstrip()+'\n',encoding='utf-8')

def montage(parts,components):
    """Assembly modules from bom/montage/module.json with per-module status counts."""
    spec=json.loads((BOM/'montage/module.json').read_text(encoding='utf-8'))
    byid={p['id']:p for p in parts}
    rows=[]
    for m in spec['module']:
        for t in m['teile']:
            if 'sys' in t:
                p=byid[t['sys']]
                rows.append(dict(modul=m['id'],modulname=m['name'],scope='ohne CAD',id=p['id'],name=p['name'],cad_name='',
                                 quantity=p['quantity'],cad_total=p['quantity'],status=p['status'],group=p['group'],hint=t.get('hinweis','')))
                continue
            scopes=t['scope'] if isinstance(t['scope'],list) else [t['scope']]
            hits=[r for r in components if r['fusion_path'] in scopes and r['cad_name']==t['cad_name']
                  and ('sub' not in t or r['subassembly']==t['sub'])]
            assert hits,(m['id'],t)
            p=byid[hits[0]['id']]
            rows.append(dict(modul=m['id'],modulname=m['name'],scope=';'.join(scopes)+(('+'+t['sub']) if 'sub' in t else ''),id=p['id'],name=p['name'],cad_name=p['cad_name'],
                             quantity=t.get('menge',sum(r['quantity'] for r in hits)),cad_total=sum(r['quantity'] for r in hits),
                             status=p['status'],group=p['group'],hint=t.get('hinweis','')))
            assert rows[-1]['quantity']<=rows[-1]['cad_total'],(m['id'],t)
    write_csv(BOM/'montage/montage.csv',rows)
    order=['bestellfähig','teilweise geklärt','Fertigung noch offen','Fertigung spezifiziert','nicht identifiziert','nicht benötigt']
    text='# Montagemodule\n\nSchrittweiser Aufbau in logisch zusammengehörigen Modulen. Definition in [module.json](module.json), Teile mit Mengen in [montage.csv](montage.csv). Mengen sind CAD-Mengen im jeweiligen Fusion-Einbau; Status aus der [Teileliste](../Teileliste.md). In Fusion einblenden: `tools/fusion_show_module.py`.\n\n'
    text+=table(['Modul','Positionen','Stück',*order],[
        [f"[{m['id']} {m['name']}](#modul-{m['id'][1:]})",len([r for r in rows if r['modul']==m['id']]),
         sum(r['quantity'] for r in rows if r['modul']==m['id']),
         *[len([r for r in rows if r['modul']==m['id'] and r['status']==s]) for s in order]] for m in spec['module']])+'\n'
    for m in spec['module']:
        sub=[r for r in rows if r['modul']==m['id']]
        text+=f"<a id=\"modul-{m['id'][1:]}\"></a>\n\n## {m['id']} {m['name']}\n\n{m['beschreibung']}\n\n*{m['stand']}*\n\n"
        text+=table(['ID / Teil','CAD-Name','Stück','Status','Beschaffungsart'],[
            [f"[{r['id']}](../Teileliste.md#{r['id'].lower()}) {r['name']}",f"`{r['cad_name']}`" if r['cad_name'] else 'nicht im CAD',
             f"{r['quantity']} von {r['cad_total']}" if r['quantity']!=r['cad_total'] else r['quantity'],
             r['status']+(f"; {r['hint']}" if r['hint'] else ''),r['group']]
            for r in sorted(sub,key=lambda r:(order.index(r['status']),r['id']))])+'\n'
        if m.get('werkstatt'):
            text+='**Werkstattfertigung**\n\n'+''.join(f'- {q}\n' for q in m['werkstatt'])+'\n'
        if m.get('zusatz'):
            text+='**Zusätzlich nötig, nicht im CAD**\n\n'+table(['Teil','Stück','Bezug','Grund'],[[z['teil'],z['menge'],z['bezug'],z['grund']] for z in m['zusatz']])+'\n'
        if m.get('entfernt'):
            text+='**Bei der Prüfung aus dem Modul genommen**\n\n'+''.join(f'- {q}\n' for q in m['entfernt'])+'\n'
        if m.get('offen'):
            text+='**Offene Fragen**\n\n'+''.join(f'- {q}\n' for q in m['offen'])+'\n'
    placed=Counter()
    for r in rows: placed[r['id']]+=r['quantity']
    rest={p['id']:int(p['cad_quantity'])-placed[p['id']] for p in parts if p['cad_name'] and int(p['cad_quantity'])>placed[p['id']]}
    assert set(rest)<={'CAD-063','CAD-066','CAD-082'},rest
    text+='## Abdeckung\n\nAlle CAD-Vorkommen sind einem Modul zugeordnet außer: '+'; '.join(f"{byid[i]['name']} ({n})" for i,n in sorted(rest.items()))+'. Das sind CAD-Platzhalter bzw. doppelte Motor-Einbaulagen.\n'
    (BOM/'montage/Montage.md').write_text(text.rstrip()+'\n',encoding='utf-8')
    return rows

def validate(parts,orders,components=None):
    with (BOM/CAD).open(encoding='utf-8-sig') as f:
        expected={r['id'] for r in csv.DictReader(f)}
    actual=[p['id'] for p in parts if p['id'].startswith('CAD-')]
    assert len(actual)==120 and set(actual)==expected and len(set(actual))==len(actual)
    assert sum(int(p['cad_quantity']) for p in parts if p['cad_quantity'])==1066
    assert len({p['id'] for p in parts})==len(parts)
    assert len({o['id'] for o in orders})==len(orders)
    if components is not None:
        placed=Counter()
        for r in components:
            if r['component']!=NOT_IN_CAD: placed[r['id']]+=r['quantity']
        for p in parts:
            if p['cad_name']: assert placed[p['id']]==int(p['cad_quantity']),p['id']
        assert len({r['component'] for r in components})==14
        assert {r['id'] for r in components if r['component']==NOT_IN_CAD}=={p['id'] for p in parts if not p['cad_name']}
    for p in parts:
        assert p['status'] in {'bestellfähig','teilweise geklärt','Fertigung spezifiziert','Fertigung noch offen','nicht identifiziert','nicht benötigt'}
        assert p['source'] and p['issue']
        if p['status']!='nicht benötigt' and p['group']!='Optional': assert p['cost_id'],p['id']
        if p['status']=='bestellfähig':
            match=[o for o in orders if o['id']==p['cost_id']][0]
            assert match['sku']!='offen' and match['url']
    for o in orders:
        if o['price_kind']=='offen': assert o['net_eur'] is None and o['gross_eur'] is None
        if o['order_quantity'] is not None: assert o['order_quantity']>=D(str(o['need']))
        if o['gross_eur'] is not None:
            assert abs(o['gross_eur']-money(o['net_eur']*(1+VAT)))<=CENT

def main():
    parts=make_parts();orders=make_orders(parts);components=make_components(parts);validate(parts,orders,components)
    write_csv(BOM/'teileliste.csv',parts);write_csv(BOM/'bestellliste.csv',orders)
    write_csv(BOM/'teileliste-komponenten.csv',components)
    totals=render(parts,orders,components)
    montage(parts,components)
    print(json.dumps(totals,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
