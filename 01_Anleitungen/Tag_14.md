# 01_Anleitungen/Tag_14_Display_Daten.md

## 📅 Tag 14: Echte Daten auf dem Display! 🌡️

"Hallo Welt!" war gestern! Heute ist der Tag, an dem deine Wetterstation zum ersten Mal echte, lebendige Daten auf dem Display anzeigt.

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* **Keine Hardware!** Wir benutzen die Bauteile von gestern und kombinieren sie mit neuem Code.

### 🎯 Das Ziel des Tages

Wir verbinden den Code von **Tag 8 (BME280 auslesen)** mit dem Code von **Tag 13 (Display anzeigen)**. Am Ende wird dein Display die **aktuelle Temperatur** anzeigen und sich **automatisch aktualisieren**.

### 🔌 Schritte (Hardware)

* **Nichts zu tun!** Deine Schaltung ist perfekt. Der BME280 Sensor und das OLED-Display teilen sich bereits friedlich die I²C-Daten-Schnellstraße (Pin 3 & 5).

---

### 💻 Schritte (Software)

1.  **Thonny IDE starten.**
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_14/` und öffne die Datei **`Tag_14.py`**.
3.  **Code ansehen:** Schau dir an, wie wir die beiden Welten verbinden. Der Code ist eine Mischung aus Tag 8 und Tag 13.
    * **Wichtig:** Wir müssen die Zahl, die der Sensor uns gibt (z.B. `23.5`), in Text umwandeln, damit das Display sie schreiben kann. Dafür benutzen wir einen Trick namens **"f-String"** (das `f` vor den Anführungszeichen).
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

Schau auf dein OLED-Display! Du solltest jetzt die **Live-Temperatur** sehen, die sich jede Sekunde aktualisiert. Wenn du auf den Sensor atmest, sollte sich die Zahl ändern!

### 🧪 Experimentier-Zone!

Du hast jetzt ein Live-Display! Was kannst du noch anzeigen?

* **Challenge 1: Der Turbo-Modus**
    * Ändere `time.sleep(1)` auf `time.sleep(0.1)`. Wie schnell aktualisiert das Display jetzt?
* **Challenge 2: Der Feuchtigkeits-Messer**
    * **Frage:** Wie änderst du den Code, damit er die **Luftfeuchtigkeit** (`bme280.humidity`) anzeigt?
    * **Tipp:** Du musst zwei Zeilen ändern: Die Zeile, die den Wert liest, und die Zeile, die den `text_fuer_display` erstellt.
* **Challenge 3 (Experte): Das Multi-Display**
    * **Herausforderung:** Zeige Temperatur UND Luftfeuchtigkeit **gleichzeitig** an (untereinander).
    * **Tipp:** Der Trick ist der "Neue Zeile"-Befehl: **`\n`**.
    * Versuche, den Text so zu ändern:
        ```python
        temp_C = bme280.temperature
        hum_pct = bme280.humidity
        text_area.text = f"Temp: {temp_C:.1f} C\nFeuchte: {hum_pct:.1f} %"
        ```
    * **Frage:** Passt der Text auf das Display? Musst du vielleicht die `y`-Position des Labels (Zeile 21) auf `y=0` ändern, damit alles Platz hat?