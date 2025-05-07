config = {
    "network": {
        "wifi": {
            "ssid": "",
            "password": "",
        },
        "url": "",
        "sleep_time": 60*60,
    },
    "soil": {
        "moisture": {
            "max_value": 0,  # ADC value for dry soil
            "min_value": 0,  # ADC value for dry soil
        }
    },
    "battery": {
        "r1": 100000,  # Top resistor in voltage divider (ohms)
        "r2": 100000,  # Bottom resistor in voltage divider (ohms)
        "v_min": 3.0,  # Voltage corresponding to 0% battery
        "v_max": 4.2,  # Voltage corresponding to 100% battery
        "v_ref": 0,    # Calibrated ADC reference voltage (based on measurement)
    },
}
