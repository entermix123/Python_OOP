# # ENCAPSULATION
# # _balance and _account_number are encapsulated in the class, they cannot be accessed outside the class
# # they can be accessed only by methods of the class, like getter, setter and withdraw methods
# class BankAccount:
#     def __init__(self, _account_number, balance):
#         self._balance = balance
#         self._account_number = _account_number
#
#     def get_balance(self):
#         return self._balance
#
#     def deposit(self, amount):
#         self._balance += amount
#         return self._balance
#
#     def withdraw(self, amount):
#         if amount > self._balance:
#             print("Insufficient funds")
#         else:
#             self._balance -= amount
#             return self._balance
#
#
# account1 = BankAccount("1234567890", 1000)
# print(account1.get_balance())
# account1.deposit(500)
# print(account1.get_balance())
# account1.withdraw(2100)

# ABSTRACTION
# base classes that can have fewer methods 3-5 that can be inhereted by mass used classes.
# Good practice is that they should not be called dirrectly, but only by other classes.
#
# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):          # Abstract class. Give us possibility not to specify next class parameters every time.
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")
#
#
# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")
#
#
# class Bird(Animal):
#     def make_sound(self):
#         print("quaa!")
#
#
# dog = Dog()
# cat = Cat()
# bird = Bird()
#
# dog.make_sound()
# cat.make_sound()
# bird.make_sound()


# # POLIMORPHISM
# # allow objects of different classes to be treated like they are from same class over shared interface or behavior
# # can be achieved by removing of overloading.
#
#
# class Animal:   # Polymorph class. Give us possibility set behaviors to other classes for same interface and environment
#     def speak(self):
#         print("Animal speak")
#
#
# class Dog(Animal):
#     def speak(self):
#         print("Dog speak")
#
#
# class Cat(Animal):
#     def speak(self):
#         print("Cat speak")
#
#
# animal = Animal()
# dog = Dog()
# cat = Cat()
#
# animal.speak()
# dog.speak()
# cat.speak()

# # INHERITANCE
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.hobbies = []
#
#     def add_hobby(self, hobby):
#         self.hobbies.append(hobby)
#
#     def __str__(self):
#         return F'{self.name} has {self.hobbies}'
#
#
# class FootballPlayer(Person):
#     def __init__(self, name):
#         super().__init__(name)          # inheritance from Person class
#         self.add_hobby('Football')
#         self.add_hobby('Fitness')
#
#
# mike = FootballPlayer('Mike')
# print(mike)

# class Person:
#     def __init__(self, name, age):      # base class
#         self.name = name                # base class parameter1
#         self.age = age                  # base class parameter2
#
#     def get_details(self):
#         return f'Name: {self.name}, Age: {self.age}'        # base class method
#
#
# class Student(Person):                                      # inherited from Person class
#     def __init__(self, name, age, rollno):                  # second class initialization
#         super().__init__(name, age)                         # second class inheritance from base class
#         self.rollno = rollno                                # second class specific parameter
#
#     def get_details(self):
#         return f'Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}'
#
#
# person = Person('John', 30)
# student = Student('Mike', 30, 123)
#
# print(person.get_details())
# print(student.get_details())
