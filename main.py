from machine import ADC, Pin
import time

from config import config


def read_moisture_percent():
    raw = soil.read()
    raw = max(WET_VALUE, min(raw, DRY_VALUE))
    return int((DRY_VALUE - raw) * 100 / (DRY_VALUE - WET_VALUE))


DRY_VALUE = config["soil"]["moisture"]["max_value"]
WET_VALUE = config["soil"]["moisture"]["min_value"]

soil = ADC(Pin(0))
soil.atten(ADC.ATTN_11DB)
soil.width(ADC.WIDTH_12BIT)

while True:
    print(read_moisture_percent())
    time.sleep(1)
