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