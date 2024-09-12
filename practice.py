import json
json_data = '{"id": 1234, "name": "Aishwarya"}'
data=json.loads(json_data)
print(data['id'],data['name'])