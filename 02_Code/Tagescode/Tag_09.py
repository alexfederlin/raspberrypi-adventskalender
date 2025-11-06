import RPi.GPIO as GPIO
import time

LDR_PIN = 14 # Der Pin, an dem wir die Ladezeit messen (GPIO 14)

GPIO.setmode(GPIO.BCM) 

def measure_light():
    # Zähler auf Null setzen
    count = 0
    
    # 1. Den Pin entladen (auf LOW setzen)
    GPIO.setup(LDR_PIN, GPIO.OUT) 
    GPIO.output(LDR_PIN, GPIO.LOW)
    time.sleep(0.1) # Kurz warten, um sicherzustellen, dass er leer ist
    
    # 2. Den Pin auf INPUT umstellen und die Ladezeit messen
    GPIO.setup(LDR_PIN, GPIO.IN)
    
    # Zähle, wie lange es dauert, bis der Pin HIGH wird (geladen ist)
    while GPIO.input(LDR_PIN) == GPIO.LOW:
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