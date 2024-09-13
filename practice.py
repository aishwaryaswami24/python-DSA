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

#lambda

add=lambda x,y:x+y
addition=add(3,4)
print(addition)

#even odd

def main():
    x=int(input('write a number: '))
    if is_even(x):
        print('Even')
    else:
        print('Odd')

def is_even(n):
    return n%2==0

main()


#2nd way to find out even odd no
def main():
    Q=int(input('Enter interger: '))
    if is_even(Q):
     print('Even')
    else:
     print('Odd')

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

main()

#identical
Q=[1,2,3]
T=[1,1,4]

identical=list((set(Q)&set(T)))
print(identical)

#true or false
a=[1,2,3]
b=a
print(a is b)