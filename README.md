# PROBoter - A platform for automated embedded system security analysis

## Floronics-Nachbau

Dieser Fork von [SCHUTZWERK/PROBoter](https://github.com/schutzwerk/PROBoter)
sammelt unsere Unterlagen für einen nachvollziehbaren Nachbau. Die
[Bestellliste](bom/Bestellliste.md) ist ein **Arbeitsstand ohne Bestellfreigabe**:
Das CAD-Modell enthält Platzhalter und widerspricht teilweise dem beschriebenen
Aufbau mit vier Prüfeinheiten. Offene Positionen sind ausdrücklich markiert.

| Unterlage | Inhalt |
|---|---|
| [Nachbau-Übersicht](docs/Floronics-Nachbau.md) | Struktur, Herkunft und nächster Schritt |
| [Quellen](docs/Quellen.md) | Öffentlich zugängliche Belege und Lizenzhinweise |
| [Aufbau](docs/Aufbau.md) | Mechanik, Elektronik und Software im Überblick |
| [Bestellliste](bom/Bestellliste.md) | Menschenlesbare Beschaffungsplanung |
| [CAD-Teileliste](bom/CAD-Teileliste.md) | Alle 120 benannten Blattteile mit Mengen und Klärstatus |
| [Offene Punkte](docs/Offene-Punkte.md) | Entscheidungen vor Konstruktion und Bestellung |

---

![PROBoter title image](/docs/title.png)

The PROBoter is a hardware and software platform to automate embedded system security analysis. The initial prototype was developed during the master's thesis **Automatisierung der hardwarenahen Sicherheitsanalyse von eingebetteten Systemen** in cooperation with [SCHUTZWERK GmbH](https://www.schutzwerk.com) and
[Hochschule Kempten](https://www.hs-kempten.de) in the context of the [SecForCARs](https://www.secforcars.de) project.

The project consists of various components which can be found in individual subfolders of this repository:

- [firmware](/firmware) Contains the firmware running on the 3D printer boards driving the PROBoter hardware platform.
- [hardware](/hardware) Contains 3D models and construction data of the PROBoter hardware platform.
- [image_data_sets](/image_data_sets) Contains image data sets to train or validate algorithms for IC and pin detection.
- [publications](/publications) Contains publications related to the PROBoter. You can also find citation information here if you want to reference our work in other research publications.
- [software](/software) Contains software components forming the high-level software part of the PROBoter platform.

Most parts of the platform are licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.txt). Detailed license information and used third-party components can be found in the individual subfolders.

Other components will be released soon. Follow the [SCHUTZWERK PROBoter blog post series](https://schutzwerk.com/en/43/posts/proboter_01/) to get updates of the current development status and new component releases. So stay tuned... :)

