from machine import ADC, Pin
import time

adc = ADC(Pin(0))
adc.atten(ADC.ATTN_11DB)

NUM_SAMPLES = 50
DELAY = 1


def calibrate_sensor():
    readings = []

    print(f"Starting calibration... Collecting {NUM_SAMPLES} samples:")

    for i in range(NUM_SAMPLES):
        value = adc.read()
        readings.append(value)
        print(f"[{i + 1}] {value}")
        time.sleep(DELAY)

    minimum = min(readings)
    maximum = max(readings)
    average = sum(readings) // len(readings)
    spread = maximum - minimum

    print("Results:")
    print(f"min: {minimum}")
    print(f"max: {maximum}")
    print(f"average: {average}")
    print(f"spread: {spread}")


calibrate_sensor()
