import board
import busio
import adafruit_bme280
import RPi.GPIO as GPIO
import time

# --- ALLE PINS DEFINIEREN ---
TASTER_PIN = 18
LDR_PIN = 14

# --- SETUP GPIO ---
GPIO.setmode(GPIO.BCM) 
GPIO.setup(TASTER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

# --- SETUP BME280 SENSOR ---
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76) 

# --- FUNKTION FÜR LICHTMESSUNG (von Tag 9) ---
def measure_light():
    count = 0
    GPIO.setup(LDR_PIN, GPIO.OUT) 
    GPIO.output(LDR_PIN, GPIO.LOW)
    time.sleep(0.1) 
    GPIO.setup(LDR_PIN, GPIO.IN)
    while GPIO.input(LDR_PIN) == GPIO.LOW:
        count += 1
    return count

# --- LOGIK-VARIABLE ---
ANZEIGE_MODUS = 0 # 0=Übersicht, 1=Wetter, 2=Umgebung

print("Starte Super-Dashboard. Drücke Taster zum Umschalten. STRG+C zum Stoppen.")

try:
    while True:
        # 1. ALLE SENSOREN LESEN
        temp_C = round(bme280.temperature, 2)
        hum_pct = round(bme280.humidity, 2)
        press_hPa = round(bme280.pressure, 2)
        licht_val = measure_light() # Kleine Zahl = Hell
        
        # 2. TASTER PRÜFEN (Logik von Tag 10)
        if GPIO.input(TASTER_PIN) == GPIO.HIGH:
            ANZEIGE_MODUS += 1 # Zähle den Modus hoch
            if ANZEIGE_MODUS > 2:
                ANZEIGE_MODUS = 0 # Springe zurück zu Modus 0
            print(f"--- Modus {ANZEIGE_MODUS} ---") # Feedback beim Drücken
            time.sleep(0.3) # Kurze Pause (Debounce)
        
        # 3. DISPLAY ANZEIGEN (Simulation)
        if ANZEIGE_MODUS == 0:
            print(f"ÜBERSICHT: {temp_C}°C | {licht_val} (Licht)")
        elif ANZEIGE_MODUS == 1:
            print(f"WETTER: {press_hPa} hPa | {hum_pct} % Feuchte")
        elif ANZEIGE_MODUS == 2:
            print(f"LICHT-Detail: {licht_val} (Je kleiner, desto heller)")
            
        time.sleep(0.2) # Aktualisierungsrate
        
except KeyboardInterrupt:
    print("\nDashboard beendet. Räume Pins auf.")
    GPIO.cleanup()