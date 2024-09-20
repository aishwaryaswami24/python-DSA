def func():
    def nested():
        global x
        x=1
x=2
func()
print(x)

#str
x='aish'
y=24
print(x+str(y))
print(x,str(y))

#add int and str:TypeError
x='abc'
y=5
print(x+y)

