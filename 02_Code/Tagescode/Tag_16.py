# (Alle Importe und Setups von Tag 15 sind hier oben)
import board
import busio
import adafruit_ssd1306
import adafruit_bme280
import RPi.GPIO as GPIO
import terminalio
from adafruit_display_text import label
import time

# --- ALLE PINS DEFINIEREN ---
TASTER_PIN = 18
LDR_PIN = 14
LED_PIN = 17    # NEU!
SUMMER_PIN = 23 # NEU!

# --- GRENZWERTE FÜR ALARME (Hier kannst du experimentieren!) ---
LICHT_GRENZE = 1000  # Ab diesem LDR-Wert (dunkel) geht die LED an
HITZE_GRENZE = 27.0  # Ab dieser Temperatur (in °C) piept der Summer

# --- SETUP GPIO ---
GPIO.setmode(GPIO.BCM) 
GPIO.setup(TASTER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(LED_PIN, GPIO.OUT)    # NEU!
GPIO.setup(SUMMER_PIN, GPIO.OUT) # NEU!

# --- I2C BUS SETUP (BME280 & Display) ---
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, address=0x3c)

# --- FUNKTION FÜR LICHTMESSUNG (von Tag 9) ---
def measure_light():
    # (Hier steht die LDR-Funktion von Tag 9)
    count = 0
    GPIO.setup(LDR_PIN, GPIO.OUT); GPIO.output(LDR_PIN, GPIO.LOW)
    time.sleep(0.1); GPIO.setup(LDR_PIN, GPIO.IN)
    while GPIO.input(LDR_PIN) == GPIO.LOW: count += 1
    return count

# --- DISPLAY SETUP (von Tag 15) ---
display.fill(0); display.show()
text_area = label.Label(terminalio.FONT, text="", color=0xFFFFFF, x=0, y=5)
display.show(text_area)
ANZEIGE_MODUS = 0 

print("Starte Alarm-System! Drücke Taster zum Umschalten. STRG+C zum Stoppen.")

try:
    while True:
        # 1. ALLE SENSOREN LESEN
        temp_C = bme280.temperature
        hum_pct = bme280.humidity
        licht_val = measure_light()
        
        # 2. TASTER FÜR DISPLAY PRÜFEN (Logik von Tag 15)
        if GPIO.input(TASTER_PIN) == GPIO.HIGH:
            ANZEIGE_MODUS = 1 - ANZEIGE_MODUS # Ein cleverer Trick, um 0 und 1 zu wechseln
            print(f"Modus auf {ANZEIGE_MODUS} gewechselt.")
            time.sleep(0.3) 
        
        # 3. DISPLAY AKTUALISIEREN (Logik von Tag 15)
        if ANZEIGE_MODUS == 0:
            text_area.text = f"Temp:  {temp_C:.1f} C\nFeuchte: {hum_pct:.0f} %"
        else:
            text_area.text = f"Lichtwert: {licht_val}\n(Dunkel > {LICHT_GRENZE})"
        
        # 4. NEU: ALARME PRÜFEN (laufen immer!)
        
        # Alarm A: Nachtlicht-Logik
        if licht_val > LICHT_GRENZE:
            GPIO.output(LED_PIN, GPIO.HIGH) # Dunkel -> LED AN
        else:
            GPIO.output(LED_PIN, GPIO.LOW) # Hell -> LED AUS
            
        # Alarm B: Hitze-Alarm-Logik
        if temp_C > HITZE_GRENZE:
            GPIO.output(SUMMER_PIN, GPIO.HIGH) # Zu heiß -> Piepen!
        else:
            GPIO.output(SUMMER_PIN, GPIO.LOW) # OK -> Still
            
        time.sleep(0.1) # Kurze Pause, damit der Pi atmen kann
        
except KeyboardInterrupt:
    print("\nSystem beendet. Räume Pins auf.")
    display.fill(0); display.show()
    GPIO.cleanup()
