import board
import displayio
import time
# WICHTIG: Die Bibliotheken für den BME280 müssen importiert werden
from adafruit_bme280 import basic as adafruit_bme280


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
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
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

# Die Schriftgröße des terminalio.FONT ist ca. 13 Pixel hoch.
# Zeile 1: Temperatur (Oben)
temp_label = label.Label(terminalio.FONT, text="Temp:", color=0xFFFFFF, x=5, y=5)

# Zeile 2: Luftfeuchtigkeit (Unten)
# y=5 + 13 Pixel Höhe + etwas Abstand = ca. 20
humidity_label = label.Label(terminalio.FONT, text="Feucht:", color=0xFFFFFF, x=5, y=19)

# Füge beide Labels der Display-Gruppe hinzu
splash.append(temp_label)
splash.append(humidity_label)

print("Starte kontinuierliche Messung und Anzeige. Drücke STRG+C zum Stoppen.")

# --- 3. Hauptschleife zur Aktualisierung ---
try:
    while True:

        if bme280 is not None:
            # Werte auslesen
            temperatur = bme280.temperature
            luftfeuchte = bme280.relative_humidity
            
            # Label-Texte separat aktualisieren
            temp_label.text = f"Temp: {temperatur:.1f} °C"
            humidity_label.text = f"Feucht: {luftfeuchte:.1f} %"
            
            # Ausgabe auf der Konsole zur Kontrolle
            print(f"Aktualisiert: {temp_label.text} | {humidity_label.text}")
            
        else:
            # Fehlermeldung anzeigen, falls Sensor fehlt
            text_area.text = "BME280 FEHLER"
            print("Warte auf BME280-Sensor...")

        display.root_group = None

        display.root_group = splash

        # Warte 2 Sekunden vor der nächsten Aktualisierung
        time.sleep(2.0)

except KeyboardInterrupt:
    print("\nProgramm beendet. Räume auf.")

# Lösche das Display, bevor das Programm endet
display.root_group = None
#time.sleep(1) 
print("Display gelöscht.")
    
    