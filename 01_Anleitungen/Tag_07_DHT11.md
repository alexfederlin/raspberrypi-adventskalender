# 01_Anleitungen/Tag_07_Temperatursensor.md

## 📅 Tag 7: Der Temperatur- und Feuchtigkeitssensor 🌡️💧

Tolle Arbeit! Mit dem Taster von gestern kannst du deinem Pi jetzt Befehle geben. Zeit für den nächsten Schritt: **Fühlen**!

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* Ein **Temperatur- und Feuchtigkeitssensor** (wahrscheinlich ein **DHT11** oder **DHT22** Modul).

### 🎯 Das Ziel des Tages

Heute bringen wir den Pi dazu, seine Umgebung wahrzunehmen. Du verbindest den Sensor mit dem Breadboard und dem Pi. Morgen verwenden wir den Code, um die Werte auszulesen!

### 💡 Der DHT11/DHT22 Sensor

Dein Sensor hat normalerweise 3 oder 4 Pins:
1.  **VCC** oder **+** (Stromversorgung)
2.  **DATA** oder **OUT** (Das Signal zum Pi)
3.  **GND** oder **-** (Masse/Minus)

Wenn du ein kleines Modul hast (3 Pins), ist der nötige Widerstand (Pull-up) oft schon eingebaut – das macht die Verkabelung einfacher!

### 🔌 Schritte (Hardware)

**WICHTIG: Pi herunterfahren und Stromkabel ziehen!** Die Schaltung von Tag 6 (LED und Taster) lassen wir für heute bestehen, falls du experimentieren möchtest.

1.  **Sensor platzieren:**
    * Stecke den **Temperatur-/Feuchtigkeitssensor** auf eine freie Stelle deines Breadboards.
2.  **Stromversorgung (3.3V):**
    * Nimm ein Jumper-Kabel (rot).
    * Verbinde den **VCC** Pin (oder **+** Pin) des Sensors mit der **Roten (+) Schiene** deines Breadboards. (Stelle sicher, dass diese Schiene wie in Tag 6 mit dem 3.3V Pin des Pi verbunden ist).
3.  **Masse (GND):**
    * Nimm ein Jumper-Kabel (schwarz oder blau).
    * Verbinde den **GND** Pin (oder **-** Pin) des Sensors mit der **Blauen (-) Schiene** deines Breadboards. (Diese Schiene sollte mit einem GND Pin des Pi verbunden sein).
4.  **Daten-Pin verbinden (Input):**
    * Nimm ein Jumper-Kabel (z.B. orange).
    * Finde den Pin **GPIO 4** am Raspberry Pi (das ist der physische Pin 7, siehe Diagramm).
    * Verbinde **GPIO 4** mit dem **DATA** Pin (oder **OUT** Pin) deines Sensors.



### 💻 Code-Test

Für heute gibt es keinen speziellen Code. Wir machen nur eine einfache Prüfung, ob der Pi den Sensor prinzipiell erkennen kann.

1.  **Pi starten:** Schließe den Strom wieder an und starte den Pi.
2.  **Terminal öffnen.**
3.  **Hardware-Test:** Gib diesen Befehl ein und drücke `Enter`:
    ```bash
    gpio read 7
    ```
    * Der Befehl fragt den Zustand von Pin 7 (GPIO 4) ab. Wenn der Sensor korrekt mit Strom versorgt wird, sollte der Wert **0** oder **1** anzeigen. Das ist schon ein gutes Zeichen!

---

**Morgen (Tag 8):** Wir installieren die nötigen Bibliotheken, um die Temperatur- und Feuchtigkeitswerte auszulesen!

Wenn du mehr darüber erfahren möchtest, wie der DHT11 Sensor mit deinem Pi verbunden wird, schau dir dieses Video an: [How to Set Up the DHT11 Humidity Sensor on the Raspberry Pi](https://www.youtube.com/watch?v=DPvxsHoD7kc).