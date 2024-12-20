def type_check(expected_type):                      # Check if the type is correct function
    def decorator(func):                            # decorator receive function
        def wrapper(*args):                         # wrapper receive arguments
            for arg in args:                        # iterate true arguments
                if not isinstance(arg, expected_type):    # check if argument is correct type
                    return f"Bad Type"                    # if not correct type return error message
            return func(*args)                      # if correct type return function execution result
        return wrapper                              # return wrapper function
    return decorator                                # return decorator function


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
