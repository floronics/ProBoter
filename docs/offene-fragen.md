# Offene Fragen

Sammelstelle für Fragen an SCHUTZWERK, die Werkstatt und andere Ansprechpartner.
Beantwortete Fragen mit Antwort und Datum unten unter **Erledigt** ablegen.

Status: `offen` · `gefragt` (wartet auf Antwort) · `erledigt`

## SCHUTZWERK

| # | Frage | Kontext | Status | Datum |
|---|-------|---------|--------|-------|
| S1 | Aus welchem Material ist die Schubladenplatte gefertigt? | Werkstoff (und ggf. Dicke/Oberfläche) für Nachbau bzw. BOM | offen | 2026-10-26 |
| S2 | Wie wurde der PCB Holder gefertigt? | Fertigungsverfahren (Fräsen, 3D-Druck, Laser …) und Material für Nachbau | offen | 2026-10-26 |
| S3 | Wie sieht die Endenbearbeitung der Trapezspindel TR10x2 aus, und hat das Spindelende eine Nut für den Sicherungsring DIN 471 D6 (BOM Pos. 52)? | Spindelende vermutlich auf Ø6 abgedreht für Lager 626-2RS und Kupplung D5/D6; Zeichnung/Maße der Ringnut erfragen, sonst muss die Werkstatt einstechen. Hängt von S4 ab: entfällt, falls die Spindelteile veraltet sind | offen | 2026-10-27 |
| S4 | Sind die Spindel-Angaben für X/Y in der BOM veraltet? Konkret: Wendelkupplungen (Pos. 15, 24), Lagerbock (Pos. 17), Trapezmuttern und TR10x2-Spindel – können diese Positionen gestrichen werden? | Die SCHUTZWERK-Liste beschreibt noch eine ältere Version mit Trapezspindeln. Im CAD ist keins dieser Spindelteile vorhanden; es gibt nur den gedruckten Adapter `TR10x2_GT2_belt_adapter`, an dem statt einer Spindelmutter der Riemen angreift. Das CAD ist also auf Riemen umgebaut, die Liste nicht. | offen | 2026-10-27 |
| S5 | Welche Prüfspitzen (Federkontaktstifte) und welche Aufnahmehülsen setzt ihr ein (Hersteller, Typ, Teilenummer, Spitzenform)? | CAD zeigt `z_pogo_pin` (31,8 mm lang, Schaft Ø1,0, Plunger Ø0,73, 15°-Kegel) und `plug_sleeve_P75-2_W` (25,4 mm, Außen Ø1,2, Anschluss Ø0,6). Das sieht nach P75 (75 mil) aus; Herstellerbezeichnung, Spitzenform (Krone, Nadel, Tulpe), Federkraft und Hub stehen nirgends. Ohne die Angabe lässt sich der BOM-Posten "Probespitze" nicht bestellen | offen | 2026-10-27 |
| S6 | Gibt es Fertigungsdaten (Gerber, KiCad/Altium-Projekt, Schaltplan) für das Probe-PCB `probe_tip_pcb`, und wie ist es aufgebaut? | Im CAD ist es nur ein Umriss ohne Bohrungen und Leiterbahnen (1,6 mm dick, ca. 27 mm lang, Spitze 3 mm breit). Unklar: Lagenaufbau, Pads für Hülse und MMCX-Stecker, Leitungsführung (Impedanz/Schirmung), Kupfer- und Oberflächenwahl, ob es eine Bestückung gibt. Zusätzlich: Welches Kabel (BOM "Kabel Probe") verbindet MMCX an der Spitze mit den SMA-Buchsen im Signal-Multiplexer? | offen | 2026-10-27 |
| S7 | Wo habt ihr die Stahlplatten lasern lassen? | Für die Dokumentation, damit Nachbauer einen Fertiger empfohlen bekommen | offen | 2026-10-27 |

## Werkstatt (Hochschule)

| # | Frage | Kontext | Status | Datum |
|---|-------|---------|--------|-------|
| W1 | Können die Motorplatten in der Werkstatt gefertigt werden? | Material, Stückzahl und Zeichnungen aus dem SCHUTZWERK-CAD mitbringen; Lieferzeit und Kosten klären | offen | 2026-10-26 |

## Sonstige

| # | Frage | Ansprechpartner | Status | Datum |
|---|-------|-----------------|--------|-------|
|   |       |                 |        |       |

## Erledigt

| # | Frage | Antwort | Datum |
|---|-------|---------|-------|
|   |       |         |       |
