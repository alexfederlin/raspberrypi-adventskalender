import board
import time
from adafruit_bme280 import basic as adafruit_bme280

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()   # uses board.SCL and board.SDA
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
