
def read_si7021(sensor):
    return {
        "temp": round(sensor.temperature, 1),
        "humidity": round(sensor.humidity, 1),
    }
