import RPi.GPIO as GPIO
import time

# Pin für den Summer festlegen
SUMMER_PIN = 23 # GPIO 23 (Pin 16)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SUMMER_PIN, GPIO.OUT)

print("Starte den Sound-Test...")

try:
    print("Piep!")
    GPIO.output(SUMMER_PIN, GPIO.HIGH) # AN
    time.sleep(0.5) # Eine halbe Sekunde piepen
    
    print("Stille.")
    GPIO.output(SUMMER_PIN, GPIO.LOW) # AUS
    
    time.sleep(1) # Kurze Pause
    
    # Noch ein paar Piepser
    print("Doppel-Piep!")
    GPIO.output(SUMMER_PIN, GPIO.HIGH); time.sleep(0.1) # Kurz AN
    GPIO.output(SUMMER_PIN, GPIO.LOW); time.sleep(0.1) # Kurz AUS
    GPIO.output(SUMMER_PIN, GPIO.HIGH); time.sleep(0.1) # Kurz AN
    GPIO.output(SUMMER_PIN, GPIO.LOW) # Wieder AUS
        
    print("\nTest beendet. Räume Pins auf.")
    GPIO.cleanup()
    
except KeyboardInterrupt:
    # Falls du das Programm abbrichst
    GPIO.cleanup()
