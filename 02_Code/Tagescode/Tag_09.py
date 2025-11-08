import RPi.GPIO as GPIO
import time

# Der Pin, an dem wir die Ladezeit messen
LDR_PIN = 14 
# Maximaler Zähler, bevor das Programm abbricht (Timeout)
# Dieser Wert ist der Schwellenwert für "zu dunkel"
MAX_COUNT = 5000 

GPIO.setmode(GPIO.BCM) 

def measure_light():
    # Zähler auf Null setzen
    count = 0
    
    # 1. Kondensator entladen (auf LOW setzen)
    GPIO.setup(LDR_PIN, GPIO.OUT) 
    GPIO.output(LDR_PIN, GPIO.HIGH)
    time.sleep(0.1) # Kurz warten, um sicherzustellen, dass er leer ist
    
    # 2. Pin auf INPUT umstellen und die Ladezeit messen
    # Die 3.3V laden den Kondensator über den LDR/Widerstand auf
    GPIO.setup(LDR_PIN, GPIO.IN)
    
    # Zähle, wie lange es dauert, bis der Pin HIGH wird (geladen ist)
    while GPIO.input(LDR_PIN) == GPIO.HIGH:
        count += 1
        
        # Sicherstellen, dass die Schleife bei extrem hohen Werten abbricht
        if count >= MAX_COUNT:
            break
            
    return count

print("Starte Helligkeitsmessung... Drücke STRG+C zum Stoppen.")

try:
    while True:
        ladezeit = measure_light()
        
        # Prüfen, ob der Zähler den maximalen Wert erreicht hat (zu dunkel)
        if ladezeit >= MAX_COUNT:
            print("🌑 Ladezeit: zu dunkel (MAX_COUNT erreicht)")
            # Hier warten wir 1 Sekunde, um die Ausgabe zu verlangsamen
            time.sleep(1.0)
        else:
            # Ausgabe des tatsächlichen Werts
            # WICHTIG: Je KLEINER die Zahl, desto HELLER ist es!
            print(f"☀️ Ladezeit: {ladezeit} (Normaler Messbereich)")
            # Hier warten wir die Standard-0.5 Sekunden
            time.sleep(0.5)
            
except KeyboardInterrupt:
    print("\nMessung beendet. Räume Pins auf.")
    GPIO.cleanup()