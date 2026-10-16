# Quellen und Datenlage

**Recherche-Stand: 16.10.2026.** Primärquellen sind das
[Original-Repository](https://github.com/schutzwerk/PROBoter), die
[SCHUTZWERK-Blogserie](https://www.schutzwerk.com/en/blog/proboter-02/)
und die dort verlinkten Veröffentlichungen. Externe Webseiten werden verlinkt,
nicht als Kopien abgelegt. So bleiben Urheberrecht, Aktualisierungen und
Quellenherkunft erkennbar.

## Originaldaten im Repository

| Bereich | Lokaler Pfad | Inhalt und Grenze |
|---|---|---|
| Gesamtdarstellung | [`README.md`](../README.md) | Plattform und Teilprojekte; Originaltext mit Floronics-Einstieg |
| Konstruktion | [`hardware/`](../hardware/) | STEP-Gesamtbaugruppe, Rendering, Lizenzen; keine separaten Fertigungszeichnungen oder Stückliste |
| CAD-Datei | [`proboter.stp`](../hardware/3d_models/proboter.stp) | Solid-Edge-Export vom 19.04.2022; 447 benannte Einbauvorkommen, 416 Blattteil-Vorkommen, 120 Blattteil-Namen |
| CAD-PDF | [`proboter.pdf`](../hardware/3d_models/proboter.pdf) | Bei Prüfung leer gerendert; auch [Upstream-Issue #2](https://github.com/schutzwerk/PROBoter/issues/2) meldet das Problem |
| Firmware | [`firmware/`](../firmware/) | Modifiziertes Marlin für vier SKR-V1.3-Controller, je Probe zu konfigurieren; Firmware-README und Konfiguration |
| Software | [`software/`](../software/) | Docker-Compose, Web-UI, Hardwaresteuerung, Bild-, Signal- und Projektdaten-Dienste |
| Datensätze | [`image_data_sets/`](../image_data_sets/) | Dokumentation und Git-LFS-Zeiger; Originalbilder von PCB-GOOGLE werden aus Lizenzgründen nicht mitgeliefert |
| Forschung | [`publications/`](../publications/) | Abschlussarbeit von Fabian Weber und Verweise/Zitate weiterer Arbeiten |

Der Fork basiert auf dem Originalstand
[`b6184ada8ddee74df746ce800c81038e8d482e1e`](https://github.com/schutzwerk/PROBoter/commit/b6184ada8ddee74df746ce800c81038e8d482e1e)
auf `master`. Im lokalen Klon zeigt `upstream` auf SCHUTZWERK; GitHub führt
`floronics/ProBoter` als Fork des Originals.

## Veröffentlichte Erläuterungen

| Quelle | Nutzen für den Nachbau |
|---|---|
| [Blog Teil I: Konzept](https://www.schutzwerk.com/en/blog/proboter-01/) | Plattformziele, Arbeitsablauf und Funktionen |
| [Blog Teil II: Hardware](https://www.schutzwerk.com/en/blog/proboter-02/) | Vier Prüfeinheiten, Aufbau, Kamera, Multiplexer, Steuerung, Kalibrierung und damaliger Kostenrahmen |
| [Blog Teil III: Visuelle Analyse](https://www.schutzwerk.com/en/blog/proboter-03/) | Bilddatensätze, IC- und Pinerkennung |
| [Blog Teil IV: Signalanalyse](https://www.schutzwerk.com/en/blog/proboter-04/) | Spannungsmessung und Protokollerkennung; Oszilloskop als Messgerät |
| [Blog Teil V: Software](https://www.schutzwerk.com/en/blog/proboter-05/) | Aktuelle veröffentlichte Dienst- und Web-UI-Architektur |
| [PROBoter-Demovideo](https://www.schutzwerk.com/en/blog/proboter-video/) | Sichtprüfung des Funktionsumfangs |
| [Weber, Masterarbeit 2019](../publications/PROBoter_thesis.pdf) | Frühere Zwei-Proben-Variante, Kinematik, Kalibrierung und Prototypkosten |
| [PROBoter-Fachbeitrag 2021](https://doi.org/10.13154/294-8348) | Evaluierung und Systembeschreibung |
| [Weitere Publikationen](../publications/README.md) | Bildanalyse und Busprotokollerkennung |

## Herstellerbelege für ausdrücklich benannte Modelle

- [BIGTREETECH SKR V1.3](https://github.com/bigtreetech/BIGTREETECH-SKR-V1.3)
  bestätigt das Controller-Modell und seine TMC2130-Schnittstelle.
- [Mean Well RSP-200-Datenblatt](https://www.meanwell.com/Upload/PDF/RSP-200/RSP-200-SPEC.PDF)
  enthält die 24-V-Variante RSP-200-24.
- [Nanotec ST4118M1804-A](https://www.nanotec.com/eu/de/produkte/363-st4118m1804-a)
  bestätigt die NEMA-17-Bestellbezeichnung.
- [Nanotec-Archiv](https://www.nanotec.com/eu/de/downloads/archiv) enthält
  ST3518M1004-A; aktuelle Lieferbarkeit ist nicht belegt.
- [CPC-Miniaturführungen](https://cpc-europe.com/cpc-cells/linear-guides/mini-linear-guides/)
  führen MR12ML. Varianten und passende Schienenlänge bleiben offen.
- [igus E2i.10-Serie](https://www.igus.de/product/series-E2i-10?c=DE&l=de)
  bestätigt die Kettenfamilie; die CAD-Namen spezifizieren zwei Breiten/Längen,
  aber keine komplette bestellfertige Konfiguration mit Anschlüssen.

## Grenzen und Lizenzhinweise

- Die Upstream-README nennt GPLv3 für große Teile der Plattform. Für die
  Hardware gelten [`hardware/COPYRIGHT`](../hardware/COPYRIGHT) und
  [`hardware/LICENSE`](../hardware/LICENSE) mit CERN-OHL-W v2.
  Weitere Komponenten enthalten eigene Lizenzdateien. Diese wurden
  unverändert übernommen.
- 16 Dateien sind Git-LFS-Zeiger (zusammen nominell rund 1,4 GB), darunter
  Datensätze und trainierte Modelle. Die großen Inhalte sind nicht Teil der
  normalen Git-Historie; der Fork enthält zunächst dieselben Zeiger wie das
  Original. Der Abruf von `ic-pins.zip` scheiterte bei der Recherche mit
  einem 404 des Upstream-LFS-Servers. Für andere LFS-Objekte wurde die
  Verfügbarkeit nicht einzeln geprüft.
- Es gibt im Original keine separat veröffentlichten KiCad-Schaltpläne,
  Gerber, STL-Dateien oder vollständige Einkaufsstückliste für die
  Multiplexer- und Prüfspitzenplatinen.
- Die Preise von 2019 und 2022 sind historische Angaben, keine aktuellen
  Bestellpreise. Preise und Lagerbestände wurden für diese erste Inventur
  nicht geprüft.

## Öffentliche Upstream-Issues

Bei der Recherche waren zwei Issues offen:
[#1: Installationsfehler mit flask-cors/flask-restx](https://github.com/schutzwerk/PROBoter/issues/1)
und [#2: leeres CAD-PDF](https://github.com/schutzwerk/PROBoter/issues/2).
Die [Hardware-Änderungsdatei](../hardware/CHANGES.txt) verweist
auf GitHub-Releases; die Upstream-Release-Liste war am Recherchedatum leer.
