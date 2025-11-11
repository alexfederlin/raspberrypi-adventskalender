import board
import displayio
import time

# from fourwire import FourWire
import terminalio
from adafruit_display_text import label
from i2cdisplaybus import I2CDisplayBus

import adafruit_displayio_ssd1306

displayio.release_displays()

oled_reset = board.D9

# Use for I2C
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
display_bus = I2CDisplayBus(i2c, device_address=0x3C, reset=oled_reset)

# Use for SPI
# spi = board.SPI()
# oled_cs = board.D5
# oled_dc = board.D6
# display_bus = FourWire(spi, command=oled_dc, chip_select=oled_cs,
#                                 reset=oled_reset, baudrate=1000000)

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 4

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.root_group = splash

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1)
splash.append(text_area)

print("Schau auf dein OLED-Display! Es sollte 'Hallo Welt!' anzeigen.")

# Wir lassen es 10 Sekunden an, bevor das Programm endet
time.sleep(10)
display.root_group = None

print("Programm beendet.")
