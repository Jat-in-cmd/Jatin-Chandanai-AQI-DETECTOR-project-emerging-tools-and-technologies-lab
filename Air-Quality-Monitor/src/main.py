"""
Air Quality Monitor
Basic project initialization file
"""

from sensor_simulator import generate_sensor_data
from data_handler import save_data
from aqi_calculator import calculate_aqi


def main():
    print("Air Quality Monitoring System Running...\n")

    data = generate_sensor_data()

    aqi = calculate_aqi(data)
    data["AQI"] = aqi

    print("Sensor Data:")
    for key, value in data.items():
        print(f"{key}: {value}")

    save_data(data)
    print("\nData saved successfully!")


if __name__ == "__main__":
    main()
