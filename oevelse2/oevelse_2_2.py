from machine import Pin, deepsleep
from random import choice
from neopixel import NeoPixel
from time import sleep
"""
2.2 - Prøv at vække ESP32 fra deepsleep med en timer,
og kør en funktion der sætter en random farve på
educaboardets neopixels LED4 og LED5 hver gang ESP32 vækkes fra deepsleep.
"""

PIXEL_AMOUNT = 2
PIXEL_GPIO = 26
np = NeoPixel(Pin(PIXEL_GPIO, Pin.OUT), PIXEL_AMOUNT)
# list with colors on or off
colors = [255, 0]
# set first pixel where R, G, B each gets random value of 255 or 0
np[0] = (choice(colors),choice(colors),choice(colors))
# set second pixel where R, G, B each gets random value of 255 or 0
np[1] = (choice(colors),choice(colors),choice(colors))
np.write()
# sleep is inserted to more easely stop the program between deepsleep
sleep(1) 
# goint to deepsleep for 1000 miliseconds
deepsleep(1000)