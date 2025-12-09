
from machine import Pin, I2C, UART
import time
import network
import urequests
import ujson
import gc
from ssd1306 import SSD1306_I2C

WIFI_PASS = "david270"
API_KEY = "36c636fb1519964da8ba93fae771f778"

WEATHER_INTERVAL = 20

gps_uart = UART(2, baudrate=9600, tx=17, rx=16)

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

OW_URL = "https://api.openweathermap.org/data/2.5/weather

def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active():
        wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(WIFI_SSID, WIFI_PASS)
        count = 0
        while not wlan.isconnected() and count < 30:
            time.sleep(1)
            count += 1
    return wlan.isconnected()

def wifi_status():
    wlan = network.WLAN(network.STA_IF)
    return wlan.isconnected()

def obtener_clima(lat, lon):
    try:
        url = "{}?lat={}&lon={}&appid={}&units=metric&lang=es".format(OW_URL, lat, lon, API_KEY)
        resp = urequests.get(url)
        data = resp.json()
        resp.close()
        temp = None
        desc = None
        if "main" in data and "temp" in data["main"]:
            temp = data["main"]["temp"]
        if "weather" in data and len(data["weather"])>0:
            desc = data["weather"][0].get("description", "")
        return temp, desc, data
    except Exception as e:
        print("Error clima:", e)
        return None, None, None

def nmea_to_decimal(coord, direction):
    try:
        if coord == "" or coord is None:
            return None
        f = float(coord)
        if f == 0.0:
            return None
        if len(coord.split('.')[0]) > 4:  
            deg = int(f / 100)
            minutes = f - deg*100
        else:  
            deg = int(f / 100)
            minutes = f - deg*100
        dec = deg + minutes/60.0
        if direction in ('S','W'):
            dec = -dec
        return dec
    except Exception as e:
        return None

def parse_nmea(sentence):
    try:
        s = sentence.strip()
        if not s.startswith('$'):
            return None
        parts = s.split(',')
        tag = parts[0][3:]
        if tag == "GGA":
            lat_raw = parts[2]
            lat_dir = parts[3]
            lon_raw = parts[4]
            lon_dir = parts[5]
            sats = parts[7]
            lat = nmea_to_decimal(lat_raw, lat_dir)
            lon = nmea_to_decimal(lon_raw, lon_dir)
            return {"type":"GGA","lat":lat,"lon":lon,"sats":sats}
        if tag == "RMC":
            status = parts[2]
            if status != 'A':
                return None
            lat_raw = parts[3]
            lat_dir = parts[4]
            lon_raw = parts[5]
            lon_dir = parts[6]
            lat = nmea_to_decimal(lat_raw, lat_dir)
            lon = nmea_to_decimal(lon_raw, lon_dir)
            return {"type":"RMC","lat":lat,"lon":lon}
    except Exception as e:
        return None

def mostrar_oled(lat, lon, sats, temp, desc, wifi_ok):
    oled.fill(0)
    oled.text("GPS + CLIMA", 0, 0)
    if lat is not None and lon is not None:
        oled.text("Lat:{:.5f}".format(lat), 0, 12)
        oled.text("Lon:{:.5f}".format(lon), 0, 24)
    else:
        oled.text("Lat: --", 0, 12)
        oled.text("Lon: --", 0, 24)
    oled.text("Sats: {}".format(sats if sats is not None else "-"), 0, 36)
    if temp is not None:
        oled.text("T:{:.1f}C".format(temp), 0, 48)
        if desc:
            oled.text(desc[:15], 64, 48)
    else:
        oled.text("Clima: --", 0, 48)
    if not wifi_ok:
        oled.text("WiFi:OFF", 64, 0)
    oled.show()

def main():
    last_weather_time = 0
    last_lat = None
    last_lon = None
    last_sats = None
    temp = None
    desc = None

    oled.fill(0)
    oled.text("Iniciando...", 0, 0)
    oled.show()

    wifi_ok = conectar_wifi()
    print("WiFi conectado:", wifi_ok)

    mostrar_oled(None, None, None, None, None, wifi_ok)
    time.sleep(1)

    buffer = b""
    while True:
        try:
            if gps_uart.any():
                data = gps_uart.readline()
                if not data:
                    continue
                try:
                    line = data.decode('utf-8', 'ignore').strip()
                except:
                    continue

                parsed = parse_nmea(line)
                if parsed:
                    if parsed.get("lat") is not None and parsed.get("lon") is not None:
                        last_lat = parsed.get("lat")
                        last_lon = parsed.get("lon")
                        if parsed.get("sats"):
                            last_sats = parsed.get("sats")
                        now = time.time()
                        if last_lat is not None and last_lon is not None and (now - last_weather_time) >= WEATHER_INTERVAL:
                            if not wifi_status():
                                print("WiFi desconectado, reconectando...")
                                wifi_ok = conectar_wifi()
                                print("WiFi conectado:", wifi_ok)
                            if wifi_status():
                                t, d, raw = obtener_clima(last_lat, last_lon)
                                if t is not None:
                                    temp = t
                                    desc = d
                                    last_weather_time = now
                                    print("Clima:", temp, desc)
                                else:
                                    print("Error al obtener clima, se reintentará mas tarde")
                            else:
                                print("Sin wifi, no se consulta clima")
                            gc.collect()

                mostrar_oled(last_lat, last_lon, last_sats, temp, desc, wifi_status())

            else:
                mostrar_oled(last_lat, last_lon, last_sats, temp, desc, wifi_status())
                time.sleep(0.2)

        except Exception as e:
            print("Error en loop principal:", e)
            time.sleep(1)
if _name_ == "_main_":
    main()