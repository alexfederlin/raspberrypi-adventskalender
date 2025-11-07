import board
import busio
import adafruit_ssd1306
import adafruit_bme280
import terminalio
from adafruit_display_text import label
import time

# --- I2C Bus Setup (wie bei Tag 8 & 13) ---
i2c = busio.I2C(board.SCL, board.SDA)

# --- BEIDE GERÄTE initialisieren ---
# WICHTIG: Prüfe deine Adressen mit 'i2cdetect -y 1'
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, address=0x3c)

# Display löschen (alles schwarz machen)
display.fill(0)
display.show()

# --- Text-Label erstellen ---
# Wir erstellen ein leeres Textfeld oben links (x=0, y=5)
text_area = label.Label(terminalio.FONT, text="", color=0xFFFFFF, x=0, y=5)
# Und zeigen es auf dem Display an
display.show(text_area)

print("Starte Live-Temperatur-Anzeige auf dem OLED! STRG+C zum Stoppen.")

try:
    # --- Endlos-Schleife für Live-Daten ---
    while True:
        # 1. Sensor auslesen
        temp_C = bme280.temperature
        
        # 2. Zahl in Text umwandeln (mit f-String)
        # Wir runden auf eine Nachkommastelle (.1f)
        text_fuer_display = f"Temperatur: {temp_C:.1f} C"
        
        # 3. Den Text im Label aktualisieren
        text_area.text = text_fuer_display
        
        # Kurze Pause
        time.sleep(1) # Aktualisiert jede Sekunde

except KeyboardInterrupt:
    # Am Ende wieder alles löschen
    display.fill(0)
    display.show()
    print("\nAnzeige beendet.")