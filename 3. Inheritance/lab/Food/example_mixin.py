class PrintableMixin:
    def print_info(self):
        print(f'Object of class {type(self).__name__}')     # return type of object --> Object of class Person
        for attr, value in self.__dict__.items():
            print(f'{attr}: {value}')


class Person(PrintableMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name}and I\'m {self.age} years old')


p1 = Person('John', 20)
p1.say_hello()
p1.print_info()
