# Plant Pulse Device

A small MicroPython project for the ESP32‑C3 that monitors soil moisture and battery level and periodically sends the data to a server over Wi‑Fi.  The repository contains calibration scripts and a wiring diagram to simplify building the device from scratch.

## Hardware
- [ESP32‑C3 SuperMini](https://www.sudo.is/docs/esphome/boards/esp32c3supermini/) — microcontroller with Wi‑Fi
- [HW‑390 capacitive soil moisture sensor](https://www.electrodragon.com/product/capacitive-soil-moisture-sensor-v1-2/) — soil moisture detection module
- [18650 3.7 V lithium‑ion battery](https://de.aliexpress.com/item/1005007076392293.html) — soldered directly, no holder
- [TP4056 charger with protection](https://support.envistiamall.com/kb/tp4056-dw01a-microusb-5v-1a-18650-lithium-battery-dual-function-charger-board-with-protection-module/)

## Getting Started
1. Install the ESP32‑C3 USB driver if needed (for example the [macOS CH340 driver](https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver)).
2. Flash a MicroPython firmware build to the device using the [official installation guide](https://micropython.org/download/ESP32_GENERIC_C3/).
3. Copy `config.tmpl.py` to `config.py` and fill in the values (see the next section for details).
4. Upload `main.py` and `config.py` to the ESP32‑C3. Any tool that can copy files to a MicroPython board works (`mpremote`, `ampy`, etc.).

## Configuration
`config.py` must define a dictionary named `config`. Each value tunes a different aspect of the device:

```python
config = {
    "network": {
        "wifi": {
            "ssid": "",         # your Wi‑Fi SSID
            "password": "",     # your Wi‑Fi password
        },
        "url": "",              # server endpoint for POST requests
        "sleep_time": 60 * 60,   # delay between measurements (seconds)
    },
    "soil": {
        "moisture": {
            "max_value": 0,     # ADC value for completely dry soil
            "min_value": 0,     # ADC value when sensor is fully wet
        }
    },
    "battery": {
        "r1": 100000,           # top resistor in voltage divider (ohms)
        "r2": 100000,           # bottom resistor in voltage divider (ohms)
        "v_min": 3.0,           # battery voltage representing 0% charge
        "v_max": 4.2,           # battery voltage representing 100% charge
        "v_ref": 0,             # calibrated ADC reference voltage
    },
}
```

## Calibration
Calibration improves measurement accuracy. The `utils` directory contains small helper scripts to run directly on the device.

### Moisture Sensor
1. Wire the sensor according to `scheme.fzz`.
2. Run `utils/soil_moisture_detector_calibration.py` and note the printed values.
3. Set `max_value` to the reading with the sensor in dry air and `min_value` to the value when the sensor is submerged in water.

### Battery Voltage
1. Connect the voltage divider to ADC pin 1.
2. Measure the voltage at that pin with a multimeter.
3. Run `utils/battery_voltage_measurement_calibration.py` after setting `measured_voltage` in the script to the value from your multimeter. The script prints `v_ref` which should be copied into the configuration.

## Wiring
The file [`scheme.fzz`](./scheme.fzz) contains the complete wiring diagram. Open it in [Fritzing](https://fritzing.org/download/) for an interactive view. Connections include

- ESP32‑C3
- soil moisture sensor
- battery and voltage divider
- TP4056 charging module

## Features
- Calibrated soil moisture readings
- Battery charge level as a percentage
- Automatic Wi‑Fi reconnection
- Data transmission via HTTP POST to your server
