import csv

# Dictionary data to be written to the CSV file
data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "San Francisco"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]

# Specify the filename
filename = "example.csv"

# Get the headers from the keys of the first dictionary
headers = data[0].keys()

# Create and write to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    # Write the header row
    writer.writeheader()
    # Write the data rows
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully.")