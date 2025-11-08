# 01_Anleitungen/Tag_09_Lichtsensor.md

## 📅 Tag 9: Der Lichtsensor – Helligkeit messen! 💡

Toll, dein Pi misst schon Temperatur, Feuchtigkeit und Druck. Jetzt bringen wir ihm bei, zu sehen!

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* Ein **Fotowiderstand** (LDR, Light Dependent Resistor)
* Ein **10 kOhm Widerstand** (Braun-Schwarz-Orange)

### 🎯 Das Ziel des Tages

Wir verwenden heute den **Fotowiderstand (LDR)**, um die Helligkeit im Raum zu messen.

**WICHTIG:** Der Raspberry Pi kann Licht nicht direkt messen, da er nur digitale Signale (AN/AUS) liest. Wir nutzen einen Trick: Wir bauen einen **Spannungsteiler** mit dem 10 kOhm Widerstand. Dieser Trick verwandelt die Helligkeit in eine **analoge Spannung**, die wir mit einem Trick (dem RC-Glied) digital messen können.

### 💡 Der RC-Trick (Widerstand-Kondensator)

Da wir keinen echten Analog-Digital-Wandler haben, nutzen wir die **Ladezeit** eines Kondensators. (Keine Sorge, du brauchst keinen Kondensator, der ist im Pi eingebaut!)

Die Zeit, die es dauert, einen Pin von **HIGH** auf **LOW** zu schalten und dann wieder auf **HIGH** zu laden, hängt von dem Widerstand im Stromkreis ab. Je heller es ist, desto geringer ist der Widerstand des LDR, und desto **schneller** ist die Ladezeit.

### 🔌 Schritte (Hardware)

**WICHTIG: Pi herunterfahren und Stromkabel ziehen!** Die Schaltung von Tag 7/8 (BME280) bleibt bestehen.

1.  **LDR platzieren:**
    * Stecke die beiden Beinchen des **Fotowiderstands (LDR)** in zwei unterschiedliche, freie Reihen deines Breadboards (z.B. Reihe 17 und 20). Der LDR hat keine Polarität, es ist egal, wie herum er steckt.
2.  **Verbindung zur Masse (GND):**
    * Verbinde das Beinchen des LDR in **Reihe 17** mit der **Blauen (GND / Minus) Schiene** deines Breadboards.
3.  **Spannungsteiler bauen:**
    * Nimm den **10 kOhm Widerstand**.
    * Stecke ein Ende in dieselbe Reihe wie das LDR-Beinchen in **Reihe 20**.
    * Stecke das andere Ende in eine freie Reihe (z.B. Reihe 24).
4.  **Verbindung zur Spannung (3.3V):**
    * Verbinde die Reihe **24** (wo das zweite Widerstands-Ende steckt) mit der **Roten (3.3V / Plus) Schiene**.
5.  **Daten-Pin (Messung):**
    * Nimm ein Jumper-Kabel.
    * Finde den Pin **GPIO 14** am Raspberry Pi (das ist der physische Pin 8, siehe Diagramm). 
    * Verbinde **GPIO 14** mit dem Messpunkt, nämlich der Reihe, die **LDR** und **10 kOhm Widerstand** verbindet (Reihe **20**).



### 💻 Schritte (Code-Ausführung)

1.  **Pi starten** und **Thonny IDE** öffnen.
2.  **Datei öffnen:** Navigiere zu `Desktop/Adventskalender_Pi_Tage/Tag_09/` und öffne die Datei **`Tag_09.py`**.
3.  **Code ansehen:** Der Code ist heute besonders spannend, weil er einen cleveren Trick benutzt, um die Ladezeit zu messen!

1
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.

### ✅ Erfolg!

Im Shell-Fenster siehst du jetzt die "Ladezeit" als Zahl. **Vergiss nicht:** Eine **kleine Zahl** bedeutet **helles Licht** (schnell geladen)!

### 🧪 Experimentier-Zone!

Der LDR reagiert superschnell! Was kannst du damit anstellen?

* **Challenge 1: Taschenlampen-Test**
    * Leuchte mit einer Taschenlampe direkt auf den LDR.
    * **Frage:** Wie tief sinkt der Wert? (Vielleicht unter 100?)
    * Halte einen Finger über den LDR. Wie hoch steigt der Wert im Dunkeln?
* **Challenge 2: Die Nacht-LED**
    * **Herausforderung:** Kombiniere den Code von heute mit dem Code der **LED (GPIO 17)** von Tag 4.
    * Schreibe eine `if`-Bedingung in die `while True`-Schleife, die sagt: "Wenn die `ladezeit` **höher als 1000** ist (es ist dunkel), schalte die LED AN."
* **Challenge 3 (Experte): Der Dämmerungsmesser**
    * **Herausforderung:** Der BME280 misst Temperatur, der LDR misst Licht. Kannst du dem Programm beibringen, nur zu messen und zu protokollieren, wenn es **dunkel UND kalt** ist?

---

**Morgen (Tag 10):** Keine Elektronik, sondern die erste Montageschritt für das Gehäuse!