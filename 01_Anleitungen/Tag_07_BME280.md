# 01_Anleitungen/Tag_07_BME280_Sensor.md

## 📅 Tag 7: Der Profi-Sensor (BME280) anschließen 🌡️💧💨

Tolle Arbeit! Zeit, dass dein Pi seine Umgebung nicht nur wahrnimmt, sondern sie wie ein Wetterfrosch messen kann!

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* Ein **BME280 Sensor-Modul** (Misst Temperatur, Luftfeuchtigkeit und Luftdruck!)

### 🎯 Das Ziel des Tages

Der BME280 ist ein Profi-Sensor. Er benutzt nicht nur ein Kabel, sondern den sogenannten **I²C-Bus** (eine Art Schnellstraße für Daten) am Raspberry Pi. Heute verkabeln wir diesen Bus und aktivieren ihn im System des Pi.

### 💡 Wichtig: I²C-Verbindung

Der BME280 benötigt **vier** Kabel für die Verbindung zum Pi: Strom (3.3V), Masse (GND) und zwei Datenleitungen (SDA und SCL).

### 🔌 Schritte (Hardware)

**WICHTIG: Pi herunterfahren und Stromkabel ziehen!** Die Schaltung von Tag 6 (LED und Taster) lässt du wie gehabt bestehen.

1.  **Sensor platzieren:**
    * Stecke das BME280 Modul auf eine freie Stelle deines Breadboards.
2.  **Stromversorgung (VCC und GND):**
    * Verbinde **VCC** (oder VIN) am Sensor mit dem **3.3V Power Pin** des Raspberry Pi (**Pin 1**).
    * Verbinde **GND** am Sensor mit einem **GND Pin** des Pi (**Pin 6**).
3.  **I²C-Datenleitungen:**
    * Nimm zwei neue Jumper-Kabel (z.B. Weiß und Grau).
    * Verbinde den Pin **SDA** (Serial Data) am Sensor mit **GPIO 2** am Pi (**Pin 3**).
    * Verbinde den Pin **SCL** (Serial Clock) am Sensor mit **GPIO 3** am Pi (**Pin 5**).

| BME280 Pin | Raspberry Pi GPIO Pin | Physischer Pin (Board) |
| :--- | :--- | :--- |
| **VCC** | 3.3V Power | **Pin 1** |
| **GND** | Ground | **Pin 6** |
| **SDA** | **GPIO 2** | **Pin 3** |
| **SCL** | **GPIO 3** | **Pin 5** |



### 💻 Schritte (Software-Vorbereitung)

Bevor wir den Sensor testen können, muss der Pi wissen, dass er den I²C-Bus benutzen soll.

1.  **Pi starten:** Schließe den Strom wieder an und starte den Pi.
2.  **Terminal öffnen.**

#### Teil A: I²C im System aktivieren

1.  Gib diesen Befehl ein und drücke `Enter`:
    ```bash
    sudo raspi-config
    ```
2.  Navigiere im blauen Menü zu **3 Interface Options** (Schnittstellen-Optionen).
3.  Wähle **I2C**.
4.  Wähle **Yes** (Ja), um die I2C-Schnittstelle zu aktivieren.
5.  Wähle **Finish** und starte den Pi **neu**, wenn er dich dazu auffordert (`sudo reboot`).

#### Teil B: I²C-Tools installieren und testen

Nach dem Neustart:

1.  Öffne das **Terminal** erneut.
2.  Installiere die nötigen Diagnose-Tools:
    ```bash
    sudo apt-get update && sudo apt-get install -y i2c-tools
    ```
3.  Teste, ob der Pi den Sensor im Bus findet:
    ```bash
    i2cdetect -y 1
    ```

### ✅ Erfolg!

* Wenn alles richtig verkabelt ist, siehst du im Terminal in der Tabelle eine **hexadezimale Adresse** (wahrscheinlich **`76`** oder **`77`**) anstatt von `--`.
* Das bedeutet: Dein Pi sieht den BME280 und ist bereit für den Code!

### 🧪 Experimentier-Zone!

* **Frage:** Was siehst du im Terminal, wenn du das **SDA**-Kabel vom Pi abziehst und den Test (`i2cdetect -y 1`) wiederholst? (Die Adresse sollte verschwinden oder der Befehl fehlschlagen, da die Datenleitung fehlt!)
* **Herausforderung:** Versuche, die LED (GPIO 17) mit dem Taster (GPIO 18) zu steuern, während der BME280 angeschlossen ist. Funktioniert das noch? (Es sollte, da sie unterschiedliche Pins verwenden!)

---

**Morgen (Tag 8):** Wir installieren die spezielle Python-Bibliothek und lesen die ersten echten Werte (Temperatur, Feuchtigkeit und Druck) aus!