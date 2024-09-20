def func():
    def nested():
        global x
        x=1
x=2
func()
print(x)

#
x='aish'
y=24
print(x+str(y))
print(x,str(y))