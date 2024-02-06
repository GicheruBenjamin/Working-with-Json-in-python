
# Import json module
import json

# Open the car.json file in read and write mode
with open('car.json', 'r+') as car_json:
    # Read the JSON data from the file
    car_json_data = car_json.read()

# Convert the JSON data to a dictionary
car = json.loads(car_json_data)

# Display the resulting dictionary
print(car)
