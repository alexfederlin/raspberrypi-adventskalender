# raspberrypi-adventskalender
Ein Raspi Adventskalender bei dem am Ende eine kleine Anzeige für Wetter rauskommt. Dieses Projekt vereint Programmierung, Elektronik und 3D Druck in 24 kindgerechten Kleinprojekten.  

# 🤖 Adventskalender: Programmierbare Wetter- und Nachrichtenstation

## 🌟 Thema & Projektziel

Dieses Projekt ist ein **Technik-Adventskalender** über 24 Tage, der speziell für einen 10-Jährigen konzipiert wurde, der bereits Zugang zu einem **Raspberry Pi** und einem **3D-Drucker** hat. **Löten wird bewusst vermieden**; der Fokus liegt auf **Programmierung (Python), Steck-Elektronik (Breadboard) und Hardware-Integration**.

**Das fertige Endprodukt am 24. Dezember ist eine voll funktionsfähige, kompakte Wetter- und Nachrichtenstation**, die:
* Lokale Daten (Temperatur, Luftfeuchtigkeit, Helligkeit) über Sensoren erfasst.
* Online-Daten (Wettervorhersage, aktuelle Nachrichten) über APIs abruft.
* Alle Informationen auf einem kleinen Display anzeigt.
* In einem selbst entworfenen, 3D-gedruckten Gehäuse verbaut ist.

## 📁 Repository-Struktur

| Ordner | Beschreibung |
| :--- | :--- |
| `00_Teileliste/` | Die gesamte Liste der benötigten Hardware-Komponenten. |
| `01_Anleitungen/` | 24 detaillierte, tägliche Anleitungen für den Aufbau und das Programmieren. |
| `02_Code/` | Python-Code-Snippets für jeden Tag sowie das finale Gesamt-Skript. |
| `03_3D_Druck/` | STL-Dateien für das Gehäuse und Halterungen. |
| `04_Verpackung_Printables/` | Vorlagen (PDF) zum Ausdrucken und Basteln der 24 Geschenkschachteln. |

---

## 🗓️ Inhaltsübersicht (24 Tage in 4 Phasen)

### Phase 1: Die Grundlagen & Erste Schritte mit Pi (Tage 1–6)

* **Schwerpunkte:** Betriebssystem-Setup, erste Python-Skripte, Grundlagen der GPIO-Steuerung, LED (Ausgang) und Taster (Eingang).

### Phase 2: Sensoren & Daten erfassen (Tage 7–12)

* **Schwerpunkte:** Anschließen und Programmieren des Temperatur-/Feuchtigkeitssensors, Lichtsensors, Akustik-Feedback (Piezosummer).

### Phase 3: Das Display & Erste Gehäuse-Teile (Tage 13–18)

* **Schwerpunkte:** Anschließen des I2C-Displays, Programmierung zur Anzeige von Text und Sensorwerten, erste Montage des 3D-gedruckten Gehäuses.

### Phase 4: Online-Daten, 3D-Druck-Projekt & Finale (Tage 19–24)

* **Schwerpunkte:** Start eines persönlichen 3D-Druck-Projekts, Abruf von externen APIs (Wetter und Nachrichten-Ticker), Finale Montage, Auto-Start des Programms.

# 🗓️ Detaillierte Übersicht: Türcheninhalt und Lernziel

Die täglichen Aufgaben sind so konzipiert, dass sie **jeweils ca. 20–30 Minuten** in Anspruch nehmen und direkt auf den Lerninhalten des Vortages aufbauen.

