
def reverse_string(s):
   return ' ' .join(s.split()[::-1]) #with join
   return s.split()[::-1] #without join

s='Hello World'
print(reverse_string(s))