
import json

# Create a soil JSON file
soil_data = {
    "type": "clay",
    "moisture": "medium",
    "ph": 6.5,
    "nutrients": {
        "nitrogen": 30,
        "phosphorus": 20,
        "potassium": 25
    }
}

# Writing in the soil JSON file
with open('soil.json', 'w') as file:
    json.dump(soil_data, file, indent=2)

print("Soil data written to 'soil.json'")

# Read the soil JSON file
with open('soil.json', 'r') as file:
    read_soil_data = json.load(file)

# Display the original soil data
print("\nOriginal Soil Data:")
print(read_soil_data)

# Update the soil file by deleting some properties
properties_to_delete = ['moisture', 'nutrients']
for prop in properties_to_delete:
    if prop in read_soil_data:
        del read_soil_data[prop]

# Display the modified soil data
print("\nModified Soil Data:")
print(read_soil_data)

# Write the updated soil data to the same JSON file
with open('soil.json', 'w') as file:
    json.dump(read_soil_data, file, indent=2)

print("\nUpdated soil data written back to 'soil.json'")
