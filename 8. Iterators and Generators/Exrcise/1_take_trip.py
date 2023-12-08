class take_skip:

    # 2 problems:
    # problem 1: how to look over the number of iterations we make?
    # problem 2: how not to change attributes that are received by the constructor

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = -1    # problem 1 solution, start from -1 because first iteration is increase by 1

    def __iter__(self):         # what we iterate true?
        return self             # object - instance of current class

    def __next__(self):
        if self.iterations == self.count - 1:   # create a StopIteration condition - max count is reached
            raise StopIteration

        self.iterations += 1                    # add 1 to the iteration count

        return self.step * self.iterations      # start from 0 (0 x 2 = 0). next step is 2 (1 x 2 = 2), and so on


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
