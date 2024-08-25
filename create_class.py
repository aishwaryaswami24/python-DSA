class Car:
    def __init__(self,model,color): #constructor
        self.model=model
        self.color=color



mycar= Car('BMW','blue')
print(mycar.color,mycar.model)
