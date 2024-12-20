def multiply(times):                                    # create decorator maker
    # return lambda f: lambda *args, **kwargs: f(*args, **kwargs) * times   # one line solution bad for reading
    def decorator(function):                            # create decorator function
        def wrapper(*args, **kwargs):                   # create wrapper function
            return function(*args, **kwargs) * times    # return result of original function
        return wrapper                                  # return wrapper function
    return decorator                                    # return decorator function


@multiply(3)            # use decorator function 3 times
def add_ten(number):
    return number + 10


print(add_ten(3))
