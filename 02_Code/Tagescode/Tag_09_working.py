import RPi.GPIO as GPIO
import time

LDR_PIN = 14 # Der Pin, an dem wir die Ladezeit messen (GPIO 14)

GPIO.setmode(GPIO.BCM) 

def measure_light():
    count = 0
    GPIO.setup(LDR_PIN, GPIO.OUT)
    GPIO.output(LDR_PIN, GPIO.HIGH) # Pin auf HIGH aufladen
    time.sleep(0.1)
    
    GPIO.setup(LDR_PIN, GPIO.IN) # Auf Input setzen
    # Messen, wie lange er braucht, um LOW zu werden
    # (Dieser Code funktioniert, wenn der LDR zwischen PIN und GND hängt)
    while GPIO.input(LDR_PIN) == GPIO.HIGH:
        count += 1
    return count

print("Starte Helligkeitsmessung... Drücke STRG+C zum Stoppen.")

try:
    while True:
        ladezeit = measure_light()
        
        # Je niedriger die Zahl, desto heller ist es!
        print(f"☀️ Ladezeit: {ladezeit} (Wertebereich: ca. 100 bis 5000)")
        
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print("\nMessung beendet. Räume Pins auf.")
    GPIO.cleanup()