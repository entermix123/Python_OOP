import time    # import time module


def exec_time(func):            # create a function receive a function as argument
    def wrapper(*args):         # create a wrapper function
        start = time.time()     # start = start time of the function
        func(*args)             # call the function
        end = time.time()       # end = end time of the function
        return end - start      # return difference between start and end time
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))    # 0.7956018447875977 result of measurement

