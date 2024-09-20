def func():
    def nested():
        global x
        x=1
x=2
func()
print(x)