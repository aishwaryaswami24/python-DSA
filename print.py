# x=int(input('Enter value1: '))
# y=int(input('Enter value2: '))
#
# if x>y:
#     print('x is greter than y')
# elif x<y:
#     print('x is less than y')
# else:
#     print('x is equal to y')
#

#2nd way:
# x=int(input('Enter value1: '))
# y=int(input('Enter value2: '))
#
# if x>y or x<y:
#     print('x is not equal to y')
# else:
#     print('x is equal to y')


# #strip
# name=input('enter your name:')
# #name=name.strip()
# #name=name.lstrip()
# name=name.rstrip()
# print(name)


#capitalize
# name=input('enter your name:')
# name=name.capitalize()
# print(name)

#range
# for i in range(4):
#     print(i)
# else:
#     print('end')

#replace
# str='11AISH1'
# print(str.replace('1','One'))
# print(str.replace('1','One',0))
# print(str.replace('1','One',1))
#here we have provided count 0 then it will not replace 1 by One
#if you give count=1 then it will replace only one occrance

#find
# text='har war bar'
# print(text.find('bar')) #it returns starting index number
# i=text.find('bar',9) #Start searching from index 9
# print(i)
#it returns starting index number
#find() string method return the index of the first occurrence of a substring

#_doc_
# def text():
#     '''doc'''
#     '''hello'''
# print(text.__doc__)


# print('Hello',end='111')
# print('Hello')
#1st print did not end on new line it remains on same line so 2nd print continued with the same line

#syntax error/#recursion error
# def func():

#     func()
#
# #slicing
# t='AaBbCcDd'
# print(t[::2])
# print(t[1::2])
# # t[::2] picks every second character starting from index 0, giving "ABC".
# # t[1::2] picks every second character starting from index 1, giving "aBd".
#
# #t[start:stop:step]
# t='12345'
# print(t[1::-1])
#
#
# #// is a floor division operator, division rounded down
# a=5//3
# print(a)

#print
a=[1]
b=[0,a]
print(b)
c=[0,b]
print(c)
print(a in b)