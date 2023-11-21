# class My_List:
#     def __init__(self, items):
#         self.items = items
#
#     def __len__(self):
#         return len(self.items)
#
#
# p1 = My_List([1, 2, 3, 4])
# print(len(p1))

# class My_List:
#     def __init__(self, items):
#         self.items = items
#
#     def __getitem__(self, index):
#         return self.items[index]
#
#
# my_list = My_List([1, 2, 3, 4])
# print(my_list[2])

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3.x, v3.y)

# class EQ:
#
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):                              # check equivalent
#         return self.x == other.x and self.y == other.y    # check equivalent
#
#
# p1 = EQ(1, 2)      # create p1
# p2 = EQ(1, 2)      # create p2
# p3 = EQ(2, 3)
# print(p1 == p2)       # check equivalent --> True
# print(p1 == p3)       # check equivalent --> False

#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'name={self.name}, age={self.age}'
#
#     def __str__(self):
#         return f'name={self.name}, age={self.age}'
#
#
# p = Person('John', 30)
# print(str(p))               # __str__ --> name=John, age=30
# print(repr(p))              # __repr__ --> name=John, age=30
# print(str('10'))            # __str__ --> 10
# print(repr('10'))           # __repr__ --> '10'


# Change class attributes
#
# class MyClass:
#     class_attribute = 'class value'
#
#     def __init__(self, instance_attribute):
#         self.instance_attribute = instance_attribute
#
#
# object1 = MyClass('value1')
# object2 = MyClass('value2')
#
# print(object1.instance_attribute)                 # value1
# print(object2.instance_attribute)                 # value2
#
# object1.instance_attribute = 'new value'
# print(object1.instance_attribute)                 # new value
#
# object1.new_instance_attribute = 'new instance value'
# print(object1.instance_attribute)                   # value1
# print(object1.new_instance_attribute)               # new instance value
#
# print(MyClass.class_attribute)                    # class value
# MyClass.class_attribute = 'new class value'
# print(MyClass.class_attribute)                    # new class value

# class Rectangle:
#
#     """Class comment - represent Rectangle class"""
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#
#         """Calculate the area of rectangle"""
#
#         return self.length * self.width
#
#
# object1 = Rectangle(5, 10)
# print(Rectangle.__doc__)            # represent class comments
# print(Rectangle.area.__doc__)       # represent class method comment
# print(object1.__doc__)              # represent class comment

#
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         return f'My name is {self.name} and O am an {self.age} years old.'
#
#
# person1 = Person('Ivan', 30)
# person2 = Person('Maria', 25)
# print(person1.__dict__)
# print(person2.__dict__)
#
# data = person1.__dict__
# print(data)
#
# for k, v in data.items():
#     print(k, v)


# DICT class EXAMPLE
#
# class KeyValueStore:
#
#     def __init__(self):             # initialize dictionary
#         self._data = {}             # define dictionary
#
#     def set(self, key, value):      # define add to dictionary method
#         self._data[key] = value     # define dictionary pair action
#
#     def get(self, key):             # define get dictionary key method
#         return self._data.get(key)  # define get dictionary action with get() function
#
#
# store = KeyValueStore()             # define object
# store.set('name', 'Maria')          # set object key = 'name', object value = 'Maria'
# store.set('age', 30)                # set object key = 'age', object value = 30
#
# print(store.__dict__)               # {'_data': {'name': 'Maria', 'age': 30}}
