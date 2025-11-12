import board
import displayio
import time

import terminalio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus

import adafruit_displayio_ssd1306

displayio.release_displays()

oled_reset = board.D9

# Use for I2C
i2c = board.I2C()  # uses board.SCL and board.SDA

display_bus = I2CDisplayBus(i2c, device_address=0x3C, reset=oled_reset)

WIDTH = 128
HEIGHT = 32 

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Erstelle die Display-Gruppe
splash = displayio.Group()
display.root_group = splash

# Definiere den Text
text = "Hello World!"

# Definiere das Label Objekt mit Text und Position
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=15)

# Füge das Label der Display-Gruppe hinzu
splash.append(text_area)

print("Schau auf dein OLED-Display! Es sollte 'Hallo Welt!' anzeigen.")

# Wir lassen es 10 Sekunden an, bevor das Programm endet
time.sleep(10)

# Lösche das Display
display.root_group = None

print("Programm beendet.")
