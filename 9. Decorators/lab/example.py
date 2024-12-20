# def outer_function(x):
#
#     # inner function have access to outer function, that allow to remember x after execution of outer function
#     def inner_function(y):
#         return x + y
#     return inner_function
#
#
# closure = outer_function(10)      # create closure function x = 10 and save it
# print(closure(5))       # 15      # execute closure with x = 10 and y = 5

# def print_message(message):
#     def message_sender():
#         "Nested Function"
#         print(message)
#     message_sender()
#
#
# print_message("Some random message")

# Example with Function
# def my_decorator(func):                 # require function
#     def wrapper():                      # create wrapper function
#         print('Before func is called')  # first print before function say_hello()
#         func()                          # call the actual function say_hello(): print('Hello')
#         print('After func is called')   # second print after func say_hello()
#     return wrapper                      # return wrapper function
#
#
# @my_decorator    # call the additional functionality in my_decorator, function wrapper()
# def say_hello():
#     print('Hello')
#
#
# say_hello()     # call the decorator function of say_hello() - my_decorator(say_hello)
#
#
# # result:
# # Before func is called
# # Hello
# # After func is called

# # Example with Class
# def my_decorator(cls):              # create function that require class
#     class NewClass(cls):            # create new class same as required class
#         def new_method(self):       # create method for the new class
#             print('New method')     # make functionality
#     return NewClass                 # return the instance of the new class
#
#
# @my_decorator                       # set decorator for the class MyClass
# class MyClass:
#
#     def original_method(self):      # existing function of class MyClass
#         print('Original method')
#
#
# my_object = MyClass()           # create instance of the class MyClass
# my_object.original_method()     # call the original method of class MyClass
# my_object.new_method()          # call the new method of decorator class NewClass

# def repeat(num):                        # create decorator function repeat(num)
#     def decorator_repeat(func):         # create decorator function that requires function
#         def wrapper(*args, **kwargs):   # create inner wrapper function require what ever is passed
#             for i in range(num):        # loop through
#                 func(*args, **kwargs)   # call the actual function
#         return wrapper                  # return the inner wrapper function
#     return decorator_repeat             # return the decorator decorator_repeat
#
#
# @repeat(3)                              # how many times we want to repeat
# def great(name):                        # create greet function that requires name
#     print(f"Hello {name}!")             # print hello message
#
#
# great('Maria')                          # call the greet function with name Maria

# # Example how to make changes out of the class for private attributes
# class Person:
#     def __init__(self):
#         self.__name = ''
#
#     @property                   # get the name property
#     def name(self):
#         return self.__name
#
#     @name.setter                # set the name property
#     def name(self, value):
#         self.__name = value
#
#
# person = Person()
# person.name = 'John'
# print(person.name)
# person.name = 'Maria'
# print(person.name)


# # Example Classes as Decorators
# class Cached:
#     def __init__(self, func):       # create an instance of the class Cached
#         self.func = func            # set the function to self.func
#         self.cache = {}             # create a cache for the function
#
#     def __call__(self, *args):          # call function with args
#         if args in self.cache:          # if there is a result of this input in the cache
#             return self.cache[args]     # return it
#         result = self.func(*args)       # if there is not result in cache, execute it
#         self.cache[args] = result       # store the result in the cache
#         return result                   # return the result
#
#
# @Cached
# def example(x):
#     result = x ** 2 + 3 * x + 1
#     return result
#
#
# print(example(2))   # slow, first time through
# print(example(2))   # fast, already exist in cache
# print(example(3))   # slow, first time through
# print(example(3))   # fast
