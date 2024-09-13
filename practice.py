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

#palindrome
def palindrome(p):
    return p==p[::-1]
p='khokho'
print(palindrome(p))
if palindrome(p) is False:
    print('Given string is not a palindrome')
else:
    print('Given string is palindrome')

#reverse words
def reverse_words(w):
    return ' '.join(w.split()[::-1])
w='Hello Aish'
print(reverse_words(w))


#palindrome

def palindrome(p):
    return p==p[::-1]
p='madam'
print('Palindrome:',palindrome(p))

#reverse
def reverse_str(r):
    return r[::-1]
r='SKNCOE'
print('Reverse string:',reverse_str(r))

#reverse words
def reverse_words(w):
    return ' '.join(w.split()[::-1])

w="Hello Words"
print('Reverse words:',reverse_words(w))