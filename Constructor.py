class Car:

    def __init__(self,model,colour):
        self.model=model
        self.colour=colour

    def check_colour(self):
        return "colour checking done"


my_car=Car('Bullet','Black')

print(my_car.check_colour())
print(my_car.model)
