# Example Classes as Decorators

class Cached:
    def __init__(self, func):       # create an instance of the class Cached
        self.func = func            # set the function to self.func
        self.cache = {}             # create a cache for the function

    def __call__(self, *args):          # call function with args
        if args in self.cache:          # if there is a result of this input in the cache
            return self.cache[args]     # return it
        result = self.func(*args)       # if there is not result in cache, execute it
        self.cache[args] = result       # store the result in the cache
        return result                   # return the result


@Cached
def example(x):
    result = x ** 2 + 3 * x + 1
    return result


print(example(2))   # slow, first time through
print(example(2))   # fast, already exist in cache
print(example(3))   # slow, first time through
print(example(3))   # fast
