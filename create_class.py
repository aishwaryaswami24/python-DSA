
#Car is a class
class Car:
    def __init__(self,model,color): #constructor
        self.model=model
        self.color=color


#mycar is a object
mycar= Car('BMW','blue')
print(mycar.color,mycar.model)




#without constructor python calls default one which doesn't inistializes object attributes
class Car:
    pass

mycar=Car()

#need to pass manually attributes values
mycar.color='blue'
print(mycar.color)