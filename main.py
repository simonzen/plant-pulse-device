from machine import ADC, Pin
import time

from config import config


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

while True:
    test_data = {
        "data": {
            "soil": {
                "moisture": read_moisture_percent(),
            },
            "battery": {
                "percentage": battery_charge_level(),
            }
        }
    }
    data = read_moisture_percent()
    time.sleep(1)
