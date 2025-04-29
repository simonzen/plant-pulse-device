# plant-pulse-device

## Elements
- [ESP32-C3 SuperMini](https://www.sudo.is/docs/esphome/boards/esp32c3supermini/) — microcontroller with Wi-Fi
- [HW-390 capacitive soil moisture sensor](https://www.electrodragon.com/product/capacitive-soil-moisture-sensor-v1-2/) — soil moisture detection module

## Prerequisites
- Install ESP32-C3 USB driver if needed: [macOS CH340 driver](https://github.com/adrianmihalko/ch340g-ch34g-ch34x-mac-os-x-driver)
- Flash MicroPython firmware on ESP32-C3: [official MicroPython installation guide](https://micropython.org/download/ESP32_GENERIC_C3/)

## Config
This repository contains a **configuration template** (`config.py`), which must be uploaded to the ESP32 device and filled with your calibration values.

Example `config.py`:

```python
config = {
    "soil": {
        "moisture": {
            "max_value": 0,  # ADC value for dry soil
            "min_value": 0,  # ADC value for fully wet soil
        }
    }
}
```

You must replace the `0` values after calibration.

## Wiring
The `scheme.fzz` file included in the repository shows the correct wiring for all components.  
You can open it using Fritzing software.

## Sensor Calibration

### Description
The HW-390 capacitive soil moisture sensor is used to measure the moisture level of soil. It provides analog output proportional to the soil moisture.

### Calibration Process
1. Connect the sensor to ESP32-C3 according to the scheme.
2. Run the script `path/to/script.py`.
3. Measure the ADC value:
    - In dry air (sensor exposed to air)
    - Submerged in a glass of water (sensor fully wet)
4. Update `config.py`:
    - `max_value` should correspond to the dry measurement.
    - `min_value` should correspond to the wet measurement.

### Troubleshooting
If the sensor provides unstable or unrealistic readings:
- Make sure VCC is connected to **3.3V**, not 5V.
- Double-check your wiring and ensure proper ground connection.
- Inspect the sensor for visible physical damage.
- You can also refer to this video tutorial: [YouTube: Soil Moisture Sensor Calibration](https://www.youtube.com/watch?v=IGP38bz-K48).

If the sensor still does not perform properly, it might be defective, and replacement should be considered.
