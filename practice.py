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

#duplicate remove
D=[1,2,2,2,2,2,4,5,6]
D=list(set(D))
print(D)


#reverse
def reverse_str(s):
    return s[::-1]
s='Priya'
print('Original string:',s)
print('Reverse string:',reverse_str(s))
