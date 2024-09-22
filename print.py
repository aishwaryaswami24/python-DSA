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
str='11AISH1'
print(str.replace('1','One'))
print(str.replace('1','One',0))
print(str.replace('1','One',1))
#here we have provided count 0 then it will not replace 1 by One
#if you give count=1 then it will replace only one occrance