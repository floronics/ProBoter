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
SHEET = ids(3,7,8,9,24,26,96,97,99,100,119,120)
CNC = ids(16,17,18,19)
STOCK = ids(11,12,13,14,20,69,70,93,94,98,103,108,109)
PCB = ids(75)
UNIDENTIFIED = ids(10,55,61,62,73,86,115)
EXCLUDED = ids(66,82)
NORM = ids(*range(28,49),56,57,58)

# id -> (precise description, open question / evidence, preferred supplier)
DETAIL = {
23: ('BIGTREETECH SKR V1.3 Steuerplatine', 'Originalmodell laut CAD/Firmware; kein belastbarer neuer EU-Lagerbestand gefunden. Ersatzboard benötigt Firmware-/Pin- und Halteranpassung.', 'RBS'),
27: ('CPC MR12ML Führungswagen', '8 Wagen für2×600-mm-Schienen. Aktueller Katalog47,8mm Länge, CAD47,6mm; Vorspannung, Genauigkeit und Paarung klären.', 'CPC'),
49: ('igus E2i.10.10.028.0, 16 kurze Abschnitte', 'Nominell16×0,24m=3,84m. Gliederraster, Verfahrweg und Endstücke prüfen;1m-Einkaufseinheiten sind keine16 ganzen Ketten.', 'TME'),
50: ('igus E2i.10.20.028.0, 8 lange Abschnitte', 'Nominell8×0,28m=2,24m. Drei1m-Einheiten ergeben rechnerisch9 Abschnitte; Teilung und Endstücke bestätigen.', 'IGUS'),
51: ('Schubladengriff, Lochabstand vermutlich100mm', 'CAD113×20×49mm; Lochabstand, Gewinde und genaue DOLD-Artikelnummer bestimmen.', 'DOLD'),
52: ('Gelenkfuß M6 / TellerØ40mm', 'CAD40×40×30,4mm; Gewindelänge, Schwenkbereich und Traglast festlegen.', 'DOLD'),
53: ('HIWIN MGNR12R150HM, Z-Schiene150mm', 'Originalname; aktuelle Suffixe, Endlochabstände und Paarung mitCAD-054 bestätigen.', 'HIWIN'),
54: ('HIWIN MGN12CZ0H Z-Führungswagen', 'Originalname; vier passende Wagen zuCAD-053, keine ungeprüfte Mischung mit Nachbauten.', 'HIWIN'),
55: ('Induktiver Näherungsschalter M8, Bauhülle60mm', '24 CAD-Vorkommen. MPN, Schaltabstand, NPN/PNP, NO/NC, Versorgung, Pegel und Kabellänge fehlen.24V nicht direkt an SKR-Eingänge; InterfaceCAD-unabhängig SYS-019.', 'TME'),
59: ('Mean Well MHS012 Montagewinkel', '4 Winkel,19×16×15mm. TME identifiziert;0,09EUR aus italienischer Indexseite nicht als bestätigter DE-Preis übernommen.', 'TME'),
60: ('Mean Well RSP-200-24 Netzteil,24V/8,4A', 'Originalmodell,215×115×30mm. Lastbilanz, Absicherung, Berührungsschutz und Schutzleiter separat.', 'REICHELT'),
61: ('MMCX-Stecker gerade / Messleitung', '4 CAD-Modelle enthalten Kabelansätze. Impedanz, Kabeltyp, Crimp/Lötanschluss, Gegenstecker und Länge unbekannt.', 'TME'),
62: ('MMCX-Stecker gewinkelt / Messleitung', '4 CAD-Modelle; Kabel-/Buchsenpaarung mitCAD-061/075 und Multiplexer offen.', 'TME'),
63: ('Nanotec ST3518M1004-A NEMA14 Z-Motor', 'Plan4 statt8 CAD: paarweise überlagerte Einbaulagen, je Probe ein Z-Antrieb. Hypothese vor Bau prüfen. Archivmodell, Ersatzpassung offen.', 'NANOTEC'),
64: ('Nanotec ST4118M1804-A NEMA17 X/Y-Motor', '12 laut STEP:8 X +4 Y. Alle12 im Fusion-Import fehlend. Hersteller nennt Modell; Anschluss und aktuelle Verfügbarkeit bestätigen.', 'NANOTEC'),
65: ('Optischer Endschalter11×35mm', '4 Stück, Kandidat mit1m-Kabel. Lochabstand28mm, Schlitzlage, Pinout, Versorgung und Schaltpegel abgleichen.', 'RBS'),
73: ('Prüfkontakt-Hülse P75-2 W', '8 Stück, CADØ1,2×25,4mm. Hersteller und passender FederkontaktCAD-115 unklar; Kontaktpaar vollständig spezifizieren.', 'TME'),
75: ('Prüfspitzen-PCB, unbestückt', '4 Stück;26,67×10,96×1,6mm Hülle. Schaltplan, Kupfer, Bohrungen, Gerber und Bestückungsdaten fehlen. Bestückung SYS-024 separat.', 'BETA'),
76: ('Umlenkrolle9mm / außenØ18 / BohrungØ5', 'CAD-Zylinder belegenØ5 undØ18, Breite11mm. DOLD64396 Kandidat; Lager, Lauffläche und axiale Passung prüfen.', 'DOLD'),
77: ('GT2-Antriebsriemenscheibe Z16 / 6mm / Bohrung5mm', '12 X/Y-Antriebe. Bore5 durch CAD-Zylinder bestätigt; Bundlänge14,1mm und Madenschrauben prüfen.', 'RBS'),
78: ('GT2-Umlenkrolle Z16 / 6mm / Bohrung3mm', '20 Stück, CADØ13×8,5mm mitØ3-Bohrung. Lager-/Distanzscheiben und Artikel46132 axial abgleichen.', 'DOLD'),
79: ('SHF10 Flanschhalter fürØ10mm Welle', '16 Stück.43×24×10mm undØ5,5-Befestigung stimmen mitDOLD11260 überein. Liefertermin27.11.2026 angekündigt.', 'DOLD'),
80: ('Lineargleitbuchse10×19×29mm', 'CAD-Name l19 irreführend:19 ist Außendurchmesser, Länge29mm. igus RJ4JP-01-10 Kandidat; Werkstoff, Spiel und zulässige Welle prüfen.', 'DOLD'),
81: ('Anschraubwinkel30 / Nut6', '26 Stück; CAD28×28×28mm. Profilserie I/B, Schraubenset und Lochbild offen.', 'DOLD'),
84: ('Teleskopschiene TSAA514613-350', '2 Einzelschienen im CAD, nicht2Paare.350×45,5×12,7mm; Hersteller, Auszug, Rastung und Last klären.', 'DOLD'),
85: ('Bewegliches USB-Mikroskop', 'Plan1 laut Hardware-Blog,4CAD. Weitere3 optional. Originalmodell unbekannt; Kandidat muss100mm Arbeitsabstand/ca30×40mm Bildfeld und Linux-UVC erfüllen.', 'REICHELT'),
86: ('Bedientaster/-schalterØ19mm', 'Schaltfunktion rastend/tastend, Kontaktlast, Beleuchtung und Zuordnung zu Versorgung/Software unbekannt.', 'REICHELT'),
87: ('GT2-Riemen X,6mm breit', '8 Verläufe.710,3mm Hülllänge ist NICHT Riemenlänge. Vorläufig gemeinsamer20m-Ansatz fürX/Y; offene/geschlossene Bauform klären.', 'DOLD'),
95: ('CPC MR12M Führungsschiene600mm', '2 Stück600×12×7,5mm. Endlochabstand, Genauigkeit, Material und passende8Wagen bestimmen.', 'CPC'),
104: ('GT2-Riemen Y,6mm breit', '4 Verläufe.503,3mm Hülllänge ist NICHT Riemenlänge; Einkauf gemeinsam mitCAD-087, nicht doppelt rechnen.', 'DOLD'),
113: ('GT2-Riemen Z,9mm breit', '4 Verläufe;119,3mm Hülllänge ist NICHT Riemenlänge.2m Budgetvorschlag; Gates LL2GT RF9mm Bezugsfamilie, Ausführung prüfen.', 'RBS'),
115: ('Federkontakt der Prüfspitze', '8 Stück, CADØ1×16,6mm. Spitzenform, Hub, Federkraft, Kontaktmaterial und Paarung mitP75-2-W unklar.', 'TME'),
}

