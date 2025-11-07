# 01_Anleitungen/Tag_12_Super-Dashboard.md

## 📅 Tag 12: Das Super-Dashboard! Alle Sensoren auf einen Blick 📈

Wahnsinn! Du hast jetzt Augen (LDR), Ohren (Taster), einen Mund (Summer) und einen Fühlsinn (BME280) für deinen Pi gebaut. Heute führen wir alles in einem Gehirn zusammen!

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* **Keine Hardware!** Heute ist ein reiner Programmier-Tag, an dem wir alles verbinden.

### 🎯 Das Ziel des Tages

Wir schreiben das bisher größte Skript: Ein **"Super-Dashboard"**.

Dein Terminal wird wieder zum simulierten Display. Mit dem **Taster** schaltest du durch verschiedene "Bildschirme", die dir alle Sensorwerte anzeigen, die dein Pi gerade misst.

### 💡 Hardware-Check (WICHTIG!)

Stelle sicher, dass **alle** deine Bauteile von den letzten Tagen noch korrekt auf dem Breadboard angeschlossen sind:

1.  **BME280** (an I2C: Pin 3 & 5)
2.  **Taster** (an GPIO 18) mit seinem 10 kOhm Pull-Down-Widerstand.
3.  **LDR-Lichtsensor** (an GPIO 14) mit seinem 10 kOhm Widerstand.
4.  *(Optional für die Challenges)*: LED (an GPIO 17) & Summer (an GPIO 23).



---

### 💻 Schritte (Software)

1.  **Thonny IDE starten.**
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_12/` und öffne die Datei **`Tag_12.py`**.
3.  **Code ansehen:** Nimm dir Zeit, den Code zu lesen. Er kombiniert alles, was du gelernt hast:
    * **Importieren:** Wir importieren alle Bibliotheken (GPIO, BME280, time).
    * **Setup:** Wir definieren alle Pins (BME280, TASTER_PIN, LDR_PIN).
    * **Funktion:** Die `measure_light()`-Funktion von Tag 9 ist wieder da.
    * **Logik-Variable:** `ANZEIGE_MODUS = 0`.
    * **While-Schleife:** Die Hauptschleife...
        1.  ...liest **alle** Sensoren (Temp, Druck, Feuchte, Licht).
        2.  ...prüft, ob der **Taster** gedrückt wurde.
        3.  ...schaltet den `ANZEIGE_MODUS` weiter (0 -> 1 -> 2 -> 0).
        4.  ...zeigt mit `if/elif/else` den richtigen "Bildschirm" an.
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

Du siehst jetzt eine Zeile mit Daten. Drücke den Taster! Die Anzeige sollte umschalten! Du hast erfolgreich **alle Sensoren und Inputs in einem Skript verbunden!**

### 🧪 Experimentier-Zone!

Du hast jetzt ein Gehirn, das alles weiß. Zeit für automatische Aktionen!

* **Challenge 1: Der "Alles-OK"-Blinker**
    * Nimm die **LED (GPIO 17)**.
    * Baue sie in die `while True`-Schleife ein. Sie soll **unabhängig vom Display-Modus** einmal pro Sekunde kurz aufblitzen (`time.sleep(0.1)`), nur um zu zeigen: "Ich lebe noch!"
* **Challenge 2: Das Nachtlicht-Alarm-System (Kombination!)**
    * **Herausforderung:** Das Programm soll **automatisch** die **LED (GPIO 17) einschalten**, wenn der Lichtwert (`licht_val`) über 1000 steigt (es ist dunkel).
    * **UND:** Es soll **automatisch** den **Summer (GPIO 23) piepen lassen**, wenn die Temperatur (`temp_C`) über 25°C steigt.
    * **Tipp:** Du brauchst dafür zwei separate `if`-Abfragen *innerhalb* der `while True`-Schleife, die *nichts* mit dem `ANZEIGE_MODUS` zu tun haben.