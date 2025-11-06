# 01_Anleitungen/Tag_06_Taster-Input.md

## 📅 Tag 6: Der Taster-Input 👆

Guten Morgen! Hast du mit `git pull` schon die heutige Aufgabe geholt?

### 🎁 Inhalt des Türchens

* Ein **Taster** (Druckknopf)
* Ein **10 kOhm Widerstand** (Braun-Schwarz-Orange-Gold)

### 🎯 Das Ziel des Tages

Bisher hat dein Pi nur Befehle *gegeben* (Ausgang/Output), wie "LED an!". Heute lernt er, Befehle zu *empfangen* (Eingang/Input).

Wir bauen einen Taster ein, damit du dem Pi sagen kannst, wann er etwas tun soll. Das ist der erste Schritt, um dein Projekt interaktiv zu machen!

### 💡 Wichtig: Pull-Down-Widerstand

Was passiert mit dem GPIO-Pin, wenn der Taster *nicht* gedrückt ist? Er "schwebt" (floating) in der Luft und weiß nicht, ob er AN (HIGH) oder AUS (LOW) ist. Das führt zu Fehlern.

Damit der Pin immer weiß, was los ist, geben wir ihm einen **Pull-Down-Widerstand**. Dieser Widerstand zieht den Pin sanft auf **GND (LOW)**, wenn der Taster offen ist. Wenn du den Taster drückst, "gewinnt" der starke Strom von den 3.3V und der Pin wird **HIGH**.


### 🔌 Schritte (Hardware)

**WICHTIG: Pi herunterfahren und Stromkabel ziehen!** Die Schaltung von Tag 4/5 (LED an GPIO 17) bleibt bestehen.

1.  **Taster platzieren:**
    * Nimm den **Taster**. Du siehst 4 Beinchen.
    * Setze ihn so auf dein Breadboard, dass er **über dem mittleren Graben** sitzt. Die Beinchen-Paare sollten auf verschiedenen Seiten des Grabens sein.
2.  **Strom für den Taster (3.3V):**
    * Verbinde einen **3.3V Pin** vom Pi (z.B. Pin 1) mit der **roten (+) Schiene** auf dem Breadboard. (Falls du dort noch 5V von Tag 3 hast, tausche das Kabel bitte auf 3.3V aus! Der Taster-Input sollte mit 3.3V laufen).
    * Verbinde ein Beinchen des Tasters (z.B. oben links) mit der **roten (3.3V) Schiene**.
3.  **Daten-Pin (Input):**
    * Nimm ein neues Jumper-Kabel (z.B. grün).
    * Verbinde den **GPIO 18** Pin (Pin 12) vom Pi mit dem *diagonal gegenüberliegenden* Beinchen des Tasters (z.B. unten rechts).
4.  **Pull-Down-Widerstand:**
    * Nimm den **10 kOhm Widerstand**.
    * Stecke ein Ende in dieselbe Reihe wie das Daten-Kabel (**GPIO 18**).
    * Stecke das andere Ende in die **blaue (GND) Schiene**.
5.  **Überprüfen!**
    * Dein Aufbau sollte jetzt so aussehen:
        * **LED-Kreis:** GPIO 17 -> Widerstand -> LED -> GND (von Tag 4)
        * **Taster-Kreis:** 3.3V -> Taster -> (ein Kabel zu GPIO 18) UND (ein 10k Widerstand zu GND)

![](Tag_06_Schaltung.png)


### 💻 Schritte (Software)

1.  **Pi starten** und **Thonny IDE** öffnen.
2.  **Datei öffnen:** `Desktop/Adventskalender_Pi_Tage/Tag_06/Tag_06.py`.
3.  **Code ansehen:** Schau dir den neuen Code an. Wir kombinieren Tag 4 und Tag 6!
    ```python
    import RPi.GPIO as GPIO
    import time
    
    # Unsere Pins definieren
    LED_PIN = 17    # Der Pin für die LED (Output)
    BUTTON_PIN = 18 # Der Pin für den Taster (Input)
    
    GPIO.setmode(GPIO.BCM) 
    
    # Pins einrichten
    GPIO.setup(LED_PIN, GPIO.OUT) 
    # NEU: Pin als EINGANG (IN) definieren
    GPIO.setup(BUTTON_PIN, GPIO.IN) 
    
    print("Drücke den Taster, um die LED zu steuern. STRG+C zum Stoppen.")
    
    try:
        while True:
            # NEU: Den Status des Tasters lesen
            if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
                # Taster ist gedrückt
                print("Taster gedrückt! LED AN.")
                GPIO.output(LED_PIN, GPIO.HIGH)
            else:
                # Taster ist NICHT gedrückt
                GPIO.output(LED_PIN, GPIO.LOW)
            
            time.sleep(0.01) # Eine klitzekleine Pause
            
    except KeyboardInterrupt:
        print("Programm gestoppt. Räume Pins auf.")
        GPIO.cleanup()
    ```
4.  **Code ausführen:** Klicke auf den **grünen Play-Button**.
5.  **Ausprobieren:** Drücke den Taster! Die LED sollte jetzt **nur leuchten, solange du den Taster gedrückt hältst.**
6.  **Stoppen:** Klicke in die Shell (unten) und drücke **STRG + C**.

### 🧪 Experimentier-Zone!

Du hast jetzt einen Input! Was kannst du damit anstellen?

* **Challenge 1: Umgekehrte Welt**
    * **Frage:** Kannst du den Code so ändern, dass die LED **immer an** ist, aber **ausgeht**, wenn du den Taster drückst?
    * **Tipp:** Du musst nur `GPIO.HIGH` und `GPIO.LOW` im `if/else`-Block vertauschen.
* **Challenge 2: Der Blinker-Knopf**
    * **Frage:** Kannst du den Code von **Tag 5 (Blinken)** und **Tag 6** kombinieren? Die LED soll **blinken**, aber *nur*, solange du den Taster gedrückt hältst.
    * **Tipp:** Du musst den Blink-Code (AN, sleep, AUS, sleep) *in* den `if GPIO.input(BUTTON_PIN) == GPIO.HIGH:` Block verschieben.
* **Challenge 3 (Experte): Der Schalter (Toggle)**
    * Das ist knifflig! Kannst du es schaffen, dass die LED **an bleibt**, nachdem du den Taster *einmal* gedrückt (und wieder losgelassen) hast? Und beim *nächsten* Drücken wieder ausgeht?
    * **Tipp:** Du brauchst eine Variable *außerhalb* der Schleife, die sich den Zustand merkt (z.B. `led_an = False`).