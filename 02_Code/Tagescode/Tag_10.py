import board
import busio
import adafruit_bme280
import RPi.GPIO as GPIO
import time

# --- PINS und Setup ---
TASTER_PIN = 18 # Pin des Tasters (GPIO 18)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(TASTER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

# --- Logik-Variable ---
ANZEIGE_MODUS = 0 # 0 = Temperatur, 1 = Luftdruck

# --- Sensor Setup ---
i2c = busio.I2C(board.SCL, board.SDA)
# WICHTIG: Prüfe, ob du 0x76 oder 0x77 brauchst!
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76) 

print("Starte Display-Simulation. Drücke den Taster zum Umschalten!")

try:
    while True:
        # 1. Sensorwerte lesen
        temp_C = round(bme280.temperature, 2)
        hum_pct = round(bme280.humidity, 2)
        press_hPa = round(bme280.pressure, 2)
        
        # 2. Terminal 'leeren' für die Simulation
        # Dies simuliert, dass das Display neu gezeichnet wird
        print("-" * 30) 
        
        # 3. Logik: Prüfe Taster und wechsle Modus
        if GPIO.input(TASTER_PIN) == GPIO.HIGH:
            # Taster wurde gedrückt
            if ANZEIGE_MODUS == 0:
                ANZEIGE_MODUS = 1 # Umschalten von Temp auf Druck
            else:
                ANZEIGE_MODUS = 0 # Umschalten von Druck auf Temp
            
            # Kurze Pause (Debounce), damit der Taster nicht 10x umschaltet
            time.sleep(0.3) 
        
        # 4. Anzeige-Logik (Display-Simulation)
        if ANZEIGE_MODUS == 0:
            print(f"MODUS: TEMPERATUR")
            print(f"🌡️ {temp_C} °C")
        else:
            print(f"MODUS: LUFTDRUCK")
            print(f"💨 {press_hPa} hPa")

        # In jedem Modus die Luftfeuchte anzeigen
        print(f"💧 Luftfeuchte: {hum_pct} %") 
        
        time.sleep(0.5) # Kurze Wartezeit vor dem nächsten Durchlauf
        
except KeyboardInterrupt:
    print("\nSimulation beendet. Räume Pins auf.")
    GPIO.cleanup()