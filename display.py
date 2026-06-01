
import framebuf

class Display:
    def __init__(self, lcd):
        self.lcd = lcd

    def clear(self):
        self.lcd.fill(self.lcd.BLACK)

    def draw_dashboard(self, i, o, t):
        self.clear()

        
        self.lcd.fill_rect(0, 0, 128, 50, self.lcd.BLUE)
        self.lcd.text("INSIDE", 40, 5, self.lcd.WHITE)
        self.lcd.text(f"{i['temp']}C", 10, 20, self.lcd.WHITE)
        self.lcd.text(f"{i['humidity']}%", 10, 35, self.lcd.WHITE)
        self.lcd.fill_rect(0, 52, 128, 75, self.lcd.GREEN)
        self.lcd.text("OUTSIDE", 40, 55, self.lcd.BLACK)
        self.lcd.text(f"T:{o['temp']}C", 5, 75, self.lcd.BLACK)
        self.lcd.text(f"F:{o['feels_like']}C", 5, 90, self.lcd.BLACK)
        self.lcd.text(f"{o['humidity']}%", 5, 105, self.lcd.BLACK)
        self.lcd.text(f"Last {t}", 20, 118, self.lcd.BLACK)
        self.lcd.show()

    def draw_graph(self, values_t, values_h, title):
        self.clear()
        self.lcd.text(title, 40, 0, self.lcd.WHITE)

        if len(values_t) < 2:
            self.lcd.text("Not", 10, 50, self.lcd.WHITE)
            self.lcd.text("enough", 10, 60, self.lcd.WHITE)
            self.lcd.text("data", 10, 70, self.lcd.WHITE)
            self.lcd.show()
            return

        def scale(v, vmin, vmax):
            return 120 - int((v - vmin) * 80 / (vmax - vmin + 0.01))

        vmin = min(values_t + values_h)
        vmax = max(values_t + values_h)

        for i in range(len(values_t) - 1):
            x1 = i * 12
            x2 = (i + 1) * 12

            y1 = scale(values_t[i], vmin, vmax)
            y2 = scale(values_t[i + 1], vmin, vmax)

            self.lcd.text("T", 2, 100, self.lcd.RED)
            self.lcd.line(x1, y1, x2, y2, self.lcd.RED)

            y1h = scale(values_h[i], vmin, vmax)
            y2h = scale(values_h[i + 1], vmin, vmax)

            self.lcd.text("H", 2, 20, self.lcd.BLUE)
            self.lcd.line(x1, y1h, x2, y2h, self.lcd.BLUE)

        self.lcd.show()

    def draw_status(self, ip, wifi_ok=True):
        self.clear()
        self.lcd.text("STATUS", 40, 10, self.lcd.WHITE)
        self.lcd.text(f"WiFi {'OK' if wifi_ok else 'FAIL'}", 10, 40, self.lcd.WHITE)
        self.lcd.text(f"IP:", 10, 60, self.lcd.WHITE)
        self.lcd.text(ip, 10, 70, self.lcd.WHITE)
        self.lcd.show()
