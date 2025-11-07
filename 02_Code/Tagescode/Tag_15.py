import board
import busio
import adafruit_ssd1306
import adafruit_bme280
import RPi.GPIO as GPIO
import terminalio
from adafruit_display_text import label
import time

# --- PIN & GPIO SETUP ---
TASTER_PIN = 18
LDR_PIN = 14
GPIO.setmode(GPIO.BCM) 
GPIO.setup(TASTER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

# --- I2C BUS SETUP (BME280 & Display) ---
i2c = busio.I2C(board.SCL, board.SDA)
# WICHTIG: Prüfe deine Adressen mit 'i2cdetect -y 1'
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, address=0x3c)

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

# --- DISPLAY SETUP ---
display.fill(0)
display.show()
# Wir erstellen ein großes Textfeld für 2 Zeilen (Tipp: \n)
text_area = label.Label(terminalio.FONT, text="", color=0xFFFFFF, x=0, y=5)
display.show(text_area)

# --- LOGIK-VARIABLE ---
ANZEIGE_MODUS = 0 # 0=Wetter, 1=Umgebung

print("Starte Display-Dashboard! Drücke Taster zum Umschalten. STRG+C zum Stoppen.")

try:
    while True:
        # 1. ALLE SENSOREN LESEN
        temp_C = bme280.temperature
        hum_pct = bme280.humidity
        licht_val = measure_light() # Kleine Zahl = Hell
        
        # 2. TASTER PRÜFEN (Logik von Tag 10)
        if GPIO.input(TASTER_PIN) == GPIO.HIGH:
            if ANZEIGE_MODUS == 0:
                ANZEIGE_MODUS = 1 # Wechsle zu Modus 1
            else:
                ANZEIGE_MODUS = 0 # Wechsle zurück zu Modus 0
            
            print(f"Modus auf {ANZEIGE_MODUS} gewechselt.")
            time.sleep(0.3) # Kurze Pause (Debounce)
        
        # 3. DISPLAY AKTUALISIEREN (Logik von Tag 14)
        if ANZEIGE_MODUS == 0:
            # Modus 0: Zeige Temperatur und Feuchtigkeit
            text_area.text = f"Temp:  {temp_C:.1f} C\nFeuchte: {hum_pct:.0f} %"
        else:
            # Modus 1: Zeige Helligkeit (LDR)
            # (Wir runden den Luftdruck auf 0 Stellen, .0f)
            text_area.text = f"Lichtwert: {licht_val}\n(Je kleiner, desto heller)"
            
        time.sleep(0.1) # Aktualisierungsrate
        
except KeyboardInterrupt:
    print("\nDashboard beendet. Räume Pins auf.")
    display.fill(0)
    display.show()
    GPIO.cleanup()
