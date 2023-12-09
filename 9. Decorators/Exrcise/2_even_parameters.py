def even_parameters(func):      # receive function
    def wrapper(*args):         # receive function arguments
        for arg in args:        # iterate true arguments
            if isinstance(arg, int):    # check if argument is an integer
                if arg % 2 == 0:        # check if argument is even number
                    continue            # if it is even integer, continue to the next argument
            return "Please use only even numbers!"  # if not an integer, return message

        return func(*args)              # if all arguments are even integers, return function result

    return wrapper                      # return wrapper function


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
