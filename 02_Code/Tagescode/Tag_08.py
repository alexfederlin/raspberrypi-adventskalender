import board
import busio
import adafruit_bme280
import time

# 1. I2C Bus initialisieren (SDA=GPIO 2, SCL=GPIO 3)
i2c = busio.I2C(board.SCL, board.SDA)

# 2. Sensor initialisieren
# HINWEIS: Prüfe, ob deine Adresse 0x76 oder 0x77 ist!
# Wenn der Code fehlschlägt, versuche: bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x77)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76) 

print("Starte Messung... Drücke STRG+C zum Stoppen.")

try:
    while True:
        # Werte auslesen und runden (z.B. 25.4 statt 25.4385...)
        temp_C = round(bme280.temperature, 2)
        hum_pct = round(bme280.humidity, 2)
        press_hPa = round(bme280.pressure, 2)

        print("---")
        print(f"🌡️ Temperatur: {temp_C} °C")
        print(f"💧 Luftfeuchte: {hum_pct} %")
        print(f"💨 Luftdruck:  {press_hPa} hPa")
        
        time.sleep(5) # Alle 5 Sekunden messen
        
except KeyboardInterrupt:
    print("\nMessung beendet.")
