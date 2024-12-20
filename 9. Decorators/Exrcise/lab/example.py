# def repeat_n_times(n):          # decorator maker
#     def decorator(func):        # decorator function receive function hello(name) with argument John
#         def wrapper(*args):     # wrapper function - actual logic
#             for _ in range(n):  # the logic
#                 func(*args)
#
#             # return wrapper result
#         return wrapper          # return the wrapper function
#     return decorator            # return the decorator function
#
#
# @repeat_n_times(2)  # decorators can stack multiple times. In this case function will be executed 5 * 2 = 10 times
# @repeat_n_times(5)              # pass argument 5 to decorator maker
# def hello(name):                # pass argument hello(name) to decorator outer function
#     print(f"Hello, {name}")     # logic of function hello(name)
#
#
# hello("John")                   # call hello function hello() with argument John

# # How to set parameters to decorator functions and how it works:
# class store_results:        # if we name class with small letter, we can use it as a function !!!
#
#     def __init__(self, arg):   # receive the parameter of @store_results(6)
#         self.arg = arg        # assign func to the class
#
#     def __call__(self, func):  # create call function and receive func as parameter
#         def wrapper(*args):    # receive the parameters of decorator functions
#             print(f"Function {func.__name__} was called. Result: {func(*args)}")    # print result
#             print("the argument is", self.arg)                                      # print argument
#         return wrapper
#
#
# @store_results(6)   # set parameters to decorator function
# def add(a, b):
#     return a + b
#
#
# @store_results(6)   # set parameters to decorator function
# def mult(a, b):
#     return a * b
#
#
# add(2, 2)
# mult(6, 4)
