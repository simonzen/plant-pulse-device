from machine import ADC, Pin
import network
import urequests
import time

from config import config


def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(ssid, password)
        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            print(".", end="")
            time.sleep(1)
            timeout -= 1
    if wlan.isconnected():
        print('\nConnected')
        return True
    else:
        print('\nFailed to connect to Wi-Fi')
        return False


def send_post(url, data):
    try:
        response = urequests.post(url, json=data)
        response.close()
    except Exception as e:
        print('POST request failed:', e)


def battery_charge_level():
    raw = battery_adc.read()
    voltage = raw / 4095 * V_REF
    battery_voltage = voltage * (R1 + R2) / R2
    battery_percentage = (battery_voltage - V_MIN) / (V_MAX - V_MIN) * 100
    battery_percentage = max(0, min(100, battery_percentage))
    return battery_percentage


def read_moisture_percent():
    raw = soil.read()
    raw = max(WET_VALUE, min(raw, DRY_VALUE))
    return int((DRY_VALUE - raw) * 100 / (DRY_VALUE - WET_VALUE))


POST_URL = config["network"]["url"]

DRY_VALUE = config["soil"]["moisture"]["max_value"]
WET_VALUE = config["soil"]["moisture"]["min_value"]

soil = ADC(Pin(0))
soil.atten(ADC.ATTN_11DB)
soil.width(ADC.WIDTH_12BIT)

R1 = config["battery"]["r1"]
R2 = config["battery"]["r2"]
V_MIN = config["battery"]["v_min"]
V_MAX = config["battery"]["v_max"]
V_REF = config["battery"]["v_ref"]

battery_adc = ADC(Pin(1))
battery_adc.atten(ADC.ATTN_11DB)
battery_adc.width(ADC.WIDTH_12BIT)

if connect_wifi(config["network"]["wifi"]["ssid"], config["network"]["wifi"]["password"]):
    while True:
        data = {
            "data": {
                "soil": {
                    "moisture": read_moisture_percent(),
                },
                "battery": {
                    "percentage": battery_charge_level(),
                }
            }
        }
        send_post(POST_URL, data)
        time.sleep(1)
