class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        return f"{self.name}, is my dog"

class Dog(Animal):
    def bark(self):
        return f"{self.name}, is barking for new guest"

object=Dog('Raja')

print(object.eat())
print(object.bark())