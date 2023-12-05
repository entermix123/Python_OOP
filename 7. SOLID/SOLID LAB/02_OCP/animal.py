class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print('woof-woof')


class Cat(Animal):

    def make_sound(self):
        print('meow')


class Chicken(Animal):

    def make_sound(self):
        print('cluck')


animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
# animals = [Animal('cat'), Animal('dog')]
[x.make_sound() for x in animals]
# for x in range(len(animals)):
#     animals[x].make_sound()

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
