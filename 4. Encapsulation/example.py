# class CreditCard:
#     def __init__(self, number, name: str, cvv: str, expiration_date: str, pin: str, pin1: str):
#         self.number = number
#         self.name = name
#         self.expiration_date = expiration_date
#         self.cvv = cvv
#         self._pin = pin         # protected attribute
#         self.__pin1 = pin1      # private attribute
#
#     def get_protected_pin(self):
#         return self._pin        # protected attribute
#
#     def get_private_pin(self):
#         return self.__pin1      # private attribute
#
#
# class ChildrenCreditCard(CreditCard):
#     def __init__(self, number, name: str, cvv: str, expiration_date: str, pin: str, pin1: str):
#         super().__init__(number, name, cvv, expiration_date, pin, pin1)
#         self._pin = pin
#
#
# mastercard = CreditCard('411111111111111', 'Test name', "123", "2024-11", "0000", "0001")
# print(mastercard.get_protected_pin())
# print(mastercard.get_private_pin())

# class Person:
#
#     def __init__(self, age=0):
#         self.age = age
#
#     @property                   # decorator getter, name of the property is same for all attributes getter
#     def age(self):              # before return, the getter goes true the setter.
#         return self.__age       # if age is not private attribute, recursion is enabled. infinite loop in the setter!
#
#     @age.setter                 # decorator setter, the name starts with attribute name!
#     def age(self, age):
#         if age < 0:
#             raise ValueError('Age cannot be negative!')
#         if age < 18:
#             self.__age = 18     # if age is not private attribute, recursion is enabled. infinite loop in the setter!
#         else:
#             self.__age = age    # if age is not private attribute, recursion is enabled. infinite loop in the setter!
#
#
# danio = Person()
# danio.age = 18
# print(danio.age)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# person = Person('Peter')
# print(setattr(person, 'name', 'George')) # None
# print(person.name) # George
# print(setattr(person, 'age', 21)) # None

# class Phone:
#     def __setattr__(self, attr, value):
#         self.__dict__[attr] = value.upper()
#
#
# phone = Phone()
# phone.color = 'blue'
# phone.name = 'Samsung'
# print(phone.color)  # BLUE
# print(phone.name)  # SAMSUNG

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# person = Person('Peter')
# print(person.name)              # Peter
# print(delattr(person, 'name'))  # None
# print(person.name)              # AttributeError

# class Phone:
#     def __delattr__(self, attr):
#         del self.__dict__[attr]
#         print(f"'{str(attr)}' was deleted")
#
#
# phone = Phone()
# phone.color = 'black'
# del phone.color # 'color' was deleted

# class Employee:
#     name = 'Diyan'
#     salary = '25000'
#
#     def show(self):
#         print(self.name)
#         print(self.salary)
#
#
# employee = Employee()
# print(getattr(employee, 'name')) # Diyan
# print(hasattr(employee, 'name')) # True
# setattr(employee, 'height', 152)
# print(getattr(employee, 'height')) # 152
# delattr(Employee, 'salary')