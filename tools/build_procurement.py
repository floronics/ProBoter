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
SHEET = ids(3,16,17,18,19,7,8,9,24,26,96,97,99,100)
CNC = []  # adapter plates moved to the workshop (decision 17.10.2026)
WORKSHOP = ids(3,16,17,18,19,96,97,99,100)
STOCK = ids(11,12,13,14,20,69,70,93,94,98,103,108,109)
PCB = ids(75)
UNIDENTIFIED = ids(10,55,61,62,73,86,115)
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
23: ('BIGTREETECH SKR V1.3 Steuerplatine', 'Original laut CAD, Firmware und Masterarbeit. Neu in DE/EU nicht gefunden (Recherche 17.10.2026). Kandidat SKR 1.4 Turbo (RBS13645) passt auf fast dieselben Löcher, braucht aber Marlin-Pinanpassung; nicht freigegeben.', 'RBS'),
27: ('CPC MR12ML Führungswagen', '8 Wagen MR12MLSSV0N für 2×600-mm-Schienen. CPC-Katalog SS-Ausführung: L 47,6, Körperhöhe 10, Breite 27, Lochbild 20×20 M3 = CAD und Fusion-Messung. Lieferbarkeit bei Motedis prüfen.', 'MOTEDIS'),
49: ('igus E2i.10.10.028.0, 16 kurze Abschnitte', 'Teilung 20 mm, Außenbreite 17,4, Einbauhöhe 71 bei R28 = CAD. 0,24 m = 12 Glieder, zusammen 192 Glieder. Anschlüsse siehe SYS-027.', 'IGUS'),
50: ('igus E2i.10.20.028.0, 8 lange Abschnitte', 'Teilung 20 mm, Außenbreite 27,4, Einbauhöhe 71 = CAD. 0,28 m = 14 Glieder, zusammen 112 Glieder. Anschlüsse siehe SYS-028.', 'IGUS'),
51: ('Schubladengriff, Lochabstand 100 mm', 'DOLD A-75903 passt in Länge 113, Höhe 49 und Lochabstand 100, hat aber M6-Gewinde; Fusion misst Ø5,5. Prüfen, ob die CAD-Bohrung ein Durchgangsloch ist (dann A-75873, 112 mm lang).', 'DOLD'),
52: ('Gelenkfuß M6×20 / Teller Ø40 mm', 'DOLD GF-K-10-PA-028: M6, Teller Ø40 = CAD; Fusion-Messung Gewindelänge 20 mm = Variante M6×20. Traglast vom Händler nicht angegeben.', 'DOLD'),
53: ('HIWIN MGNR12R150HM, Z-Schiene 150 mm', 'HIWIN-Katalog: 12×8, Teilung 25, Bohrung Ø3,5/Ø6; 150 mm mit 6 Bohrungen und Endabstand 12,5 = Fusion-Messung. Bezug Damen CNC (NL), Zuschnitt.', 'DAMEN'),
54: ('HIWIN MGN12CZ0HM Z-Führungswagen', 'Bestellschlüssel: Z0 spielfrei, H hohe Genauigkeit, M Edelstahl. Breite 27, Körperhöhe 10, Lochbild 20×15 M3 = CAD; Katalog-Länge 34,7 statt CAD 35,7.', 'DAMEN'),
55: ('Induktiver Näherungsschalter M8, Bauhülle60mm', '24 CAD-Vorkommen. MPN, Schaltabstand, NPN/PNP, NO/NC, Versorgung, Pegel und Kabellänge fehlen.24V nicht direkt an SKR-Eingänge; InterfaceCAD-unabhängig SYS-019.', 'TME'),
59: ('Mean Well MHS012 Montagewinkel', '4 Winkel für RSP-200. Mean-Well-Zeichnung 15×16,2×19,5 mm = CAD (Abweichung höchstens 0,3 mm). Reichelt MHS-012.', 'REICHELT'),
60: ('Mean Well RSP-200-24 Netzteil,24V/8,4A', 'Originalmodell,215×115×30mm. Lastbilanz, Absicherung, Berührungsschutz und Schutzleiter separat.', 'REICHELT'),
61: ('MMCX-Stecker gerade / Messleitung', '4 CAD-Modelle enthalten Kabelansätze. Impedanz, Kabeltyp, Crimp/Lötanschluss, Gegenstecker und Länge unbekannt.', 'TME'),
62: ('MMCX-Stecker gewinkelt / Messleitung', '4 CAD-Modelle; Kabel-/Buchsenpaarung mitCAD-061/075 und Multiplexer offen.', 'TME'),
63: ('NEMA14 Z-Motor, ERSATZ: STEPPERONLINE 14HS13-0804S statt Nanotec ST3518M1004-A', 'ORIGINALMOTOR AUSGETAUSCHT (Entscheidung Luis 17.10.2026). Original nur im Nanotec-Archiv. Ersatz 34,8 mm statt 36 mm lang, Welle Ø5×24 mit D-Abflachung, 0,8 A statt 1,0 A, 18 statt 14 Ncm, Litzen ohne Stecker. Motorstrom in der Firmware auf 0,8 A begrenzen. Fusion-Messung: nur 2,8 mm Luft zum Endschalter, kürzerer Motor passt.', 'STEPPERONLINE'),
64: ('Nanotec ST4118M1804-A NEMA17 X/Y-Motor', 'Originalmodell, aktuelle Nanotec-Serie: 1,8 A, 0,28 Nm, 38 mm, Welle Ø5×24, Litzen 300 mm mit JST XHP-4. 12 laut STEP (8 X + 4 Y), im Fusion-Import fehlend. Verfügbarkeit beim Hersteller anfragen.', 'NANOTEC'),
65: ('Optischer Endschalter 11×35 mm', 'RBS12901: 35×11 mm und Lochabstand 28 mm stimmen mit der Fusion-Messung überein. VCC/GND/SIG, 2,7–5 V, HIGH bei Unterbrechung. Pinfolge am SKR-Stecker vor dem Anschluss prüfen.', 'RBS'),
73: ('Prüfkontakt-Hülse P75-2 W', '8 Stück, CADØ1,2×25,4mm. Hersteller und passender FederkontaktCAD-115 unklar; Kontaktpaar vollständig spezifizieren.', 'TME'),
75: ('Prüfspitzen-PCB, unbestückt', '4 Stück;26,67×10,96×1,6mm Hülle. Schaltplan, Kupfer, Bohrungen, Gerber und Bestückungsdaten fehlen. Bestückung SYS-024 separat.', 'BETA'),
76: ('GT2-Zahnscheibe Z16 / 9 mm / Bohrung 5 mm, ANPASSUNG', 'Exaktes Teil (Ø18×11) in der EU nicht lieferbar. RBS12867 (Ø13×19,5, für 10-mm-Riemen) wird verwendet; Y-Schlitten-Druckteil und Umlenkachse müssen angepasst werden (Entscheidung Luis 17.10.2026). Fusion-Messung: Umlenkscheibe hat nur 3 mm Luft zum Schlitten.', 'RBS'),
77: ('GT2-Antriebsriemenscheibe Z16 / 6 mm / Bohrung 5 mm', '12 X/Y-Antriebe. RBS10278: Bordscheibe Ø14 statt CAD Ø13; Fusion-Messung zeigt 4,6 mm Abstand zum nächsten Teil, passt.', 'RBS'),
78: ('GT2-Umlenkrolle Z16 / 6 mm / Bohrung 3 mm', '20 Stück. Tinytronics 002225: Bohrung 3, Ø13, Breite 8,5 mm = CAD exakt (Rollen sitzen paarweise ohne Luft zwischen den Spannerflügeln).', 'TINYTRONICS'),
79: ('SHF10 Flanschhalter fürØ10mm Welle', '16 Stück.43×24×10mm undØ5,5-Befestigung stimmen mitDOLD11260 überein. Liefertermin27.11.2026 angekündigt.', 'DOLD'),
80: ('Lineargleitbuchse Ø10 innen / Ø19 außen / Länge 29 mm', 'igus RJ4JP-01-10: d 10, D 19, B 29, Nut Ø18 = CAD und Fusion-Messung. iglidur J4, LM10UU-Bauform.', 'DOLD'),
81: ('Anschraubwinkel 30 / Nut 6', 'DOLD 62378 (I-Typ Nut 6) 28×28×28 = CAD; bestellt als Satz 62385-BS mit Schrauben und Nutensteinen.', 'DOLD'),
84: ('Teleskopschiene 350 mm, Vollauszug', 'DOLD HS-4613-350 (CAD-Name enthält 4613): 350×45,7×12,7 (CAD 45,5), 1 Paar = die 2 CAD-Schienen. Vollauszug 354 mm.', 'DOLD'),
85: ('Bewegliches USB-Mikroskop', 'Plan1 laut Hardware-Blog,4CAD. Weitere3 optional. Originalmodell unbekannt; Kandidat muss100mm Arbeitsabstand/ca30×40mm Bildfeld und Linux-UVC erfüllen.', 'REICHELT'),
86: ('Bedientaster/-schalterØ19mm', 'Schaltfunktion rastend/tastend, Kontaktlast, Beleuchtung und Zuordnung zu Versorgung/Software unbekannt.', 'REICHELT'),
87: ('GT2-Riemen X, 6 mm breit', '8 Verläufe, offen mit Spanner an beiden Enden. Fusion-Messung: 699 mm Trum, Teillänge 1.430 mm je Verlauf; Zuschnitt mit 2×40 mm Klemmzugabe ca. 1,51 m. Summe X+Y ca. 16,5 m aus zwei 10-m-Rollen.', 'DOLD'),
95: ('CPC MR12M Führungsschiene 600 mm', '2 Stück MR12M-N-600: 12×7,5 mm, Teilung 25, 24 Bohrungen Ø3,5/Ø6, Endabstand 12,5 = CAD. Nicht mit HIWIN MGN mischen.', 'MOTEDIS'),
104: ('GT2-Riemen Y, 6 mm breit', '4 Verläufe. Fusion-Messung: 492 mm Trum, Teillänge 1.016 mm; Zuschnitt mit 2×40 mm Klemmzugabe ca. 1,10 m. Einkauf gemeinsam mit CAD-087, nicht doppelt rechnen.', 'DOLD'),
113: ('GT2-Riemen Z, 9 mm breit', '4 Verläufe, offen am Z-Riemenhalter geklemmt. Fusion-Messung: Achsabstand 108 mm, Teillänge 248 mm; Zuschnitt mit 2×35 mm Klemmzugabe ca. 0,32 m, zusammen 1,3 m. RBS14040 als Meterware.', 'RBS'),
115: ('Federkontakt der Prüfspitze', '8 Stück, CADØ1×16,6mm. Spitzenform, Hub, Federkraft, Kontaktmaterial und Paarung mitP75-2-W unklar.', 'TME'),
}

