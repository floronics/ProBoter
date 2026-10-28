# PROBoter signal multiplexer board

Aktuell schaltet das Board (`mux.kicad_sch`) jeden Eingangskanal (I1–I4, B1–B4) per Relais
(K1–K7, je über NMOS Q1–Q8 vom ATmega328PB angesteuert) wahlweise auf einen von zwei
Oszilloskop-Ausgängen (SCOPE-A / SCOPE-B).

## Konzept (offen, noch nicht umgesetzt): Oszi/Multimeter-Umschaltung pro Probe

Idee: zusätzlich zur Oszi-Umschaltung soll pro (beweglicher) Probe auch zwischen
Oszilloskop und Multimeter umgeschaltet werden können, statt feste Probes pro
Instrument (eine fest fürs Oszi, eine fest für Multimeter+, eine für GND, eine für
Power) zu verwenden.

**Empfohlener Ansatz:** Hybridlösung.
- **GND und Power fest verdrahtet lassen**, nicht mitmultiplexen. Beide werden während
  einer Messung durchgehend gebraucht; ein Umschalten der GND-Referenz mitten in der
  Messung erzeugt Spannungsspitzen bzw. kurzzeitiges Floating.
- **Signal-Probe(s) per Relais zwischen Oszi und Multimeter umschaltbar**, nach
  demselben Muster wie die bestehende SCOPE-A/SCOPE-B-Umschaltung (zusätzliche
  Relais-Stufe/-Bus fürs Multimeter pro Kanal). Das passt zur vorhandenen Architektur
  und erspart getrennte Roboter-Bewegungen/Probes für denselben Testpunkt.

**Zu beachtende Trade-offs:**
- Jede zusätzliche Relais-Stufe im Oszi-Pfad erhöht parasitäre Kapazität und
  Kontaktwiderstand → Bandbreitenverlust beim Oszi. Multimeter-Messungen (meist
  DC/langsam) sind davon kaum betroffen.
- Multimeter sind im Widerstands-/Durchgangs-/Dioden-Modus **aktiv** (speisen Strom
  bzw. Spannung ein), ein Oszi-Eingang ist rein passiv hochohmig. Oszi und Multimeter
  dürfen daher nie gleichzeitig am selben Knoten hängen → Umschaltung muss
  break-before-make sein, sonst drohen Messfehler oder Kurzschlüsse zwischen den
  Instrumenten.
