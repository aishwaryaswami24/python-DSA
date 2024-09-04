# def main():
#     x = int(input("enter number: "))
#     if is_even(x):
#         print('Even')
#     else:
#         print('Odd')
#
#
# def is_even(n):
#     return n%2==0
#
#
# main()

def main():
    x=int(input('what is x: '))
    if is_even(x):
        print('Even')
    else:
        print('Odd')


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
main()