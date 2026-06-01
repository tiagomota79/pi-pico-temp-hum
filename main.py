
import time
import machine
from machine import I2C, Pin
from micropython_si7021 import si7021

from lcd import LCD_1inch44
# Init LCD
lcd = LCD_1inch44()

from config import *
from wifi import connect_wifi
import config as config
from display import Display
from app import App

import ntptime

import gc
gc.collect()
print(gc.mem_free())


# Buttons
key0 = Pin(15, Pin.IN, Pin.PULL_UP)
key1 = Pin(17, Pin.IN, Pin.PULL_UP)
key2 = Pin(2, Pin.IN, Pin.PULL_UP)
key3 = Pin(3, Pin.IN, Pin.PULL_UP)

# Sensor
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
sensor = si7021.SI7021(i2c)

# Display & App
display = Display(lcd)
app = App(lcd, sensor, config, display)

# WiFi
app.ip = connect_wifi(SSID, PASSWORD, lcd)

try:
    ntptime.settime()
except:
    pass

UTC_OFFSET = -4 * 3600  # seconds

def read_time():
    t = time.time() + UTC_OFFSET
    t = time.localtime(t)
    return "{:02d}:{:02d}".format(t[3], t[4])

inside = None
outside = None
current_time = "--:--"

while True:
    if not key3.value():
        app.set_screen(1)
        app.render(inside, outside, current_time)
    elif not key2.value():
        app.set_screen(2)
        app.render(inside, outside, current_time)
    elif not key1.value():
        app.set_screen(3)
        app.render(inside, outside, current_time)
    elif not key0.value():
        app.set_screen(4)
        app.render(inside, outside, current_time)

    inside, outside = app.update()

    current_time = read_time()

    if inside is not None and outside is not None:
        app.render(inside, outside, current_time)

    time.sleep(0.1)
