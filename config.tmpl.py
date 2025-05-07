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
        "v_ref": 0,             # Calibrated ADC reference voltage
    },
}