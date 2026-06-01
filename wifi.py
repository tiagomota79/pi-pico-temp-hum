
import network
import time
# from picozero import pico_led

def connect_wifi(ssid, password, lcd):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        # pico_led.on()
        # time.sleep(0.2)
        # pico_led.off()
        # time.sleep(0.2)

        lcd.fill(lcd.BLACK)
        lcd.text("Connecting WiFi", 10, 50, lcd.WHITE)
        lcd.text("Please wait...", 10, 65, lcd.WHITE)
        lcd.show()

    # pico_led.on()
    ip = wlan.ifconfig()[0]
    return ip
