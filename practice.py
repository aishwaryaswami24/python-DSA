# #json
# import json
# json_data = '{"id": 1234, "name": "Aishwarya"}'
# data=json.loads(json_data)
# print(data['id'],data['name'])
#
# #identical
# A=[1,1,2,3]
# B=[3,2,2,2,1]
# C=list((set(A)&set(B)))
# print(C)
#
# #duplicate remove
# D=[1,2,2,2,2,2,4,5,6]
# D=list(set(D))
# print(D)
#
#
# #reverse
# def reverse_str(s):
#     return s[::-1]
# s='Priya'
# print('Original string:',s)
# print('Reverse string:',reverse_str(s))
#
# #palindrome
# def palindrome(p):
#     return p==p[::-1]
# p='khokho'
# print(palindrome(p))
# if palindrome(p) is False:
#     print('Given string is not a palindrome')
# else:
#     print('Given string is palindrome')
#
# #reverse words
# def reverse_words(w):
#     return ' '.join(w.split()[::-1])
# w='Hello Aish'
# print(reverse_words(w))
#
#
# #palindrome
#
# def palindrome(p):
#     return p==p[::-1]
# p='madam'
# print('Palindrome:',palindrome(p))
#
# #reverse
# def reverse_str(r):
#     return r[::-1]
# r='SKNCOE'
# print('Reverse string:',reverse_str(r))
#
# #reverse words
# def reverse_words(w):
#     return ' '.join(w.split()[::-1])
#
# w="Hello Words"
# print('Reverse words:',reverse_words(w))
#
# #lambda
#
# add=lambda x,y:x+y
# addition=add(3,4)
# print(addition)
#
# #even odd
#
# def main():
#     x=int(input('write a number: '))
#     if is_even(x):
#         print('Even')
#     else:
#         print('Odd')
#
# def is_even(n):
#     return n%2==0
#
# main()
#
#
# #2nd way to find out even odd no
# def main():
#     Q=int(input('Enter interger: '))
#     if is_even(Q):
#      print('Even')
#     else:
#      print('Odd')
#
# def is_even(n):
#     if n%2==0:
#         return True
#     else:
#         return False
#
# main()
#
# #identical
# Q=[1,2,3]
# T=[1,1,4]
#
# identical=list((set(Q)&set(T)))
# print(identical)
#
# #true or false
# a=[1,2,3]
# b=a
# print(a is b)
#
# c=list(a)
# print(a is c)
#
# #occrance of string
#
# test_str="aishwaryaswami"
# count=0
# for i in test_str:
#     if i=='i':
#         count=count+1
# print('occrance of i:',str(count))
#
# #Check if the string contains only digits.
# def string_contains(s):
#     return s.isdigit()
#
# s='123456'
# print('string contains:',string_contains(s))
#
#
#
#
#
#
#
#
#
#
#
#
#
#reverse
def reverse_str(l):
    return l[::-1]

l='hello world'
print('reverse_string:',reverse_str(l))


#reverse words
def reverse_words(f):
    return ' '.join(f.split()[::-1])
f='hello world'
print('reverse words:',reverse_words(f))


#palindrome
def palindrome(k):
    return k==k[::-1]
k='madam'
print('palindrome:',palindrome(k))

#identical
V=[1,2,0,7]
B=[7,1,0,0]

print(list(set(V)&set(B)))

#duplicates

Dup=['Aish','Aishw','Aish']
print(list(set(Dup)))


#even_odd
def main():
    y=int(input('Enter value:'))
    if is_even(y):
        print('Even')
    else:
        print('Odd')

def is_even(o):
    if o%2==0:
        return True
    else:
        return False

main()

#True or False

a=[1,2,1]
b=a
print(a is b)

c=list(a)
print(c is a)

#is_digit
def is_digit(h):
    return h.isdigit()
h='12345aish'
print('is str contains digit:',is_digit(h))

#str occrance


strr='aishswamiaishaish'

count=0
for i in strr:
    if i=='a':
        count=count+1
print('occrance of a:',str(count))

#lambda
addition=lambda x,y:x+y
print(addition(2,5))


#json
import json
jsn='{"id": 1234, "name": "Aishwarya"}'
data=json.loads(jsn)
print('id is:',data['id'])
print('name is:',data['name'])

#print
name=input('what is your name: ')
print('Hello World',name)
print('Hello World '+name)
print(f'Hello World {name}')


#float to round
x=float(input('enter value: '))
print(x)
y=float(input('enter value: '))
print(y)
add=round(x+y)

print(add)

#print

def hello(self='world'):
    print(f'hello:{self}')
name=input('what is your name:')
print('Your name is:',name)
hello(name)
hello()


