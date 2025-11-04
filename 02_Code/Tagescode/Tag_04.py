import RPi.GPIO as GPIO
import time

# Den Pin festlegen (nach GPIO-Nummer)
LED_PIN = 17 

# GPIO-Modus setzen
GPIO.setmode(GPIO.BCM) 
# Den LED-Pin als AUSGANG (OUT) definieren
GPIO.setup(LED_PIN, GPIO.OUT) 

print("LED wird eingeschaltet...")
# Den Pin auf HIGH (Strom AN) setzen
GPIO.output(LED_PIN, GPIO.HIGH) 

# Wir warten 10 Sekunden, damit du sie leuchten siehst
time.sleep(10) 

print("Programm beendet. LED bleibt an.")
# Am Ende räumen wir die Pins auf (wichtig!)
GPIO.cleanup() 
print("Pins aufgeräumt. LED geht aus.")