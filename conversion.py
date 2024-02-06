
# Importing the json Module
import json

# Creating a car dictionary
car = {
    "Brand": "Toyota",
    "Model": "Hillux",
    "Year of production": 2011,
    "Engine": {
        "Type": "V8",
        "Fuel": "Diesel",
        "Version": 7.89
    },
    "Wheels": ["Wide", "All terrain", 18],
    "Torque": 890,
    "horsepower": "925hp"
}

# Converting the car dictionary to JSON string
car_json_string = json.dumps(car, indent=2)

# Creating a JSON file
with open('car.json', 'w') as car_json_file:
    # Writing the car dictionary to the file
    car_json_file.write(car_json_string)

print("Car data written to 'car.json'")

