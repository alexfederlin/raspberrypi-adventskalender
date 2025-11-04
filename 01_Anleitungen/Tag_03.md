# 01_Anleitungen/Tag_03_Breadboard.md

## 📅 Tag 3: Breadboard-Grundlagen 📌

Bevor du dieses Türchen öffnest: Hast du dir schon die heutige Anleitung geholt?

**Deine erste Aufgabe (jeden Tag!):**
1.  Öffne das **Terminal**.
2.  Gehe in deinen Projektordner: `cd Desktop/Adventskalender_Pi_Tage`
3.  Hole die neuen Dateien ab: `git pull`
4.  Jetzt kannst du das Türchen öffnen!

### 🎁 Inhalt des Türchens

* Ein **Breadboard** (Steckplatine)
* Ein paar **Jumper-Kabel** (Verbindungskabel)

### 🎯 Das Ziel des Tages

Heute lernst du das **wichtigste Werkzeug** für Elektronik-Bastler kennen: das **Breadboard** (man sagt auch Steckplatine).

Stell dir ein Breadboard wie ein Lego-Brett für Elektronik vor. Statt zu löten, kannst du Bauteile einfach hineinstecken, um Schaltungen zu testen.

### 💡 Breadboard-Erklärung

Schau dir dein Breadboard genau an:

* **Die Power-Schienen (Rails):** An den Seiten siehst du **rote** und **blaue** Linien. Alle Löcher in der **blauen** Spalte sind miteinander verbunden (das ist der Minuspol, **GND**). Alle Löcher in der **roten** Spalte sind miteinander verbunden (das ist der Pluspol, **5V** oder **3.3V**).
* **Die Reihen (Rows):** In der Mitte sind die Löcher in 5er-Reihen (z.B. Reihe 1, A-B-C-D-E) verbunden. Diese Reihen sind perfekt, um Bauteile miteinander zu verbinden.



### 💡 GPIO-Pins am Raspberry Pi

Dein Raspberry Pi hat an der Seite eine lange Reihe von "Stacheln". Das sind die **GPIO-Pins** (General Purpose Input/Output). Über diese Pins kann der Pi mit unserer Hardware sprechen (Strom senden, Signale empfangen).



[Image of Raspberry Pi GPIO pinout diagram]


### 🔌 Schritte (ca. 15 Minuten)

Heute bauen wir noch keinen echten Stromkreis, aber wir bereiten das Breadboard vor, indem wir es mit dem Strom des Raspberry Pi verbinden.

**WICHTIG: Dein Pi muss ausgeschaltet sein, während du Kabel an die GPIO-Pins anschließt!**

1.  **Pi herunterfahren:** Fahre deinen Pi über das Menü herunter und ziehe das Stromkabel ab.
2.  **Minuspol (GND) verbinden:**
    * Nimm ein **Jumper-Kabel** (am besten ein schwarzes oder blaues).
    * Finde einen **"GND" (Ground)** Pin am Raspberry Pi (siehe GPIO-Diagramm, z.B. Pin 6).
    * Stecke das eine Ende des Kabels auf Pin 6.
    * Stecke das andere Ende in ein beliebiges Loch der **blauen (Minus-) Schiene** auf deinem Breadboard.
3.  **Pluspol (5V) verbinden:**
    * Nimm ein **Jumper-Kabel** (am besten ein rotes).
    * Finde einen **"5V power"** Pin am Raspberry Pi (z.B. Pin 2).
    * Stecke das eine Ende des Kabels auf Pin 2.
    * Stecke das andere Ende in ein beliebiges Loch der **roten (Plus-) Schiene** auf deinem Breadboard.
4.  **Überprüfen:**
    * Dein Aufbau sollte jetzt so aussehen (oder ähnlich): 
    * Du hast jetzt Strom auf den Schienen deines Breadboards!

### 💻 Code-Test

Für heute gibt es keinen Code. Das heutige Ziel war es, dein "Elektronik-Lego-Brett" vorzubereiten.

---

**Morgen (Tag 4):** Wir bringen das erste Bauteil zum Leuchten!