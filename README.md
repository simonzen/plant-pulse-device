# plant-pulse-device

## Elements
- [ESP32-C3 SuperMini](https://www.sudo.is/docs/esphome/boards/esp32c3supermini/) — microcontroller with Wi-Fi
- [HW-390 capacitive soil moisture sensor](https://www.electrodragon.com/product/capacitive-soil-moisture-sensor-v1-2/) — soil moisture detection module
- [18650 Battery 3.7V 2200mah](https://www.jameco.com/Jameco/Products/ProdDS/2144243.pdf)
- [18650 battery holder](https://www.mouser.com/datasheet/2/1398/Soldered_101619_holder_for_18650_lithium_battery-3532573.pdf) — holder for the battery
- [TYPE C 5V 1A 18650 TP4056 with protection](https://support.envistiamall.com/kb/tp4056-dw01a-microusb-5v-1a-18650-lithium-battery-dual-function-charger-board-with-protection-module/) — Lithium Battery Dual Function Charger Board with Protection Module

## Prerequisites
- Install ESP32-C3 USB driver if needed: [macOS CH340 driver](https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver)
- Flash MicroPython firmware on ESP32-C3: [official MicroPython installation guide](https://micropython.org/download/ESP32_GENERIC_C3/)

---

## Configuration

This repository contains a configuration template: [`config.tmpl.py`](./config.tmpl.py).  
You must create a file `config.py` based on this template and upload it to the device.

### Configuration Fields

```python
config = {
    "network": {
        "wifi": {
            "ssid": "",         # Your Wi-Fi SSID
            "password": "",     # Your Wi-Fi password
        },
        "url": "",              # Server endpoint for POST requests
        "sleep_time": 60*60,    # Delay between measurements (in seconds)
    },
    "soil": {
        "moisture": {
            "max_value": 0,     # ADC value for completely dry soil
            "min_value": 0,     # ADC value when sensor fully wet (e.g. water cup)
        }
    },
    "battery": {
        "r1": 100000,           # Top resistor in voltage divider (Ohms)
        "r2": 100000,           # Bottom resistor in voltage divider (Ohms)
        "v_min": 3.0,           # Battery voltage representing 0% charge
        "v_max": 4.2,           # Battery voltage representing 100% charge
        "v_ref": 0,             # Calibrated ADC reference voltage (see below)
    },
}
```

---

## Sensor Calibration

### Moisture Sensor

The HW-390 capacitive soil moisture sensor provides analog output proportional to soil moisture.

#### Steps
1. Connect the sensor to ESP32-C3 according to `scheme.fzz`
2. Run `utils/soil_moisture_detector_calibration.py`
3. Measure and record ADC values:
   - `dry`: sensor in air
   - `wet`: sensor submerged in water
4. Update `config["soil"]["moisture"]` with `max_value = dry`, `min_value = wet`

### Battery Voltage Calibration

ESP32 reads battery voltage using a voltage divider. Because ADC reference (v_ref) is imprecise, manual calibration improves accuracy.

#### Steps
1. Connect voltage divider to ADC (Pin 1)
2. Use multimeter to measure actual voltage at ADC pin
3. Run `utils/battery_voltage_measurement_calibration.py` with `measured_voltage`
4. Update `config["battery"]["v_ref"]` with calculated result

---

## Wiring

The file [`scheme.fzz`](./scheme.fzz) provides the full wiring diagram.  
Open it in [Fritzing](https://fritzing.org/download/) to explore the connections between:

- ESP32-C3
- Moisture sensor
- Battery
- Voltage divider
- TP4056 charging module

---

## Features

- Calibrated soil moisture readings
- Battery charge level (in %)
- Reliable Wi-Fi reconnect support
- Data transmission to server endpoint via HTTP POST