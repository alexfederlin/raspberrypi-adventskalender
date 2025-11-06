# 01_Anleitungen/Tag_08_BME280_Auslesen.md

## 📅 Tag 8: Temperatur, Feuchtigkeit und Druck auslesen! 📊

Super! Gestern hast du den BME280 korrekt verkabelt und den I²C-Bus im Pi aktiviert. Heute bringen wir Python bei, die Daten von diesem Sensor zu holen.

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* **Keine Hardware!** Heute geht es nur um **Code-Installation** und **Ausführung**.

### 🎯 Das Ziel des Tages

Um den BME280 über I²C auszulesen, brauchen wir eine spezielle **Bibliothek** (eine Art Werkzeugkasten für Python). Wir installieren die Bibliothek von Adafruit und schreiben ein Skript, das Temperatur, Feuchtigkeit und Luftdruck misst.

### 💻 Schritte (Software-Installation)

Der Code für den BME280 ist etwas komplexer, daher nutzen wir einen fertigen Code-Baukasten, den wir über den Paketmanager `pip` installieren.

1.  **Terminal öffnen.** (Falls du es von gestern noch aufhast: Gut!)
2.  Installiere die nötigen Python-Pakete, um den I²C-Bus und den Sensor anzusprechen:
    ```bash
    sudo pip3 install adafruit-circuitpython-bme280
    ```
    * (**Tipp:** Wenn du eine Fehlermeldung bekommst, versuche zuerst, `sudo pip3 install adafruit-blinka` zu installieren und wiederhole dann den obigen Befehl).
3.  **Warten:** Die Installation dauert einen Moment, da Python die nötigen Werkzeuge herunterlädt.

---

### 💻 Schritte (Code-Ausführung)

Jetzt, wo der Werkzeugkasten installiert ist, können wir den Code starten, um die ersten echten Messwerte zu sehen!

1.  **Thonny IDE starten.**
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_08/` und öffne die Datei **`Tag_08.py`**.
3.  **Code ansehen:** Der Code sieht komplexer aus, aber er macht im Grunde nur Folgendes:
    * Er schaut, wo der Sensor sitzt (`i2c = busio.I2C(board.SCL, board.SDA)`).
    * Er liest die drei Werte aus (`sensor.temperature`, `sensor.humidity`, `sensor.pressure`).
    * Er wiederholt das, damit du die Änderungen beobachten kannst!

4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

Im unteren Shell-Fenster siehst du jetzt im 5-Sekunden-Takt die aktuellen **Temperatur**, **Luftfeuchtigkeit** und den **Luftdruck** an deinem Standort!

* **Stoppen:** Klicke in die Shell und drücke **STRG + C**.

### 🧪 Experimentier-Zone!

Super! Du hast jetzt deine eigene kleine Wetterstation! Was kannst du damit machen?

* **Challenge 1: Heißluft-Föhn**
    * Halte deinen Finger oder deine Hand vorsichtig über den Sensor.
    * **Frage:** Wie schnell ändert sich die Temperatur?
    * **Herausforderung:** Nimm einen kleinen Ventilator oder puste vorsichtig über den Sensor. Ändert sich der Feuchtigkeitswert?
* **Challenge 2: Die Wetter-Geschwindigkeit**
    * **Frage:** Die Messung alle 5 Sekunden ist langsam. Was passiert, wenn du `time.sleep(5)` zu `time.sleep(0.5)` änderst? Wie schnell kann der Pi messen?
* **Challenge 3 (Experte): Höhenmesser**
    * Wenn du den Luftdruck in eine Höhe umrechnest, kannst du einen Höhenmesser bauen!
    * **Suche:** Wie lautet die **Barometrische Höhenformel**? Versuche, eine neue Variable (`hoehe_m`) im Code zu berechnen, die sich nur ändert, wenn du den Sensor kurz anhebst!
