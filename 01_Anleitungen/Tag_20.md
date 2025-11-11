# 01_Anleitungen/Tag_20_Das_Gehaeuse.md

## 📅 Tag 20: Wir bauen ein Zuhause! (3D-Druck) 🏠

Fantastisch! Dein Code kann jetzt alles: Lokale Sensoren messen, das Internet abfragen und Alarme auslösen. Dein Breadboard platzt bestimmt schon aus allen Nähten!

Heute beginnen wir mit dem finalen Schritt: Wir bauen ein **permanentes Gehäuse** für deine Wetterstation.

* **Tages-Routine:** Terminal öffnen, `cd Desktop/Adventskalender_Pi_Tage`, dann `git pull`.

---

### 🎁 Inhalt des Türchens

* Eine Rolle **Spezial-Filament** (z.B. Leucht-PLA, Seiden-Blau oder Glitzer-Schwarz)
* Eine Notiz, die auf die **STL-Dateien** im Git-Repo hinweist.

### 🎯 Das Ziel des Tages

Heute ist ein "Action-Tag" außerhalb des Pi! Wir werden die 3D-Modelle (die digitalen Baupläne) für dein Gehäuse finden und den **3D-Druck starten**. Das ist der größte Schritt, um deine Station von einem Experiment in ein fertiges Produkt zu verwandeln.

### 💡 Die STL-Dateien (Die Baupläne)

STL-Dateien sind die Standard-Baupläne für 3D-Drucker. In deinem `Adventskalender_Pi_Tage` Ordner solltest du jetzt (nach dem `git pull`) einen neuen Ordner `02_Gehaeuse_STL/` finden.

Darin liegen die drei Teile, die wir brauchen:
1.  **`Gehaeuse_Boden.stl`**: Das Fundament, auf das der Raspberry Pi geschraubt wird.
2.  **`Gehaeuse_Front.stl`**: Die Frontplatte mit den perfekten Ausschnitten für dein OLED-Display, den Taster und die LED.
3.  **`Gehaeuse_Deckel.stl`**: Der Deckel, der alles schützt und (oft) die Sensoren hält.



---

### 🛠️ Schritte (Vorbereitung & Druck)

**WICHTIG:** 3D-Drucken ist ein Prozess, der Zeit braucht und oft die Hilfe eines Erwachsenen erfordert.

1.  **Dateien finden:** Stelle sicher, dass du den Ordner `02_Gehaeuse_STL/` auf deinem Computer hast.
2.  **Filament auspacken:** Nimm das coole Spezial-Filament aus dem heutigen Türchen. Das wird das Material sein, aus dem dein Gehäuse besteht!
3.  **"Slicen" (Eltern-Hilfe):**
    * Die `.stl`-Dateien müssen mit einer Software (genannt "Slicer", z.B. *Cura*, *PrusaSlicer* oder *OrcaSlicer*) für den 3D-Drucker vorbereitet werden.
    * In dieser Software werden Dinge wie die Schichthöhe (z.B. 0.2mm) und Stützstrukturen (falls nötig) eingestellt.
4.  **Druck starten!**
    * Legt das neue Filament in den 3D-Drucker ein.
    * Startet den Druck für alle drei Teile.

> **Achtung: Der Druck dauert lange!**
> Je nach Drucker und Einstellungen kann das Drucken aller Teile **mehrere Stunden (z.B. 4 bis 8 Stunden)** dauern. Wir starten den Druck heute, damit die fertigen Teile morgen (Tag 21) bereit für die Montage sind.

---

### 🧪 Experimentier-Zone (Während der Drucker läuft...)

Du musst stundenlang warten? Perfekte Zeit für einen Code-Check!

* **Challenge 1: Code-Review**
    * Öffne deinen Code von **Tag 16 (Alarm-System)** und **Tag 19 (Nachrichten-Ticker)**.
    * **Frage:** Wie würdest du diese beiden Skripte zu einem **finalen Super-Code** kombinieren? Du brauchst jetzt eine Logik, die den Taster für **vier** Modi umschaltet (z.B. 0=Wetter Innen, 1=Wetter Außen, 2=Licht, 3=News).
* **Challenge 2: 3D-Modell ansehen**
    * Öffne die `.stl`-Dateien in einem 3D-Viewer (Windows hat z.B. den "3D-Viewer" eingebaut).
    * Schau dir genau an, wo die Löcher sind. Kannst du schon erkennen, wo der Pi, das Display und der Taster morgen hingeschraubt werden?
