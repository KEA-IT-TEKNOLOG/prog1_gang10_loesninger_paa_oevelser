from hcsr04 import HCSR04
from machine import Pin
from time import ticks_ms, sleep_ms

usonic = HCSR04(trigger_pin=15, echo_pin=34, echo_timeout_us=10000)

start = ticks_ms()
delay_ms = 300

while True:
    if ticks_ms() - start > delay_ms:
        print(usonic.distance_cm())
        start = ticks_ms()
    sleep_ms(10)