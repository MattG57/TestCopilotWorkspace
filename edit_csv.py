import csv

# Read data from 'data.csv' file and store it in a list
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Delete the first and last columns from the data
for row in data:
    del row[0]
    del row[-1]

# Write the modified data to 'output.csv' file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
