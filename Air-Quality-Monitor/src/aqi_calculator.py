def calculate_aqi(data):
    """
    Very basic AQI calculation (simplified logic)
    """

    pm25 = data["PM2.5"]
    pm10 = data["PM10"]

    aqi = (pm25 * 0.6) + (pm10 * 0.4)

    return round(aqi, 2)
