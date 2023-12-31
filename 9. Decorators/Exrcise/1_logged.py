def logged(function):
    def wrapper(*args):
        function(*args)
        return f"you called {function.__name__}({', '.join(str(arg) for arg in args)})\n" \
               f"it returned {function(*args)}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
