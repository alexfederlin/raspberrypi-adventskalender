# 01_Anleitungen/Tag_11_Piezosummer.md

## 📅 Tag 11: Piep! Der Pi macht Geräusche! 📢

Guten Morgen! Gestern haben wir die Logik für unser Display simuliert. Heute geben wir der Station eine Stimme (oder zumindest ein Piepsen).

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* Ein **Piezosummer** (ein kleiner Lautsprecher)

### 🎯 Das Ziel des Tages

Heute bringen wir den Pi dazu, Töne von sich zu geben. Wir verwenden einen **aktiven Summer**. "Aktiv" bedeutet, du musst ihm nur Strom geben (ihn auf `HIGH` setzen), und er piept von selbst. Das ist super einfach und perfekt für Alarme!

### 💡 Wichtig: Die Polarität (+) und (-)

Schau dir den Summer genau an:
* Meistens hat er ein **langes Beinchen (+)** und ein **kurzes Beinchen (-)**.
* Manchmal ist auch ein **+** auf das Gehäuse gedruckt.
* Es ist wichtig, ihn richtig herum anzuschließen!

### 🔌 Schritte (Hardware)

**WICHTIG: Pi herunterfahren und Stromkabel ziehen!** Die Schaltungen von BME280 und Taster/LED bleiben bestehen.

1.  **Summer platzieren:**
    * Stecke den **Piezosummer** in zwei freie Reihen auf deinem Breadboard (z.B. Reihe 25 und 26). Achte darauf, welches das lange (+) und welches das kurze (-) Beinchen ist.
2.  **Minuspol (GND) verbinden:**
    * Verbinde das **kurze Beinchen (-)** des Summers mit der **Blauen (GND / Minus) Schiene** deines Breadboards.
3.  **Pluspol (Signal) verbinden:**
    * Wir brauchen einen neuen GPIO-Pin als Ausgang. Nehmen wir **GPIO 23** (das ist der physische Pin 16).
    * Verbinde das **lange Beinchen (+)** des Summers mit **GPIO 23** am Pi.




---

### 💻 Schritte (Software)

1.  **Pi starten** und **Thonny IDE** öffnen.
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_11/` und öffne die Datei **`Tag_11.py`**.
3.  **Code ansehen:** Der Code ist super einfach. Er funktioniert genau wie bei der LED: `HIGH` = Piepen, `LOW` = Stille.
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

Dein Pi sollte gerade gepiept haben! Du hast deiner Station eine Stimme gegeben!

### 🧪 Experimentier-Zone!

Jetzt wird es richtig spannend, denn jetzt können wir **ALLES** kombinieren!

* **Challenge 1: Der Alarm-Knopf 🚨**
    * Kombiniere den Code von **Tag 6 (Taster)** und **Tag 11 (Summer)**.
    * **Herausforderung:** Schreibe ein Programm (in einer `while True`-Schleife), bei dem der Summer **nur piept, solange du den Taster (GPIO 18) gedrückt hältst.**
* **Challenge 2: Der Temperatur-Alarm (WICHTIG!) 🔥**
    * Das ist die Haupt-Challenge für die Wetterstation!
    * Kombiniere **Tag 8 (BME280)** und **Tag 11 (Summer)**.
    * **Herausforderung:** Schreibe ein Programm, das kontinuierlich die Temperatur misst. **Wenn die Temperatur über einen bestimmten Wert steigt (z.B. 25°C), soll der Summer automatisch anfangen zu piepen!**
    * **Tipp:** Du brauchst eine `while True`-Schleife und eine `if`-Abfrage (z.B. `if temp_C > 25:`).
* **Challenge 3 (Experte): Der Helligkeits-Alarm ☀️**
    * Kombiniere **Tag 9 (LDR)** und **Tag 11 (Summer)**.
    * **Herausforderung:** Der Pi soll piepen, wenn es **zu dunkel** wird (also, wenn der LDR-Wert *über* einen Schwellenwert steigt).

