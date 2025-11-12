import board
import displayio
import time
# WICHTIG: Die Bibliotheken für den BME280 müssen importiert werden
import busio 
import adafruit_bme280

import terminalio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus

import adafruit_displayio_ssd1306

# --- Initialisierung ---

displayio.release_displays()

# Pin-Definitionen
oled_reset = board.D9
# I²C-Bus initialisieren (wird für Display und BME280 genutzt)
i2c = board.I2C()  # uses board.SCL and board.SDA

# --- 1. BME280 Sensor initialisieren (NEU) ---
try:
    # Sensor am I²C-Bus finden
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    # Optional: Einstellungen anpassen
    bme280.sea_level_pressure = 1013.25 # Beispiel für Meereshöhe
    print("BME280 Sensor initialisiert.")
except ValueError:
    print("FEHLER: BME280 Sensor nicht gefunden (prüfe Adressierung/Verkabelung).")
    # Stelle sicher, dass das Programm trotzdem weiterläuft, falls der Sensor fehlt
    bme280 = None 


# --- 2. OLED Display initialisieren (Wie Tag 13) ---

display_bus = I2CDisplayBus(i2c, device_address=0x3C, reset=oled_reset)

WIDTH = 128
HEIGHT = 32 

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Erstelle die Display-Gruppe
splash = displayio.Group()
display.root_group = splash

# Definiere das Label Objekt
# Wir lassen den Text zunächst leer und zentrieren das Label
text_area = label.Label(terminalio.FONT, text="", color=0xFFFFFF, x=0, y=15)

# Füge das Label der Display-Gruppe hinzu
splash.append(text_area)

print("Starte kontinuierliche Messung und Anzeige. Drücke STRG+C zum Stoppen.")

# --- 3. Hauptschleife zur Aktualisierung ---
try:
    while True:
        if bme280 is not None:
            # Temperaturwert auslesen
            temperatur = bme280.temperature
            luftfeuchte = bme280.relative_humidity
            
            # Text formatieren
            anzeige_text = f"Temp: {temperatur:.1f} °C\nFeucht: {luftfeuchte:.1f} %"
            
            # Label auf dem Display aktualisieren
            text_area.text = anzeige_text
            
            # Ausgabe auf der Konsole zur Kontrolle
            print(f"Aktualisiert: {anzeige_text.replace('\n', ' | ')}")
            
        else:
            # Fehlermeldung anzeigen, falls Sensor fehlt
            text_area.text = "BME280 FEHLER"
            print("Warte auf BME280-Sensor...")

        # Warte 2 Sekunden vor der nächsten Aktualisierung
        time.sleep(2.0)

except KeyboardInterrupt:
    print("\nProgramm beendet. Räume auf.")
finally:
    # Lösche das Display, bevor das Programm endet
    display.root_group = None
    time.sleep(1) 
    print("Display gelöscht.")