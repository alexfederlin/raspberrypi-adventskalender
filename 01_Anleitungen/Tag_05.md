# 01_Anleitungen/Tag_05_Blinken.md

## 📅 Tag 5: Die LED blinken lassen ✨

Hallo Programmierer! Hast du schon dein `git pull` gemacht?

### 🎁 Inhalt des Türchens

* **Heute: Kein Inhalt!**
* Wir benutzen die Hardware von gestern. Heute geht es nur um **neuen Code**!

### 🎯 Das Ziel des Tages

Die LED nur einzuschalten ist langweilig. Heute bringen wir sie dazu, **zu blinken**! Dazu brauchen wir eine **Schleife** (Loop).

### 🔌 Schritte (Hardware)

* Nichts zu tun! Die Schaltung von Tag 4 ist perfekt.

### 💻 Schritte (Software)

1.  **Pi starten** und **Thonny IDE** öffnen.
2.  **Datei öffnen:** `Desktop/Adventskalender_Pi_Tage/Tag_05/Tag_05.py`.
3.  **Code ansehen:** Schau dir den neuen Code genau an. Was ist anders als gestern?
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.
5.  **WICHTIG:** Das Programm läuft ewig! Um es zu stoppen, klicke in das **"Shell"-Fenster** (unten in Thonny) und drücke auf deiner Tastatur **gleichzeitig STRG + C**.

### 🧪 Experimentier-Zone!

Jetzt bist du dran! Ein blinkendes Licht ist der Anfang von allem. Ein Leuchtturm? Ein Alarmsignal? Ein Roboter-Auge?

* **Challenge 1: Der Beschleuniger**
    * **Frage:** Was musst du ändern, damit die LED **viel schneller** blinkt?
    * **Versuche:** Ändere beide `time.sleep(0.5)`-Werte auf `time.sleep(0.1)`. Was passiert?
    * **Frage:** Wie schnell kannst du es blinken lassen, bevor deine Augen es nicht mehr als Blinken erkennen?
* **Challenge 3:**
    * Was passiert, wenn du `time.sleep(1)` für "AN" und `time.sleep(0.1)` für "AUS" nimmst? Wie ändert sich der Rhythmus?
* **Challenge 2 (Experte): Der SOS-Code**
    * Im Morsealphabet ist SOS: 3x kurz, 3x lang, 3x kurz.
    * **Tipp:** "Kurz" könnte `time.sleep(0.2)` sein, "Lang" könnte `time.sleep(0.7)` sein.
    * **Herausforderung:** Kannst du den `while True:`-Block so umschreiben, dass die LED SOS morst? (Du musst viele `HIGH`, `LOW` und `sleep`-Befehle untereinanderschreiben).