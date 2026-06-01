
import urequests
import gc

def fetch_weather(api_key, lat, lon):
    url = ("http://api.openweathermap.org/data/2.5/weather"
           f"?lat={lat}&lon={lon}&appid={api_key}&units=metric")

    r = urequests.get(url)
    data = r.json()
    r.close()
    gc.collect()

    return {
        "temp": round(data["main"]["temp"], 1),
        "feels_like": round(data["main"]["feels_like"], 1),
        "humidity": round(data["main"]["humidity"], 1),
    }