# Explicit non-CAD system inventory. Quantities are planning values, not discoveries.
# key, description, quantity, unit, group, supplier, specification/gap, source
SYSTEM = [
('001','TMC2130 SPI Treibermodule',16,'Stück','Kaufteile','RBS','4 je SKR fürX/X2/Y/Z; Kühlkörper/Jumper im Lieferumfang prüfen.',FIRMWARE),
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
('027','Energieketten-Endanschlüsse schmal',16,'Paare','Kaufteile','IGUS','Je kurzerKette1bewegliches+1festesEnde. E2i.10.10 passendeMPN ermitteln; Lieferumfang und CAD-Dreikörpermodell prüfen.',CAD),
('028','Energieketten-Endanschlüsse breit',8,'Paare','Kaufteile','IGUS','Je langerKette1Paar passendE2i.10.20; keine Endstücke doppelt kaufen, falls enthalten.',CAD),
('029','Profil-Nutensteine und Zusatzbefestigung',1,'Satz','Kaufteile','DOLD','Nut6/Profilserie klären; 26Winkel plus Halter. CAD-Vierkantmuttern29/30 und mitgelieferte Winkelsätze abziehen.',CAD),
('030','Scheiben, Sicherungselemente, Distanzteile',1,'Satz','Kaufteile','SCHRAUBEN','Ergänzungsbedarf je Verschraubung/Idler; CAD-Normteile und Sensor-Beipack abziehen. Stückzahlen noch offen.',CAD),
('031','Lötzinn, Schrumpfschlauch, Binder, Labels, Kleber',1,'Satz','Kaufteile','REICHELT','Verbrauchsmaterialbudget; vorhandene Bestände später abziehen. Werkzeuge nicht enthalten.',CAD),
('032','Controller-Befestigung und Kühlung',1,'Satz','Kaufteile','RBS','Abstandshalter, Isolierung, ggf.Lüfter; SKR/TMC-Beipack und thermische Auslegung prüfen.',FIRMWARE),
('033','Zusätzliche bewegliche Kameras',3,'Stück','Optional','REICHELT','Optional zur Vollbestückung aller4CAD-Halter; zusätzliche USB-Ports/Bandbreite/Kabel separat dimensionieren.',CAD),
('034','Host-PC, Messgeräte und Werkzeuge',1,'Bestand','Nicht benötigt','OFFEN','Vom Käufer vorhanden; Kosten ausgeschlossen. Software nennt PicoScopePS5000a; bestehendes Gerät/Hostkompatibilität prüfen.',SOFTWARE),
('035','Z-Antriebsriemenscheibe / integrierter Adapter',4,'Stück','Ungeklärte Teile','DOLD','16Zähne laut Firmware,9mmZ-Riemen. Prüfen, obCAD-001/002 das Antriebsrad bereits integriert; gegebenenfalls kein separater Kauf.',FIRMWARE),
('036','USB-/Versorgungsanschlüsse der Kalibrierung',1,'Prüfung','Nicht benötigt','OFFEN','Passive Referenzplatte benötigt nach veröffentlichtem Konzept keine eigene USB-Elektronik; kein zusätzliches Gerät.',BLOG),
('037','Weiße äußere Kalibrierreferenzen',4,'Stück','Weitere Fertigung','OFFEN','ReferenceBoardConfig beschreibt vier äußere weiße Referenzpins. Raster109,9×89,8mm; Durchmesser, Höhe, Material und Umsetzung am gewählten Board fehlen. Nicht mit12Messingpins gleichsetzen.','../software/hardware-control/proboter/model/reference_board_config.py'),
('038','Kalibrier-Kontaktleitungen und gemeinsame Messreferenz',1,'Satz','Kaufteile','TME','4SKR-Zentriereingänge P0_17 mitPull-up/aktivLow sowie Referenzkörper/Kontaktkreis verdrahten. Netzplan, Stecker, Länge undBezugspotenzial mitMultiplexer klären; keineVerbindung ungeprüft festlegen.','../firmware/Marlin/src/module/proboter.cpp'),
('039','Erhöhte Messing-Referenzzylinder',4,'Stück','Weitere Fertigung','DOLD','Ø7mm lautReferenceBoard-Skizze; Code setzt vierEndflächen6/8/10/12mm über Bezugsebene aufRaster59,6×39,9mm. Gesamtlängen undEinstecktiefe sindnichtdieseHöhen; Zeichnung undToleranzen fehlen.','../software/hardware-control/proboter/tasks/utils/reference_board.py'),
('040','Äußere flache Messing-Referenzzylinder',4,'Stück','Weitere Fertigung','DOLD','Ø7mm lautReferenceBoard-Skizze; Mittelpunkte(±54,95;0) und(0;±44,9)mm. Endflächen aufBezugsebene; Länge undMontage offen. Insgesamt12Messingzylinder plus4weißeReferenzen.','../software/hardware-control/proboter/tasks/utils/reference_board.py'),
]

