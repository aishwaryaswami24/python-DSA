# # #json
# # import json
# # json_data = '{"id": 1234, "name": "Aishwarya"}'
# # data=json.loads(json_data)
# # print(data['id'],data['name'])
# #
# # #identical
# # A=[1,1,2,3]
# # B=[3,2,2,2,1]
# # C=list((set(A)&set(B)))
# # print(C)
# #
# # #duplicate remove
# # D=[1,2,2,2,2,2,4,5,6]
# # D=list(set(D))
# # print(D)
# #
# #
# # #reverse
# # def reverse_str(s):
# #     return s[::-1]
# # s='Priya'
# # print('Original string:',s)
# # print('Reverse string:',reverse_str(s))
# #
# # #palindrome
# # def palindrome(p):
# #     return p==p[::-1]
# # p='khokho'
# # print(palindrome(p))
# # if palindrome(p) is False:
# #     print('Given string is not a palindrome')
# # else:
# #     print('Given string is palindrome')
# #
# # #reverse words
# # def reverse_words(w):
# #     return ' '.join(w.split()[::-1])
# # w='Hello Aish'
# # print(reverse_words(w))
# #
# #
# # #palindrome
# #
# # def palindrome(p):
# #     return p==p[::-1]
# # p='madam'
# # print('Palindrome:',palindrome(p))
# #
# # #reverse
# # def reverse_str(r):
# #     return r[::-1]
# # r='SKNCOE'
# # print('Reverse string:',reverse_str(r))
# #
# # #reverse words
# # def reverse_words(w):
# #     return ' '.join(w.split()[::-1])
# #
# # w="Hello Words"
# # print('Reverse words:',reverse_words(w))
# #
# # #lambda
# #
# # add=lambda x,y:x+y
# # addition=add(3,4)
# # print(addition)
# #
# # #even odd
# #
# # def main():
# #     x=int(input('write a number: '))
# #     if is_even(x):
# #         print('Even')
# #     else:
# #         print('Odd')
# #
# # def is_even(n):
# #     return n%2==0
# #
# # main()
# #
# #
# # #2nd way to find out even odd no
# # def main():
# #     Q=int(input('Enter interger: '))
# #     if is_even(Q):
# #      print('Even')
# #     else:
# #      print('Odd')
# #
# # def is_even(n):
# #     if n%2==0:
# #         return True
# #     else:
# #         return False
# #
# # main()
# #
# # #identical
# # Q=[1,2,3]
# # T=[1,1,4]
# #
# # identical=list((set(Q)&set(T)))
# # print(identical)
# #
# # #true or false
# # a=[1,2,3]
# # b=a
# # print(a is b)
# #
# # c=list(a)
# # print(a is c)
# #
# # #occrance of string
# #
# # test_str="aishwaryaswami"
# # count=0
# # for i in test_str:
# #     if i=='i':
# #         count=count+1
# # print('occrance of i:',str(count))
# #
# # #Check if the string contains only digits.
# # def string_contains(s):
# #     return s.isdigit()
# #
# # s='123456'
# # print('string contains:',string_contains(s))
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #reverse
# def reverse_str(l):
#     return l[::-1]
#
# l='hello world'
# print('reverse_string:',reverse_str(l))
#
#
# #reverse words
# def reverse_words(f):
#     return ' '.join(f.split()[::-1])
# f='hello world'
# print('reverse words:',reverse_words(f))
#
#
# #palindrome
# def palindrome(k):
#     return k==k[::-1]
# k='madam'
# print('palindrome:',palindrome(k))
#
# #identical
# V=[1,2,0,7]
# B=[7,1,0,0]
#
# print(list(set(V)&set(B)))
#
# #duplicates
#
# Dup=['Aish','Aishw','Aish']
# print(list(set(Dup)))
#
#
# #even_odd
# def main():
#     y=int(input('Enter value:'))
#     if is_even(y):
#         print('Even')
#     else:
#         print('Odd')
#
# def is_even(o):
#     if o%2==0:
#         return True
#     else:
#         return False
#
# main()
#
# #True or False
#
# a=[1,2,1]
# b=a
# print(a is b)
#
# c=list(a)
# print(c is a)
#
# #is_digit
# def is_digit(h):
#     return h.isdigit()
# h='12345aish'
# print('is str contains digit:',is_digit(h))
#
# #str occrance
#
#
# strr='aishswamiaishaish'
#
# count=0
# for i in strr:
#     if i=='a':
#         count=count+1
# print('occrance of a:',str(count))
#
# #lambda
# addition=lambda x,y:x+y
# print(addition(2,5))
#
#
# #json
# import json
# jsn='{"id": 1234, "name": "Aishwarya"}'
# data=json.loads(jsn)
# print('id is:',data['id'])
# print('name is:',data['name'])
#
# #print
# name=input('what is your name: ')
# print('Hello World',name)
# print('Hello World '+name)
# print(f'Hello World {name}')
#
#
# #float to round
# x=float(input('enter value: '))
# print(x)
# y=float(input('enter value: '))
# print(y)
# add=round(x+y)
#
# print(add)
#
# #print
#
# def hello(self='world'):
#     print(f'hello:{self}')
# name=input('what is your name:')
# print('Your name is:',name)
# hello(name)
# hello()
#
#

