"""
Air Quality Monitor
Basic project initialization file
"""

from sensor_simulator import generate_sensor_data


def main():
    print("Air Quality Monitoring System Initialized")

    data = generate_sensor_data()

    print("Simulated Sensor Data:")
    for key, value in data.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
