#json
import json
json_data = '{"id": 1234, "name": "Aishwarya"}'
data=json.loads(json_data)
print(data['id'],data['name'])

#identical
A=[1,1,2,3]
B=[3,2,2,2,1]
C=list((set(A)&set(B)))
print(C)


