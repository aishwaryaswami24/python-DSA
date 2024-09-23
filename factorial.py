# from datetime import datetime
# now=datetime.now()
# print(now)
#
# #time
# import time
# tme=time.strftime('%H:%M:%S',time.localtime())
# print(tme)
#
# #Python’s math library provides a built-in function factorial() that can compute the factorial of a number.
# import math
# num=int(input('Enter the number:'))
# print(f'Factorial of {num} is:{math.factorial(num)}')
#
# #it will raise a ValueError if you input a negative number.


#factorial 2nd way
def factorial_num(n):
    if n == 0 or 1:
        return 1
    else:
        n * n - 1

num = int(input('Enter value:'))
print(f'Factorial of {num}:',{factorial_num(num)})
