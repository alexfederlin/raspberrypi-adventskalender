# 02_Code/Tagescode/Tag_05_LED_Blink.py

import RPi.GPIO as GPIO
import time

# Pin-Nummerierung auf BCM festlegen (GPIO-Nummerierung)
GPIO.setmode(GPIO.BCM)

# Den GPIO-Pin festlegen, an den die LED angeschlossen ist (z.B. GPIO 17)
LED_PIN = 17

# Pin als Ausgang (OUT) konfigurieren
GPIO.setup(LED_PIN, GPIO.OUT)

print("Starte den LED-Blink-Test. Beende mit STRG+C")

try:
    while True:
        # LED einschalten (High)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)  # 0.5 Sekunden warten
        
        # LED ausschalten (Low)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)  # 0.5 Sekunden warten

except KeyboardInterrupt:
    # Aufräumen, wenn das Programm mit STRG+C beendet wird
    print("Programm beendet. GPIO wird aufgeräumt.")
    GPIO.cleanup()