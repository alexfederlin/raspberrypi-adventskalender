# 01_Anleitungen/Tag_13_Das_Display.md

## 📅 Tag 13: Das Display! Wir sehen was! 📺

Guten Morgen! Gestern haben wir unser "Super-Dashboard" im Terminal simuliert. Schluss mit der Simulation! Heute schließt du den echten Bildschirm an, auf dem unsere Wetterstation bald alles anzeigen wird.

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* Ein **OLED-Display** (ein kleiner, schwarzer Bildschirm)
* Ein paar Jumper-Kabel

### 🎯 Das Ziel des Tages

Wir schließen das Display an und bringen es dazu, "Hallo Welt!" anzuzeigen.

### 💡 Wichtig: Die I²C-Daten-Schnellstraße

Weißt du noch, als wir an Tag 7 den BME280 Sensor an die "Daten-Schnellstraße" (genannt **I²C-Bus**) angeschlossen haben? (Das waren Pin 3 und 5).

Das Geniale ist: An diese Schnellstraße können **mehrere Geräte gleichzeitig** angeschlossen werden! Wir müssen das Display nur mit denselben Pins verbinden, die der BME280 bereits nutzt. Das nennt man "parallel schalten".

### 🔌 Schritte (Hardware)

**WICHTIG: Pi herunterfahren und Stromkabel ziehen!**

Die Schaltung von gestern (BME280, Taster, LDR etc.) bleibt einfach so, wie sie ist!

1.  **Display platzieren:** Stecke das OLED-Display in einen freien Bereich deines Breadboards.
2.  **Strom und Masse:**
    * Verbinde **VCC** (oder VIN) am Display mit der **Roten (+) Schiene** (3.3V).
    * Verbinde **GND** am Display mit der **Blauen (-) Schiene** (GND).
3.  **Daten-Schnellstraße (I²C) TEILEN:**
    * Verbinde **SDA** am Display mit **Pin 3 (GPIO 2)** am Pi.
    * Verbinde **SCL** am Display mit **Pin 5 (GPIO 3)** am Pi.

**Tipp:** Du hast jetzt zwei Kabel, die zu Pin 3 (SDA) wollen (vom BME280 und vom Display). Stecke sie einfach beide in dieselbe 5er-Reihe auf dem Breadboard, die dann mit Pin 3 verbunden ist. Dasselbe machst du für Pin 5 (SCL).



---

### 💻 Schritte (Software)

#### Teil A: Testen

3.  **Der ultimative Test:** Wir prüfen, ob der Pi jetzt **BEIDE** Geräte sieht. Gib wieder ein:
    ```bash
    i2cdetect -y 1
    ```
4.  **Erfolg:** Du solltest jetzt **ZWEI** Adressen in der Tabelle sehen! (z.B. **`76`** oder `77` für den BME280 und **`3c`** für das Display).

#### Teil B: "Hallo Welt!" anzeigen

1.  **Thonny IDE starten.**
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_13/` und öffne die Datei **`Tag_13.py`**.
3.  **Code ansehen:** Der Code ist etwas knifflig, aber er macht Folgendes:
    * Er importiert die neuen Display-Werkzeuge.
    * Er startet den I²C-Bus (wie bei Tag 8).
    * Er initialisiert das Display (unter der Adresse `0x3c`, die du eben gesehen hast).
    * Er erstellt ein Textfeld und zeigt es an.
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

Auf deinem kleinen, schwarzen Bildschirm sollte jetzt hell "Hallo Welt!" leuchten. Du hast das Display zum Leben erweckt!

### 🧪 Experimentier-Zone!

* **Challenge 1: Persönliche Begrüßung**
    * Ändere die Zeile `text = "Hallo Welt!"` in `text = "Dein Name!"` oder `text = "Pi-Wetter!"`. Führe das Skript erneut aus.
* **Challenge 2: Position ändern**
    * Was passiert, wenn du `x=28` und `y=30` änderst?
    * **Versuche:** Setze `x=0` und `y=0`. Wo ist der Text jetzt? (Der 0/0-Punkt ist oben links!)
* **Challenge 3 (Experte): Blinken**
    * Kannst du das Programm so ändern, dass der Text **blinkt**? (Tipp: Du brauchst eine `while True`-Schleife (wie an Tag 5) und Befehle wie `display.root_group = None` und `display.root_group = splash` im Wechsel.)