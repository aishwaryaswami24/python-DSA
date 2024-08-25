class Dog:
    def make_sound(self):
        return 'chirp'

class Cat:
    def make_sound(self):
        return 'wayk'

class Duck:
    def make_sound(self):
        return 'daw'

#common method of above three classes
def animal_sound(animal):
    print(animal.make_sound())


dog=Dog()
cat=Cat()
duck=Duck()

animal_sound(dog)
animal_sound(cat)
animal_sound(duck)