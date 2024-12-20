class store_results:        # if we name class with small letter, we can use it as a function !!!

    def __init__(self, func):   # receive func as parameter
        self.func = func        # assign func to the class

    def __call__(self, *args):  # create call function
        with open("result.txt", "a") as result_file:    # create a file called result.txt
            # append the function name and result to the file
            result_file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