# Explicit non-CAD system inventory. Quantities are planning values, not discoveries.
# key, description, quantity, unit, group, supplier, specification/gap, source
SYSTEM = [
('001','TMC2130 SPI Treibermodule',16,'Stück','Kaufteile','RBS','4 je SKR für X/X2/Y/Z. RBS13024: 4 Treiber mit Kühlkörpern und Kabel, SPI-Pins laut Fotos vorgelötet. Revision nicht angegeben; SPI-Modus laut Datenblatt per Lötbrücke CFG4/CFG5 prüfen.',FIRMWARE),
('002','Stationäre Übersichtskamera',1,'Stück','Kaufteile','REICHELT','1080p-Softwarekonfiguration; Optik, Blickfeld und Halterpassung offen.',BLOG),
('003','Signal-Multiplexer, unbestückte Leiterplatte',1,'Stück','PCB extern','BETA','CAD-082 ist nur Platzhalter. Schaltplan/Gerber/Board-BOM fehlen; USB/9600Baud-Protokoll ist keine Schaltung.',SOFTWARE),
('004','Kalibrier-Referenzkörper / Platte',1,'Stück','3D-Druck intern','RBS','Geometrie mit aktueller Software festlegen; Plattendicke5,1mm ist Konfigurationswert, keine validierte Zeichnung.',SOFTWARE),
('005','Innere Messing-Referenzzylinder',4,'Stück','Weitere Fertigung','DOLD','Je1×Ø7/8/9/10mm nach ReferenceBoard.inner_brass_pin_position_map; Raster11,95×19,95mm. Endfläche auf Bezugsebene; Gesamtlänge, Einbau, Toleranzen und Messprotokoll fehlen.','../software/hardware-control/proboter/tasks/utils/reference_board.py'),
('006','Kalibriermarker / matte Druckvorlage',1,'Satz','Weitere Fertigung','OFFEN','4Hamming-Marker mitIDs1/3/6/12 lautReferenceBoard, je18,2×18,2mm, Raster60×80mm. Mtracker-Format verwenden, keinebeliebigenArUco-Marker. Maßstab1:1 undrealeAbstände vermessen.','../software/hardware-control/proboter/tasks/utils/reference_board.py'),
('007','Weißer24-V-LED-Streifen',2,'m','Kaufteile','REICHELT','2m vorläufig;5m-Rolle. Weiß4500K vorgeschlagen; Leistung, Flimmern und Lichtverteilung testen.',BLOG),
('008','LED-Aluprofile, Diffusoren, Kappen, Halter',2,'m','Kaufteile','DOLD','8mm-Streifen aufnehmen, Wärmeabfuhr und Befestigung; genaue Aufteilung/Menge offen. Keine Doppelrechnung als Band.',BLOG),
('009','LED-Anschluss an vorhandenen SKR-Ausgang',1,'Satz','Kaufteile','REICHELT','Configuration_adv.h:4396 setzt PROBOTER_LIGHT_CONTROL_PIN auf HEATER_BED_PIN; M376 steuert Helligkeit. Kein separater USB-LED-Controller nötig. Stecker/Leitungen, Strom und Flimmern prüfen; keine zusätzliche MOSFET-Platine pauschal kaufen.','../firmware/Marlin/Configuration_adv.h'),
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
('023','Signal-Multiplexer Bestückung',1,'Baugruppe','PCB extern','BETA','MCU, USB/Versorgung, Schalter/Relais, Schutz, Stecker, Passives und Montage nach noch fehlendem Schaltplan. Keine Stückzahlen erfinden.',SOFTWARE),
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
('037','Weiße äußere Kalibrierreferenzen',4,'Stück','Weitere Fertigung','OFFEN','ReferenceBoardConfig beschreibt vier äußere weiße Referenzpins. Raster109,9×89,8mm; Durchmesser, Höhe, Material und Umsetzung am gewählten Board fehlen. Nicht mit12Messingpins gleichsetzen.','../software/hardware-control/proboter/model/reference_board_config.py'),
('038','Kalibrier-Kontaktleitungen und gemeinsame Messreferenz',1,'Satz','Kaufteile','TME','4SKR-Zentriereingänge P0_17 mitPull-up/aktivLow sowie Referenzkörper/Kontaktkreis verdrahten. Netzplan, Stecker, Länge undBezugspotenzial mitMultiplexer klären; keineVerbindung ungeprüft festlegen.','../firmware/Marlin/src/module/proboter.cpp'),
('039','Erhöhte Messing-Referenzzylinder',4,'Stück','Weitere Fertigung','DOLD','Ø7mm lautReferenceBoard-Skizze; Code setzt vierEndflächen6/8/10/12mm über Bezugsebene aufRaster59,6×39,9mm. Gesamtlängen undEinstecktiefe sindnichtdieseHöhen; Zeichnung undToleranzen fehlen.','../software/hardware-control/proboter/tasks/utils/reference_board.py'),
('040','Äußere flache Messing-Referenzzylinder',4,'Stück','Weitere Fertigung','DOLD','Ø7mm lautReferenceBoard-Skizze; Mittelpunkte(±54,95;0) und(0;±44,9)mm. Endflächen aufBezugsebene; Länge undMontage offen. Insgesamt12Messingzylinder plus4weißeReferenzen.','../software/hardware-control/proboter/tasks/utils/reference_board.py'),
('041','Nutenstein I-Typ Nut 6, M6, Motorplatten',8,'Stück','Kaufteile','DOLD','Fusion-Kontaktanalyse M01: die 8 Senkschrauben M6×20 der Motorplatten greifen in die Nut der 60×30-Profile; im CAD kein Gegenstück.',CAD),
('042','Nutenstein I-Typ Nut 6, M4, Rückwand',6,'Stück','Kaufteile','DOLD','Fusion-Kontaktanalyse M01: 6 Bohrungen Ø4,5 der Rückwand liegen auf den langen Profilen; im CAD keine Befestigung.',CAD),
('043','Zylinderschraube DIN 912 M4×10 A2, Rückwand',6,'Stück','Kaufteile','SCHRAUBEN','Zu SYS-042; 3 mm Rückwand plus Nutenstein.',CAD),
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
            note = 'CAD-Prüfobjekt, kein Maschinenteil.' if key=='CAD-066' else 'Nur Platzhalter; reale Multiplexer-Platine und Bestückung unterSYS-003/023 erfasst.'
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
        if key in ids(11,12,13,14,20,27,63,69,76,77,78,98,49,50,52,53,54,59,60,64,65,79,80,81,84,87,95,104,113) or (key in NORM and key!='CAD-058'): status='bestellfähig'
        if key=='CAD-080': title='GleitbuchseØ10 innen / Ø19 außen / Länge29mm'
        if key=='CAD-001': title='Y-Riemenklemme (CAD-Name TR10x2 GT2 Adapter)'
        if key=='CAD-002': title='Y-Riemenklemme, Deckel'
        if key=='CAD-010':
            note='Schubladen-Dummy564×410×12mm: unklar, ob reale Platte benötigt und welches Material. Nicht stillschweigend ausschließen oder aus Stahl fertigen.'
        if group=='3D-Druck intern':
            status='Fertigung spezifiziert'
            process_evidence='3D-Druck intern, PETG, Geometrie als STL aus dem CAD (Entscheidung Luis 17.10.2026)'
        if key in ids(16,17,18,19,99,100):
            material='Stahl- oder Aluminiumblech, Werkstattentscheidung'
            process_evidence='WERKSTATT: eigene Fertigung (Entscheidung Luis 17.10.2026)'
            note=('10 mm Platte mit Stufen auf 5 mm und 90°-Senkungen; trägt die X-Riemenantriebe. Fräsen oder aus zwei 5-mm-Platten.' if key in ids(16,17,18,19) else '5 mm Seitenplatte des X-Wagens, im Original lasergeschnitten.')+' Zeichnung aus CAD ableiten.'
        if key=='CAD-108':
            note='Fusion-Messung: massiver Rundstab Ø4×70 mm, Fasen an beiden Enden, ohne Gewinde. Werkstatt: aus Ø4-h6-Silberstahl (1.2210) ablängen und anfasen (Entscheidung Luis 17.10.2026).'
            material='Silberstahl 1.2210 Ø4 h6'; status='Fertigung spezifiziert'; process_evidence='WERKSTATT: Ablängen und Anfasen'
        if key=='CAD-103':
            note='Profil 16×40, 436 mm, CAD-Querschnitt 446 mm², Kernbohrungen Ø2,46/Ø5. Kein passendes Nut-5-Profil gefunden (Recherche 17.10.2026); Kandidat norelem 16×40 Typ I hat Nut 8. Profil identifizieren.'
        if key=='CAD-003':
            material='Aluminium 3 mm (Entscheidung 17.10.2026), z. B. EN AW-5754'
            process_evidence='WERKSTATT: eigene Fertigung aus Blech oder Aluminium (Entscheidung Luis 17.10.2026)'
            note='650×270×3 mm, 54 Bohrungen Ø3,4, 10 Bohrungen Ø4,5, 1 Bohrung Ø8. 6 Ø4,5-Bohrungen sitzen auf den langen Profilen (M4 + Nutenstein, siehe M01). Zuschnitt und Bohrungen intern; Zeichnung aus CAD ableiten.'
        if key in ids(96,97):
            process_evidence='WERKSTATT: eigene Fertigung aus Stahl- oder Aluminiumblech (Entscheidung Luis 17.10.2026); Original lasergeschnitten (Blog)'
            material='Stahl- oder Aluminiumblech 5 mm, Werkstattentscheidung'
            note='5 mm Stahl, 550×135 mm. Fusion-Messung: 16 Kernlöcher Ø2,46 für M3-Gewinde (Riemenspanner), Senkungen für M6 und Ø22-Durchbrüche für die Motoren. Kontur und Bohrungen aus CAD; Gewinde und Senkungen intern. Zeichnung mit Lagetoleranzen der Führungsbohrungen fehlt.'
        if key=='CAD-020':
            note='Querschnitt und Länge aus CAD (4×350 mm). Unten M6-Gewinde in die Kernbohrung Ø5 für die Gelenkfüße, intern schneiden (Entscheidung 17.10.2026). Profilserie siehe M01.'
        if key=='CAD-109':
            note='Name nennt2mm, CAD zeigt3mm Dicke. Innendurchmesser, Material und benötigte Distanz vor Fertigung klären.'
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
        if key in ('041','042','043'): status='bestellfähig'
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
    add('BUY-010','Übersichtskamera, Ersatzkandidat',['SYS-002'],1,offer='O-011')
    add('BUY-011','USB-Mikroskop, Ersatzkandidat',ids(85),1,offer='O-012')
    add('BUY-012','Aktiver7Port-USB-Hub',['SYS-010'],1,offer='O-013')
    add('BUY-013','LED5m-Rolle fürgeplant2m',['SYS-007'],2,unit='m',offer='O-014')
    add('ALT-001','MR12MLVergleich, keine bestätigteCPC-Paarung',ids(27),8,offer='O-015',optional=True)
    add('ALT-002','MGN12CNachbauvergleich, keinHIWIN',ids(54),4,offer='O-016',optional=True)
    add('OPT-001','3zusätzlicheMikroskope',['SYS-033'],3,offer='O-012',optional=True,note='Nur Kamerapreis; zusätzliche Kabel, Halteränderung und USB-Topologie nicht kalkuliert.')

    # Own rough budget assumptions; not supplier quotations or promises of fit.
    add('BUY-014','12 NEMA17 Originalmotoren',ids(64),12,offer='O-041')
    add('BUY-015','4 NEMA14 Z-Motoren, ERSATZ STEPPERONLINE 14HS13-0804S',ids(63),4,offer='O-063',estimate='8',basis='net',note='Shoppreis 8,48 USD, als 8 EUR netto geschätzt; EUR-Preis und Versandlager im Checkout prüfen.')
    add('BUY-016','4 Steuerplatinen, Ersatzkandidat SKR 1.4 Turbo',ids(23),4,offer='O-043',note='Preis des Ersatzkandidaten; Firmware-Migration nicht enthalten und nicht freigegeben.')
    add('BUY-018','8 CPC-Führungswagen MR12ML',ids(27),8,offer='O-045')
    add('BUY-019','2 CPC-Schienen MR12M 600 mm',ids(95),2,offer='O-046')
    add('BUY-020','4 HIWIN-Schienen 150 mm',ids(53),4,offer='O-047')
    add('BUY-021','4 HIWIN-Wagen MGN12C',ids(54),4,offer='O-048')
    add('BUY-022','16 Gleitbuchsen RJ4JP-01-10',ids(80),16,offer='O-052')
    add('BUY-023','Lange Energieketten, 112 Glieder',ids(50),112,unit='Glied',offer='O-049',note='8 Abschnitte à 14 Glieder (0,28 m).')
    add('BUY-024','16 Anschlusssätze E2.10 schmal',['SYS-027'],16,unit='Satz',offer='O-050')
    add('BUY-025','8 Anschlusssätze E2.10 breit',['SYS-028'],8,unit='Satz',offer='O-051')
    add('BUY-017','Z-Riemen 9 mm',ids(113),D('1.28'),unit='m',offer='O-044',note='Zuschnitt aus Fusion-Messung 4×0,32 m.')
    for key in ('SYS-041','SYS-042','SYS-043'):
        add('BUY-'+key,byid[key]['name'],[key],byid[key]['quantity'],offer=cad_offers[key])
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
    add('MAT-005','Versteifungsprofile40×16 undHalte-/Distanzstäbe',ids(70,93,94,103,108,109),1,unit='Los',estimate='100',note='Eigenes100EUR-Bruttobudget fürProfile4×436mm, Rechteck2×205mm, Ø8Trigger4×125+4×75mm, Ø4Stäbe8×70mm und4Distanzteile. Material/Profile noch klären.')
    add('MAT-006','Blechrohmaterial undVerschnitt',[p['id'] for p in parts if p['group']=='Blech intern'],1,unit='Los',estimate='200',note='Eigener200EUR-Bruttobudgettopf für3/5mmPlatten und noch nicht abgewickelteTeile. Kein Händlerangebot; Material/Flachzuschnitte noch nicht bestellfähig. InterneArbeits-/Maschinenzeit ausgeschlossen.')
    for key,amount in [('008','30'),('011','20'),('012','15'),('013','15'),('014','64'),('015','25'),('018','60'),('020','35'),('021','15'),('022','60'),('025','20'),('029','35'),('030','20'),('031','35'),('032','30')]:
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
        'Blech intern': '''Die Basis-Motorplatten und Schlitten-Seitenteile sind durch Blog/Thesis als Laserteile belegt; andere Verfahren/Materialien bleiben Vorschläge. Für Basisplatten Stahl, z.B.S235, vorschlagen; Sorte und Beschichtung sind nicht belegt. Abdeckungen können andere Werkstoffe erfordern. Dicke beiCAD-003 geometrisch3mm, CAD-007/008/026/096/097/099/100 geometrisch5mm. CAD-024 ist3mm dick; Kettenhalter und Trigger benötigen eine gesonderte Dicken-/Biegeprüfung.

Für jede Variante: Flachkontur/DXF, Lochliste, Gewinde/Senkungen, Biegeradien/-winkel, Bezugsflächen, Entgratung und Korrosionsschutz festlegen. Die beiden5mm-Motorplatten und8Seitenteile belegen zusammen mindestens0,22176m² rechteckige Hüllfläche; die beidenSeitendeckel undTopdeckel weitere0,41822m².3mm-Rückwand0,17550m², vierKabeldeckel0,005104m². Das sind Flächen ohne Verschachtelung, Schnittfugen, weitereBleche oder Biegeabwicklungen. Der200EUR-Materialansatz ist eine eigene Schätzung, keine Zuschnittbestellung.''',
        'CNC extern': '''Vier Varianten, je2Stück =8Adapterplatten. CNC-Fräsen aus ENAW-6082T6,10mm-Ausgangsdicke ist ein Vorschlag. Prüfen, ob Lasern/Wasserstrahl plus Nacharbeit technisch genügt; dadurch kann sich der Preis ändern.

Angebotspaket: separate STEP-Datei jeCAD-ID,2D-PDF mit Datumsstand/Revision, Material, Rohmaß inklusive Aufmaß, Loch-/Gewindetabelle, Bezugsflächen, Funktionspassungen, Ebenheit/Parallelität und Oberfläche. ISO2768-m allenfalls als zu bestätigender Allgemeintoleranzvorschlag, keine pauschale Freigabe kritischer Führungssitze. Kanten entgraten.8Teile getrennt ausweisen, Prüfmaße dokumentieren, Fertigung inDE/EU verlangen. [Xometry](https://xometry.eu/de/faq/) ist ein möglicher Anbieter; noch kein Angebot angefragt. Budget100EUR netto jeTeil inklusiveRohmaterial, ohneTransport.''',
        'Weitere Fertigung': '''**Profile:** CAD-011/012/013/020:30×30,2×564+3×590+12×350 =7098mm netto. CAD-014:60×30,2×650 =1300mm. Nut6/I-Typ ist ein Kandidat; Nutgeometrie/Winkel/Nutensteine gegen CAD prüfen. Rohmaterialansatz8m bzw.1,4m enthält Reserve, garantiert aber bei noch unbekannten Lieferstangen keinen optimierten Schnittplan. Schnittfuge, Rechtwinkligkeit, Stirngewinde und zusätzliche Bohrungen separat angeben.

**Wellen:** CAD-098:8×Ø10×450 undCAD-069:2×Ø10×356,8 =4313,6mm netto. CF53h6 als Vorschlag, gehärtet/geschliffen nur passend zur gewählten Buchse. Enden entgraten; Längentoleranzen festlegen.5m Budgetmaterial. CAD-103:4×40×16×436mm Profilhülle; Hohlquerschnitt/Material noch identifizieren. CAD-070:2×11,5×11,5×205mm, CAD-108:8×Ø4×70mm, CAD-093/094: je4Triggerstäbe Ø8×125/75mm. CAD-109:4Distanzteile, Name2mm gegen geometrisch3mm auflösen.

**Kalibrierung:** Messingzylinder drehen/ablängen und Stirnflächen vermessen. Der aktuelle ReferenceBoard-Code unterscheidet vier innere ZylinderØ7/8/9/10, viererhöhteØ7 (Höhenniveaus6/8/10/12mm) undvieräußereØ7 aufGrundniveau; zusätzlich vierweißeReferenzen. Siehe SYS-005/037/039/040. Durchmesser7mm deräußerenGruppen kommen ausderCode-Skizze, nicht auseinerFertigungszeichnung. Thesis und spätererSoftwarestand sindverschiedeneVersionen. `inner_brass_pin_width=11.95`, `height=19.95` sowie `raised_brass_pin_width=59.6`, `height=39.9` sindRaster-/Abstandswerte, keineZylinderdurchmesser. ÄußereMessingpins liegenaufdenAchsen, weißePins andenEcken desRasters109,9×89,8mm. Marker18,2×18,2 undMarker-Raster60×80mm, Hamming-IDs1/3/6/12. Gesamtlänge/Einstecktiefe ist nichtEndflächenhöhe. TatsächlicheGeometrie vermessen undinSoftware hinterlegen; keinevollständigeFertigungszeichnung alleinausdenParametern behaupten.''',
        'PCB extern': '''**Keine Gerber/Schaltpläne/elektronischen Stücklisten im veröffentlichten Hardware-Verzeichnis gefunden.** STEP enthält äußerePlattenkörper, keine Leiterbahnen. Betroffen: vierPrüfspitzen-PCBs, einMultiplexer, eventuell24KanäleSensorinterface und der inSoftware konfigurierteZielversorgungscontroller. Platinen undBestückung sind eigeneZeilen; CAD-082 alsDummy wirdnichtnochmals bestellt. CAD-Stecker/Federkontakte nicht nochmals inPCBA-Budget aufnehmen.

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
