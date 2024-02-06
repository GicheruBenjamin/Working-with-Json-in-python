
# Import json module
import json

# Create a JSON file named 'house.json' and write data to it
with open('house.json', 'w') as house_file:
    house_file.write('{"rooms": 13, "windows": 16, "doors": 9, "resided": true}')

print("Original house data written to 'house.json'")

# Read the existing data from the JSON file
with open('house.json', 'r') as file:
    house_data = json.load(file)

# Update the JSON data by adding new properties
house_data['floors'] = 2
house_data['garage'] = True

# Write the updated data back to the JSON file
with open('house.json', 'w') as file:
    json.dump(house_data, file, indent=2)

print("Updated house data written back to 'house.json'")



    