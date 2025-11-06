# 01_Anleitungen/Tag_10_Display_Simulation.md

## 📅 Tag 10: Umschalten wie ein Profi! (Display-Logik) 👆

Heute bauen wir die Schaltzentrale deiner Wetterstation! Wir verbinden den Taster (Tag 6) mit dem Sensor (Tag 8). Das Terminal wird unser **simuliertes Display**. Auf Knopfdruck zeigen wir entweder die Temperatur oder den Luftdruck an!

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* **Keine Hardware!** Nur eine coole neue Programmier-Idee.

### 🎯 Das Ziel des Tages

Wir nutzen den **Taster (Button)**, um eine Variable im Code umzuschalten. Diese Variable entscheidet dann, welche Messung des BME280 im Terminal angezeigt wird. Das ist die genaue Logik, die später dein echtes Display steuern wird!

### 💡 Wichtig: Überprüfung der Anschlüsse

Stelle sicher, dass diese beiden Teile noch korrekt auf deinem Breadboard verbunden sind:
1.  **BME280 Sensor** (Pin 3 & 5)
2.  **Taster** (GPIO 18, Pin 12) – Wichtig: Denk an den **Pull-Down-Widerstand (10 kΩ)** vom Taster zu GND, sonst funktioniert die Messung nicht!



### 💻 Schritte (Code-Kombination)

Heute schreiben wir den Code, der **zwei Dinge gleichzeitig** macht: Die Taste abfragen und den Sensor lesen.

1.  **Thonny IDE starten.**
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_10/` und öffne die Datei **`Tag_10.py`**.
3.  **Code ansehen:** Der neue Code ist deutlich länger. Achte besonders auf diese neuen Teile:

    * **Zeile 10:** Wir erstellen eine Variable namens **`ANZEIGE_MODUS`** und setzen sie auf **0**. Dies ist unser "Schalter".
        * `0` = Zeige Temperatur.
        * `1` = Zeige Luftdruck.
    * **Zeile 35:** Wir prüfen, ob der Taster gedrückt wurde (`GPIO.input(TASTER_PIN) == GPIO.HIGH`).
    * **Zeile 37-41:** Wenn der Taster gedrückt wird, schalten wir den Modus um (`if ANZEIGE_MODUS == 0: ANZEIGE_MODUS = 1` und umgekehrt).
    * **Zeile 45-51:** Wir nutzen eine **IF-Abfrage**, um zu entscheiden, welche Zeile im Terminal (unserem simulierten Display) angezeigt wird.

4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

* Im Terminal siehst du jetzt entweder die Temperatur oder den Luftdruck.
* **Drücke den Taster** auf deinem Breadboard – die Anzeige sollte sofort umschalten!

### 🧪 Experimentier-Zone!

* **Challenge 1: Drei Modi?**
    * Wir haben zwei Modi (0 und 1). Kannst du einen dritten Modus (2 = Feuchtigkeit) einbauen?
    * **Tipp:** Du musst in der **Modus-Umschalt-Logik** (Zeile 37-41) prüfen, ob der Modus 0, 1 oder 2 ist, und dann zum nächsten springen.
* **Challenge 2: Die Nacht-LED als Anzeige**
    * Nimm die LED (GPIO 17) aus Tag 4.
    * Schreibe Code, der die LED **AN** schaltet, wenn der `ANZEIGE_MODUS` auf **Luftdruck (1)** steht, und **AUS** schaltet, wenn er auf **Temperatur (0)** steht.

---

**Morgen (Tag 11):** Wir bauen den **Piezosummer** ein, um Töne auszugeben!