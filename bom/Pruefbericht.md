# Prüfung des Beschaffungsstands

**16.10.2026 – Dokumenten- und Rechenprüfung, keine physische Erprobung.**

| Prüfung | Ergebnis |
|---|---|
| STEP-Abdeckung | Alle 120 Blattteil-IDs genau einmal zugeordnet; 1.066 ursprüngliche Vorkommen erhalten |
| Fusion-Abgleich | 1.054 Blattvorkommen; fehlende 12 NEMA17 bleiben im Bedarf |
| Gesamtinventur | 160 Positionen: 120 CAD + 40 System-/Abgrenzungspositionen |
| Bestellrechnung | 104 Zeilen, darunter 3 separate Optionen/Vergleiche; diese sind nicht im Grundtotal |
| Unbekannte Kosten | 24 Zeilen ohne Preis; weder als null noch als vollständiger Baupreis dargestellt |
| Kostenbesitzer | Jedes benötigte Teil einem Posten zugewiesen; Druckmaterial, CNC-Material, Riemen und Führungssätze nicht doppelt gerechnet |
| Mengen/Steuern | 11 automatisierte Tests erfolgreich, einschließlich wiederverwendeter STEP-Baugruppen, Packungsrundung, Nettopreisen und Alternativenausschluss |
| Lokale Dokumentlinks | Keine fehlenden Linkziele in `bom/*.md` und `docs/*.md` gefunden |
| Quelldatei | SHA256 der STEP-Datei stimmt mit `evidence/manifest.json` überein |
| Formatprüfung | `git diff --check` ohne Whitespace-Fehler |

## Zahlenstand

- Beobachtete Webpreise bei Planmengen einschließlich Kandidaten und bestimmbarer Fracht: **817,03 € brutto / 686,58 € netto**.
- Zusätzliche eigene Schätzungen: **5.012,10 € brutto / 4.211,82 € netto**.
- Vorläufiger Gesamtbedarf des bezifferten Umfangs: **5.829,13 € brutto / 4.898,40 € netto**.
- Davon eindeutig identifizierte und mit Bezugsquelle versehene Teile: Netzteil und SHF10-Halter, **104,90 € brutto**; Halterliefertermin beachten.

## Grenzen

Keine vollständige Original-BOM, keine freigegebenen Fertigungszeichnungen,
keine Slicerprüfung, keine Lieferantenangebote für CNC/PCB und keine praktische
Kompatibilitätsprüfung der Ersatzkandidaten. Materialien, Passungen, manche
Planmengen und die Elektronikentwicklung bleiben wie in den Listen markiert offen.
Die Tests belegen die Konsistenz der dokumentierten Planung, nicht die Vollständigkeit
aller erst bei Konstruktion und Montage erkennbaren Kleinteile.

[Rechenweg](Reproduktion.md) · [Offene Positionen](Ungeklaert.md) · [Bestellliste](Bestellliste.md)
