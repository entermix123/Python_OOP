from time import sleep, time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f'Function {func.__name__} took {end_time - start_time} seconds')
        return result
    return wrapper


@measure_time           # by decorator function we can measure time of a function
def slow_function(n):
    sleep(n)


slow_function(2)
