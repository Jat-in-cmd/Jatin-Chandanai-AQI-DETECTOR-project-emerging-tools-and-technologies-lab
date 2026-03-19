import csv
import os

FILE_NAME = "data/air_quality_data.csv"

def save_data(data):
    """
    Save sensor data to CSV file
    """

    os.makedirs("data", exist_ok=True)

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)