| Tag | Phase | Thema/Ziel | Inhalt des Türchens (Hardware/Code) | Lernschwerpunkt |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **I** | **Start & Pi-Vorbereitung** 🚀 | Micro-SD-Karte (mit vorinstalliertem OS) | System-Setup, WLAN-Verbindung |
| **2** | **I** | **Erster Programmcode** 💻 | Git Repo mit Code-Vorlagen clonen | Python-Grundlagen, Code ausführen |
| **3** | **I** | **Breadboard-Grundlagen** 📌 | Breadboard und 5 Jumper-Kabel (M/F) | GPIO-Pins, Schaltkreis-Grundlagen |
| **4** | **I** | **Erste LED schalten** 🔴 | Rote LED und 220 Ohm Widerstand | Digitaler Ausgang, Stromkreis schließen |
| **5** | **I** | **LED blinken lassen** ✨ | Anleitung zum Code-Update (`time.sleep()`) | Programmablaufsteuerung, Timing |
| **6** | **I** | **Taster-Input** 👆 | Taster und 10 kOhm Widerstand | Digitaler Eingang, Interrupts |
| --- | --- | --- | --- | --- |
| **7** | **II** | **Temperatursensor I** 🌡️ | Temperatur-/Feuchtesensor **DHT11/BME280** und Kabel | Datenblatt lesen, serielle Kommunikation |
| **8** | **II** | **Sensor-Code integrieren** | Code-Snippets zum Auslesen des Sensors | Externe Bibliotheken verwenden |
| **9** | **II** | **Umgebungslicht-Sensor** 💡 | Fotowiderstand (LDR) + 10 kOhm Widerstand | Analoge Werte digital messen (Spannungsteiler) |
| **10** | **II** | **Anzeigemodi umschalten** 🔩 | Taster bestimmt welcher Sensorwert angezeigt wird | Funktionen steuern |
| **11** | **II** | **Ein Summer für Alarme** 📢 | Aktiver Piezosummer und Jumper-Kabel | Akustischer Ausgang, Feedback-Systeme |
| **12** | **II** | **Dashboard** | Code-Update: Alle Sensorwerte abfragen und zwischen Anzeigen umschalten | Kombination aller Sensoren |
| --- | --- | --- | --- | --- |
| **13** | **III** | **Display anschließen** 📺 | Kleines **OLED/LCD Display** (128x64, I2C) anschlißen und "Hello World"| Neue Hardware-Schnittstelle I2C |
| **14** | **III** | **Display-Code I (Werte)** | Code-Update: Sensorwerte auf dem Display anzeigen | Variablen-Management, Datenformatierung |
| **15** | **III** | **Display-Code II (Dashboard)** | Code-Update: Sensorwerte auf dem Display anzeigen und umschalten |  |
| **16** | **III** | **Alarm System** |  |
| **16** | **IV** | **Internet-Daten I (Uhrzeit)** 🌐 | Anleitung zur **API-Bibliothek** (`requests`) | Netzwerkprogrammierung, HTTP-Anfragen |
| **18** | **IV** | **Internet-Daten II (Wetter)** 🌤️ | Open-Meteo  | JSON-Daten parsen, externe Daten nutzen |
| **17** | **III** | **Gehäuse-Teil I** 📦 | Der **3D-gedruckte Boden** des Gehäuses | Funktionale Gehäuse-Elemente |
| **18** | **III** | **Gehäuse-Teil II** 🖼️ | Die **3D-gedruckte Display-Fassung/Frontplatte** | Modulares Bauen, Hardware-Integration |
| --- | --- | --- | --- | --- |
| **19** | **IV** | **3D-Druck Projekt-Tag** 🌈 | **Neue Rolle Filament** (z.B. Leucht-PLA) | Design-Ideen, Slicing-Software (optional) |

| **22** | **IV** | **Nachrichten-Ticker** 📰 | Code-Snippets für **RSS-Parsing** | Datenstrukturierung (XML/RSS), Text-Scrolling |
| **23** | **IV** | **Finale Gehäuse-Montage** 🛠️ | Der **3D-gedruckte Gehäuse-Deckel** + restliche Schrauben | Endgültiger Zusammenbau, Kabelmanagement |
| **24** | **IV** | **Das fertige Produkt!** 🎉 | End-Anleitung zur **Startautomatik** | Systemkonfiguration, Produktiv-Einsatz |

Display ideen
https://www.printables.com/model/588251-091-oled-display-stand