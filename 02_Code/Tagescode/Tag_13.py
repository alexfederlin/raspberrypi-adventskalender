import board
import busio
import adafruit_ssd1306
import terminalio
from adafruit_display_text import label
import time

# Gibt alle alten Displays frei, falls das Skript mal abgestürzt ist
# displayio.release_displays() 
# (Oben auskommentiert, brauchen wir meist nicht, aber gut zu wissen)

# --- I2C Bus Setup (wie bei Tag 8) ---
i2c = busio.I2C(board.SCL, board.SDA)

# --- Display Setup (Adresse 0x3c ist üblich) ---
# Wir sagen ihm explizit, dass er das Display (0x3c) nehmen soll
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, address=0x3c)

# Display löschen (alles schwarz machen)
display.fill(0)
display.show()

# --- Text erstellen ---
text = "Hallo Welt!"
# Wir benutzen eine eingebaute Schriftart (terminalio.FONT)
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=30)

# --- Text anzeigen ---
display.show(text_area)

print("Schau auf dein OLED-Display! Es sollte 'Hallo Welt!' anzeigen.")

# Wir lassen es 10 Sekunden an, bevor das Programm endet
time.sleep(10)

# Display am Ende wieder löschen
display.fill(0)
display.show()
print("Programm beendet.")
