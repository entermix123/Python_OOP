
def cache(func):

    def wrapper(n):

        # the check is made twice for the execution of function of fibonacci(n) - fibonacci(n-1) + fibonacci(n-2)
        # first time for  n-1 and second time for n-2
        if n not in wrapper.log:        # check if calculation has been done before, is in log
            wrapper.log[n] = func(n)    # if not in log, calculate it
        return wrapper.log[n]           # save calculation in log

    wrapper.log = {}                    # initialize log dictionary

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(50)
print(fibonacci.log)
