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

## Config
This repository contains a **configuration template** (`config.py`), which must be uploaded to the ESP32 device and filled with your calibration values.

Example: [config.py](./config.tmpl.py)

You must replace the values with actual measurements based on calibration.

## Wiring
The `scheme.fzz` file included in the repository shows the correct wiring for all components.  
You can open it using Fritzing software.

## Sensor Calibration

### Moisture Sensor
The HW-390 capacitive soil moisture sensor is used to measure the moisture level of soil. It provides analog output proportional to the soil moisture.

#### Calibration Process
1. Connect the sensor to ESP32-C3 according to the scheme.
2. Run the script `utils/soild_moisture_detector_calibration.py`.
3. Measure the ADC value:
    - In dry air (sensor exposed to air)
    - Submerged in a glass of water (sensor fully wet)
4. Update `config.py`:
    - `max_value` should correspond to the dry measurement.
    - `min_value` should correspond to the wet measurement.

#### Troubleshooting
If the sensor provides unstable or unrealistic readings:
- Make sure VCC is connected to **3.3V**, not 5V.
- Double-check your wiring and ensure proper ground connection.
- Inspect the sensor for visible physical damage.
- You can also refer to this video tutorial: [YouTube: Soil Moisture Sensor Calibration](https://www.youtube.com/watch?v=IGP38bz-K48).

If the sensor still does not perform properly, it might be defective, and replacement should be considered.

### Battery Voltage Measurement

The ESP32-C3 reads battery voltage through a resistive voltage divider. Because internal ADC reference voltage (V_ref) is not exact, calibration is required for accurate readings.

#### Calibration Process
1. Ensure the battery is connected through the voltage divider (using `R1` and `R2`).
2. Measure the actual voltage at the **ADC pin 1** using a multimeter.  
   For example: `1.97 V`
3. Run the script `utils/battery_voltage_measurment_calibration.py` with `measured_voltage` provided.
4. Update `config.py`:
   - `v_ref`: calculated value (e.g. 2.92)
   - `r1`, `r2`: resistor values from your voltage divider (default `100000`)
   - `v_min`: voltage that should be considered 0% battery (default `3.0`)
   - `v_max`: voltage that represents 100% battery (default `4.2`)

#### Notes
- This calibration only needs to be done once per device or hardware revision.
- Using precise resistors and reliable multimeter improves accuracy.
- ESP32-C3 ADC accuracy is limited; expect some fluctuation.
