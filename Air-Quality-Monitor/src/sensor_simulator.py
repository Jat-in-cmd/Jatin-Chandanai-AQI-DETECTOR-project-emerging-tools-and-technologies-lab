import random

def generate_sensor_data():
    """
    Simulates air quality sensor data.
    Returns a dictionary containing pollutant values.
    """

    data = {
        "PM2.5": round(random.uniform(5, 150), 2),
        "PM10": round(random.uniform(10, 200), 2),
        "CO2": round(random.uniform(300, 800), 2),
        "Temperature": round(random.uniform(20, 40), 2),
        "Humidity": round(random.uniform(30, 80), 2)
    }

    return data
