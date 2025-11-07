# 01_Anleitungen/Tag_15_Display_Dashboard.md

## 📅 Tag 15: Das Display-Dashboard! 📊

Du hast es fast geschafft! Gestern hast du Live-Daten auf dem Display angezeigt. Heute kombinieren wir das mit der Taster-Logik von Tag 12. Das hier ist der "Meister-Code" für unsere Wetterstation!

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* **Keine Hardware!** Heute ist der ultimative Code-Kombinations-Tag.

### 🎯 Das Ziel des Tages

Wir bringen **alle** wichtigen Teile zusammen:
1.  **BME280 Sensor** (Lesen)
2.  **LDR Lichtsensor** (Lesen)
3.  **Taster** (Input)
4.  **OLED-Display** (Output)

Am Ende kannst du mit dem Taster durch **zwei** verschiedene Bildschirme auf deinem **echten OLED-Display** blättern.

### 🔌 Schritte (Hardware)

* **Nichts zu tun!** Deine Schaltung ist perfekt, wenn alles von gestern noch angeschlossen ist:
    * **I2C-Bus (Pin 3 & 5):** BME280 UND OLED-Display.
    * **GPIO 18 (Pin 12):** Taster (mit Pull-Down-Widerstand).
    * **GPIO 14 (Pin 8):** LDR-Lichtsensor (mit seinem 10k-Widerstand).



---

### 💻 Schritte (Software)

1.  **Thonny IDE starten.**
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_15/` und öffne die Datei **`Tag_15.py`**.
3.  **Code ansehen:** Das ist unser bisher schlaustes Skript. Es verbindet alles, was du gelernt hast.

    * Es importiert **alle** Bibliotheken (GPIO, I2C-Sensoren, Display).
    * Es richtet **alle** Pins ein.
    * Es hat die `measure_light()`-Funktion von Tag 9.
    * Es hat eine `ANZEIGE_MODUS`-Variable.
    * In der `while True`-Schleife liest es **alle** Sensoren, prüft den **Taster** und **ändert den Text** auf dem Display!
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

Dein Display zeigt jetzt Temperatur und Feuchtigkeit an. **Drücke den Taster!** Die Anzeige sollte sofort umschalten und den Helligkeitswert des LDR-Sensors anzeigen. Drücke ihn erneut, und du bist wieder zurück.

Du hast das Gehirn deiner Wetterstation fertig programmiert!

### 🧪 Experimentier-Zone!

Du bist jetzt der Chef-Programmierer.

* **Challenge 1: Bessere Anzeige**
    * Im Modus 1 (Lichtwert) ist die zweite Zeile nur eine Erklärung.
    * **Herausforderung:** Ändere den Code für Modus 1 so, dass er stattdessen den **Luftdruck** (`bme280.pressure`) anzeigt!
* **Challenge 2: Der "Willkommen"-Bildschirm**
    * **Herausforderung:** Bevor die `while True`-Schleife startet, füge Code hinzu, der 2 Sekunden lang "Wetterstation STARTET..." auf dem Display anzeigt.
    * **Tipp:** Du musst `text_area.text = "STARTET..."`, `time.sleep(2)` und `display.fill(0)` *vor* der `while True`-Schleife einfügen.