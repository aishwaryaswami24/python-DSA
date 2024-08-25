# Abstract class
class Vehicle:
    def start(self):
        raise NotImplementedError("This is an abstract method and should be overridden in a subclass")

class Car(Vehicle):
    def start(self):
        return 'car class'

class Bike(Vehicle):
    def start(self):
        return 'bike class'

# Create instances of Car and Bike
car = Car()
bike = Bike()

# Attempting to create an instance of Vehicle (abstract class) should not be allowed
try:
    vehicle = Vehicle()
    print(vehicle.start())
except NotImplementedError as e:
    print(e)

# Correct usage with Car and Bike
print(car.start())   # Output: car class
print(bike.start())  # Output: bike class

#should show error while calling abtract class method return below error bez it should be overridden in a subclass only
#NotImplementedError: This is an abstract method and should be overridden in a subclass
#
# vehicle=Vehicle()
# print(vehicle.start())