# #half diamond
# n=5
# i=1
# while i<=n:
#     print('*'*i)
#     i += 1
#
# i=n-1
# while i>0:
#     print('*'*i)
#     i -=1
#
# #convert 1st 3 letters to upper
#
# s='Priya Swami'
# convert= s[:3].upper()+s[3:].lower()
# print(convert)
#
# convert1=s[:4].lower()+s[4:].upper()
# print(convert1)


#occrance of each word in sentence
# from collections import Counter
# def occrance_word(sentence):
#    words= sentence.split()
#    print(words)
#    return Counter(words)
#
#
# sentence="hello world hello"
# print(occrance_word(sentence))
#
#
# #capitalize
# def capital_word(s):
#     return s.capitalize()
# s='word'
# print(capital_word(s))
#
#
# #longest
# def longest_word(s):
#     word=s.split()
#     print(word)
#     return max(word,key=len)
# s="konichiwa world "
# print(longest_word(s))
#

# #range
# for i in range(0,1):
#     print(i)
# else:
#     print('end')

#
# for i in range(1,4,1):
#     print(i)
#

# def reverse_str(s):
#     return s[::-1]
# s='Aish swami'
# print(reverse_str(s))
# print(s.title())
# print(s.capitalize())
# print(' '.join(s.split()[::-1]))
# print(s==s[::-1])
#
# lst=[1,32,45,9,4]
# even_count=0
# odd_count=0
# for i in lst:
#     if i%2==0:
#         even_count +=1
#     else:
#         odd_count +=1
# print(even_count)
# print(odd_count)
#
# ls=[1,2,3,4]
# even_lst=[]
# for i in ls:
#     if i%2==0:
#         even_lst.append(i)
# print(even_lst)

#even odd no
# def main():
#     num=int(input('enter num:'))
#     if is_even(num):
#         print('Even')
#     else:
#         print('Odd')
#
# def is_even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
#
# main()

# name='Aishwarya'
# print(name.lower())
# print(name.islower())

# #lambda
# add=lambda x,y:x+y
# add=add(2,3)
# print(add)
#
# #vowels
# def vowels_count(s):
#     vowels='aeiouAEIOU'
#     return sum(1 for char in s if char in vowels)
# s='Hello World'
# print(vowels_count(s))
#
# #annagrams
# def annagram_find(s1,s2):
#     return sorted(s1)==sorted(s2)
# s1='aish'
# s2='shia'
# print(annagram_find(s1,s2))
#
# #remove duplicates from string
# def remove_dupstr(s):
#     return ''.join(sorted(set(s)))
# s='abcdcdda'
# print(remove_dupstr(s))


lst1=[1,0,9,8,3]
lst2=[2,3,4,1,0]
dup=[]
for i in lst1:
    if i in lst2:
        dup.append(i)


