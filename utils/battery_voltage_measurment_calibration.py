from machine import ADC, Pin
import time

measured_voltage = 0  # should be measured

battery_adc = ADC(Pin(1))
battery_adc.atten(ADC.ATTN_11DB)
battery_adc.width(ADC.WIDTH_12BIT)

raw = battery_adc.read()
print(raw)
time.sleep(1)

v_ref = measured_voltage * 4095 / raw
print(f"v_ref={v_ref}")