def make_parts():
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
        if key in CNC:
            group, supplier, status = 'CNC extern','XOMETRY','Fertigung noch offen'
            material, process_evidence = 'EN AW-6082 T6 vorgeschlagen', 'CNC-Fräsen vorgeschlagen; Originalverfahren nicht belegt'
            note = '10mm Plattenhülle. Material, Nullpunkte, Loch-/Gewindetabelle, Passungen, Ebenheit und Oberflächen festlegen; STEP allein reicht nicht zur Funktionsfreigabe.'
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
            material = 'Festigkeitsklasse/Material nicht belegt; Stahl8.8 für Schrauben nur Vorschlag'
            note = 'Norm/Größe aus CAD; Material, Festigkeit, Oberflächen und tatsächliche Packung vor Kauf bestätigen.'
            supplier = 'SCHRAUBEN'
            if key in ids(56,57,58):
                note += ' ISO8673 bezeichnet Feingewinde abM8 (ISO8673:2012/2023). NamenM3/M4 widersprechen dem Normumfang. TatsächlicheSteigung gegenSchrauben/Sensor prüfen; nicht ungeprüftRegelgewinde bestellen.'
            if key=='CAD-058':
                note += ' 48M8-Muttern könnten als2jeSensor bereits enthalten sein; Kosten nicht doppelt ansetzen.'
        quantity = int(g['step_qty'])
        if key=='CAD-063': quantity=4
        if key=='CAD-085': quantity=1
        if key in EXCLUDED: quantity=0
        if key in ids(60,79): status='bestellfähig'
        if key=='CAD-080': title='GleitbuchseØ10 innen / Ø19 außen / Länge29mm'
        if key=='CAD-010':
            note='Schubladen-Dummy564×410×12mm: unklar, ob reale Platte benötigt und welches Material. Nicht stillschweigend ausschließen oder aus Stahl fertigen.'
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
    def add(key, title, part_ids, need, unit='Stück', offer=None, estimate=None, pack=1,
            supplier=None, note='', optional=False, source=None, basis='gross', spec=''):
        assert all(i in byid for i in part_ids),part_ids
        o=offers.get(offer,{})
        sup=supplier or o.get('supplier') or byid[part_ids[0]]['supplier']
        price=o.get('price') if offer else estimate
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
                 price_kind='Webpreis' if offer else ('Schätzung' if estimate is not None else 'offen'),
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
    add('BUY-005','20Umlenkrollen6mm',ids(78),20,offer='O-005')
    add('BUY-006','8Umlenkrollen9mm, Kandidat',ids(76),8,offer='O-006')
    add('BUY-007','X/Y-Riemen6mm,2Rollen à10m',ids(87,104),20,unit='m',offer='O-007',note='Eigene Mengenreserve:8×ca1,45m +4×ca1,03m =15,72m; auf20m gerundet. Kein bestätigter Zuschnittplan.')
    add('BUY-008','KurzeEnergieketten,4×1m',ids(49),D('3.84'),unit='m',offer='O-008',note='Schnittplan4×0,24m je1m; Gliederraster noch prüfen, keine Lieferfähigkeit für4m bestätigt.')
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
    add('BUD-001','12NEMA17Originalmotoren',ids(64),12,estimate='60',basis='net',note='Eigener Budgetansatz60EUR netto/Motor; kein Nanotec-Angebot.')
    add('BUD-002','4NEMA14Z-Motoren',ids(63),4,estimate='50',basis='net',source='https://www.nanotec.com/eu/de/downloads/archiv',note='Eigener Budgetansatz50EUR netto; Originalarchivteil bzw.Ersatz und Mengenhypothese noch offen.')
    add('BUD-003','4SteuerplatinenSKR1.3oderMigration',ids(23),4,estimate='50',basis='net',note='Budget50EUR netto; keine bestätigteEU-Quelle fürOriginal. Ersatzmigration nicht enthalten.')
    add('BUD-004','CPCSchienen/Wagen alsabgestimmterSatz',ids(27,95),1,unit='Satz',estimate='500',basis='net',supplier='CPC',note='Eigene grobe Reserve für2×600mm+8Wagen; kein Angebot. ALT-001 nicht hinzurechnen.')
    add('BUD-005','HIWINZ-Führungen als4Paare',ids(53,54),4,unit='Paare',estimate='80',basis='net',supplier='HIWIN',note='Eigener Budgetansatz80EUR netto je150mm-Schiene+Wagen. ALT-002 nicht hinzurechnen.')
    add('BUD-006','igusRJ4JP-01-10Kandidat',ids(80),16,estimate='4',source='https://www.dold-mechatronik.de/drylin-R-Lineargleitbuchse-RJ4JP-01',note='4EUR brutto Budget jeBuchse; Varianten-Abpreis nicht als konkreter Preis verwendet.')
    add('BUD-007','LangeEnergiekette',ids(50),D('2.24'),unit='m',estimate='40',supplier='IGUS',note='Budget40EUR brutto je1m,3Bestelleinheiten; Abschnittsteilung prüfen.')
    add('BUD-008','Z-Riemen9mm',ids(113),2,unit='m',estimate='8',supplier='RBS',source='https://www.roboter-bausatz.de/p/1-meter-gt2-zahnriemen-gates-ll2gt-rf-9mm',note='8EUR brutto/m ist eigene Schätzung.2m Reserve für4Verläufe, kein gemessener Zuschnitt.')
    for n,price in [(51,'10'),(52,'5'),(59,'1'),(81,'3'),(84,'20')]:
        p=byid[f'CAD-{n:03}']
        add(f'BUD-C{n:03}',p['name'],[p['id']],p['quantity'],estimate=price,note='Eigener Brutto-Budgetansatz; genaue Shopvariante/Packung noch offen.')
    for key in NORM:
        if key=='CAD-058': continue # Possibly included with sensors; deliberately unpriced.
        p=byid[key]
        price='0.80' if key=='CAD-028' else ('0.30' if key in ids(29,30,32,33,34,45,46,47) else '0.15')
        add('N-'+key[-3:],p['name'],[key],p['quantity'],estimate=str(D(price)*10),pack=10,
            note=f'Eigene Schätzung{price}EUR brutto/Stück; Rechenpackung10 als Planung, tatsächliche Mindestmenge/Verfügbarkeit nicht bestätigt. Keine Materialfreigabe.')
    profiles=ids(11,12,13,20)
    add('MAT-002','30×30Nut6Aluprofil inklusiveSchnittreserve',profiles,8,unit='m',estimate='12',
        source='https://www.dold-mechatronik.de/Aluminum-profile-30x30-L-I-type-slot-6-light-silver-Alu',
        note='Eigener Budgetansatz12EUR brutto/m. Nettolängen7,098m;2×564+3×590+12×350mm.8mMaterialansatz, Lieferstangen/Schnittplan und Zusatzbearbeitung offen.')
    add('MAT-003','60×30Nut6Aluprofil',ids(14),D('1.4'),unit='m',estimate='2.50',pack=D('.1'),note='Eigener Budgetansatz25EUR brutto/m, Recheneinheit0,1m;2×650mm netto,1,4m mitReserve. Kein bestätigtesSchnittangebot.')
    add('MAT-004','PräzisionswellenØ10 inklusiveZuschnitt',ids(69,98),5,unit='m',estimate='25',note='CF53h6 vorgeschlagen;8×450+2×356,8=4,3136m netto.5mBudget à25EUR brutto; Schnittverteilung, Härte und Buchsenpaarung prüfen.')
    add('MAT-005','Versteifungsprofile40×16 undHalte-/Distanzstäbe',ids(70,93,94,103,108,109),1,unit='Los',estimate='100',note='Eigenes100EUR-Bruttobudget fürProfile4×436mm, Rechteck2×205mm, Ø8Trigger4×125+4×75mm, Ø4Stäbe8×70mm und4Distanzteile. Material/Profile noch klären.')
    add('MAT-006','Blechrohmaterial undVerschnitt',[p['id'] for p in parts if p['group']=='Blech intern'],1,unit='Los',estimate='200',note='Eigener200EUR-Bruttobudgettopf für3/5mmPlatten und noch nicht abgewickelteTeile. Kein Händlerangebot; Material/Flachzuschnitte noch nicht bestellfähig. InterneArbeits-/Maschinenzeit ausgeschlossen.')
    add('FAB-001','8AdapterplattenCNC extern',CNC,8,estimate='100',basis='net',supplier='XOMETRY',note='Eigene grobe Schätzung100EUR netto/Teil inklusiveRohmaterial. Kein Fertigungsangebot, kein Material zusätzlich kalkulieren. Zeichnungen undEU-Fertigungsort offen.')
    for key,amount in [('008','30'),('011','20'),('012','15'),('013','15'),('014','64'),('015','25'),('018','60'),('020','35'),('021','15'),('022','60'),('025','20'),('027','48'),('028','32'),('029','35'),('030','20'),('031','35'),('032','30')]:
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
    print(json.dumps(totals,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
