
import time
from storage import History
from wifi import connect_wifi
from weather import fetch_weather
from sensor import read_si7021

class App:
    def __init__(self, lcd, sensor, config, display):
        self.lcd = lcd
        self.sensor = sensor
        self.config = config
        self.display = display

        self.history = History(config.HISTORY_SIZE)
        self.last_update = 0

        self.screen = 1
        self.ip = ""

        self.inside = None
        self.outside = None

    def update(self):
        now = time.time()

        if now - self.last_update > self.config.UPDATE_INTERVAL:
            inside = read_si7021(self.sensor)
            outside = fetch_weather(
                self.config.OW_API_KEY,
                self.config.LAT,
                self.config.LON
            )

            self.history.add(
                inside["temp"], inside["humidity"],
                outside["temp"], outside["humidity"]
            )

            self.last_update = now

            self.inside = inside
            self.outside = outside

        return self.inside, self.outside

    def set_screen(self, screen):
        self.screen = screen

    def render(self, inside, outside, now_str):
        if self.screen == 1:
            self.display.draw_dashboard(inside, outside, now_str)

        elif self.screen == 2:
            self.display.draw_graph(
                list(self.history.inside_t),
                list(self.history.inside_h),
                "Indoor"
            )

        elif self.screen == 3:
            self.display.draw_graph(
                list(self.history.outside_t),
                list(self.history.outside_h),
                "Outdoor"
            )

        elif self.screen == 4:
            self.display.draw_status(self.ip)
