
# Creating a JSON file named 'person.json'
with open('person.json', 'w') as person_file:
    # Writing data to the JSON file
    person_file.write('{"Name": "Irene Joy", "Age": 20, "is_cute": true}')

print("Person data written to 'person.json'")

