# def func():
#     def nested():
#         global x
#         x=1
# x=2
# func()
# print(x)
#
# #str
# x='aish'
# y=24
# print(x+str(y))
# print(x,str(y))
#
# #add int and str:TypeError
# x='abc'
# y=5
# print(x+y)

#boolean True & False
# x='xyz'
# y=True
# print(x+y)

#pass
def func():
    pass
func()

#str bool
x='pqr'
y=True
print(x+str(y))
print(x+str(not y))

#lower
a='AISHwarya'
print(a.lower())

#
def func():
    x=1
x=2
func()
print(x)

#upper
d='SHUbham'
print(d.upper())

#global
def func():
    global x
    x=1
x=2
func()
print(x)

#capitalize
x='aISH SWAMI'
print(x.capitalize())