#print id value from json
# {'id': 1234,
#  'name': 'Aishwarya'}

import json

# JSON data (correctly formatted as a string)
json_data = '{"id": 1234, "name": "Aishwarya"}'

# Parse JSON data
data = json.loads(json_data)

# Access and print the 'id' and 'name' values
print("ID value:", data['id'])
print("Name:", data['name'])