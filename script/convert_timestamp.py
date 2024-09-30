import csv
from datetime import datetime

# Define the path to your CSV file
csv_file = 'output/VMT_USDT-202408.csv'

# Open the CSV file and read its content
with open(csv_file, 'r') as file:
    reader = csv.reader(file)

    # Iterate through each row in the CSV
    for row in reader:
        # The first column (index 0) is the timestamp in each row
        timestamp = float(row[0])

        # Convert the timestamp to a datetime object
        dt_object = datetime.fromtimestamp(timestamp)

        # Print the original row along with the converted timestamp
        # print(f"Original Row: {row}")
        # print(f"Converted Timestamp: {dt_object}")
        print(f"{dt_object}")
        print()
