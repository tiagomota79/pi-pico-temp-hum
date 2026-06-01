# Raspberry Pi Pico Temperature and Humidity

## The Project

Simple temperature and humidity station with internal and external values and trend graphs.

## Materials

- Raspberry Pi Pico W
  - Not tested on Pi Pico 2, but likely to work as is
- Adafruit Si7021 Temperature & Humidity Sensor Breakout Board - STEMMA QT
- Waveshare 1.44inch LCD Display Module for Raspberry Pi Pico, 65K Colors, 128x128, SPI

## Wiring

                    Raspberry Pi Pico W
             ┌───────────────────────────┐
             │                           │
             │ GP0  ───────────── SDA ───┼──── Si7021 SDA
             │ GP1  ───────────── SCL ───┼──── Si7021 SCL
             │ 3V3  ─────────────────────┼──── Si7021 VIN
             │ GND  ─────────────────────┼──── Si7021 GND
             │                           │
             │ GP10 ───────────── SCK ───┼──── LCD CLK
             │ GP11 ──────────── MOSI ───┼──── LCD DIN
             │ GP12 ───────────── RST ───┼──── LCD RST
             │ GP13 ───────────── BL  ───┼──── LCD BL
             │ GP8  ───────────── DC  ───┼──── LCD DC
             │ GP9  ───────────── CS  ───┼──── LCD CS
             │ 3V3  ─────────────────────┼──── LCD VCC
             │ GND  ─────────────────────┼──── LCD GND
             │                           │
             │ GP3  ─────────── KEY3 ────┼──── LCD Button A
             │ GP2  ─────────── KEY2 ────┼──── LCD Button B
             │ GP17 ─────────── KEY1 ────┼──── LCD Button X
             │ GP15 ─────────── KEY0 ────┼──── LCD Button Y
             │                           │
             └───────────────────────────┘

## How it works

There are four screens:
- Screen 1 and initial screen: Displays inside outside temperature and humidity, with external feels like temperature, and the time of the last update.
<img width="3024" height="1793" alt="IMG_5320" src="https://github.com/user-attachments/assets/88da49dc-90dc-4123-8541-897013083dd9" />

- Screen 2: Indoor temperature and humidity graph, showing the last 10 measumerents.
<img width="3024" height="1784" alt="IMG_5322" src="https://github.com/user-attachments/assets/6e701f54-ef69-4a27-a9dc-dd272ab99d65" />

- Screen 3: Outdoor temperature and humidity graph, showing the last 10 measumerents.
<img width="3024" height="1791" alt="IMG_5323" src="https://github.com/user-attachments/assets/22e2e6fd-1979-4189-b930-ed9621c40afd" />

- Screen 4: Wifi status and device IP.
<img width="3024" height="2034" alt="IMG_5321" src="https://github.com/user-attachments/assets/dc297110-2feb-41c2-b102-4f270c5e6419" />


There is an initial screen shown while the device is connecting to the WiFi.

Change the screens using the buttons in the LCD screen. Due to the screen default orientation, the buttons number are opposite to the screen numbers:
- Key 3: Screen 1
- Key 2: Screen 2
- Key 1: Screen 3
- Key 0: Screen 4

For the device to correctly show the temperature in your local, you need yout latitude and longitude values, as well as an OpenWeather API key.

## Known limitations

The last update time is calculated manually from UTC, with no automatic change for Daylight Saving Time.
