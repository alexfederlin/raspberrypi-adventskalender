# 01_Anleitungen/Tag_16_Das_Alarm_System.md

## 📅 Tag 16: Das Alarm-System! 🚨

Dein Dashboard ist fantastisch! Aber was nützt eine Wetterstation, wenn sie dich nicht **automatisch** warnt? Heute geben wir ihr ein Gehirn, das selbstständig auf die Umgebung reagiert!

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* **Keine Hardware!** Heute ist der Tag der Logik. Wir brauchen die Bauteile der letzten Tage:
    * **LED** (an GPIO 17)
    * **Summer** (an GPIO 23)

### 🎯 Das Ziel des Tages

Wir rüsten dein Dashboard (den Code von Tag 15) zu einem **vollautomatischen Alarm-System** auf.

1.  Die **LED** soll als **Nachtlicht** dienen: Wenn der LDR-Sensor (Tag 9) Dunkelheit meldet, geht die LED automatisch an.
2.  Der **Summer** soll als **Hitze-Alarm** dienen: Wenn der BME280 (Tag 8) eine hohe Temperatur (z.B. über 27°C) misst, piept der Summer.

Und das Wichtigste: Das alles passiert **im Hintergrund**, während du auf dem Display ganz normal mit dem Taster umschalten kannst!

### 🔌 Schritte (Hardware)

* **Hardware-Check!** Stelle sicher, dass **ALLE** Teile angeschlossen sind:
    * **I2C-Bus (Pin 3, 5):** BME280 UND OLED-Display.
    * **GPIO 18 (Pin 12):** Taster.
    * **GPIO 14 (Pin 8):** LDR-Lichtsensor.
    * **GPIO 17 (Pin 11):** Rote LED.
    * **GPIO 23 (Pin 16):** Piezosummer.



---

### 💻 Schritte (Software)

1.  **Thonny IDE starten.**
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_16/` und öffne die Datei **`Tag_16.py`**.
3.  **Code ansehen:** Das ist der Code von Tag 15, aber mit zwei wichtigen Ergänzungen:
    * Wir definieren `LED_PIN` und `SUMMER_PIN`.
    * In der `while True`-Schleife (Zeile 70+) gibt es **zwei neue `if`-Abfragen**, die *nichts* mit dem Display-Modus zu tun haben. Sie laufen immer im Hintergrund mit.
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

* Dein Display sollte das Dashboard von gestern anzeigen.
* **Probiere es aus:** Halte deine Hand über den **LDR-Sensor**. Wird es dunkel genug (Wert über 1000)? Die **LED** sollte angehen!
* **Probiere es aus:** Atme auf den **BME280-Sensor**. Steigt die Temperatur über 27°C? Der **Summer** sollte piepen!
* **Probiere es aus:** Drücke den **Taster**. Das Display schaltet um, aber die Alarme funktionieren weiter!

### 🧪 Experimentier-Zone!

Du hast die volle Kontrolle über die Grenzwerte!

* **Challenge 1: Empfindlichkeit einstellen**
    * Finde den perfekten Wert für deine `LICHT_GRENZE`. Ändere die Zahl in Zeile 16. Ist `1000` zu viel? Ist `500` besser?
* **Challenge 2: Hitze-Alarm testen**
    * 27°C (Zeile 17) ist vielleicht zu hoch. Setze `HITZE_GRENZE` zum Testen auf `20.0` und starte den Code neu. Piept der Summer jetzt die ganze Zeit (weil es wärmer als 20°C ist)?
* **Challenge 3 (Experte): Der Stumm-Schalter**
    * **Herausforderung:** Kannst du den **Taster (GPIO 18)** so umprogrammieren, dass er den **Summer stumm schaltet**, *nachdem* der Alarm losgegangen ist?
    * **Tipp:** Du brauchst eine neue Variable (z.B. `alarm_stumm = False`) und musst die Taster-Logik (Zeile 47) UND die Summer-Logik (Zeile 78) anpassen. Das ist knifflig!