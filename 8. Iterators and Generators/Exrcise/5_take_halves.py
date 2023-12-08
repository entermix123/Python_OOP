def solution():

    def integers():
        num = 1         # start number

        while True:     # infinite loop += 1
            yield num   # save last iterate number
            num += 1    # increase number by 1

    def halves():           # take half of the numbers
        for i in integers():    # call infinite loop integers()
            yield i / 2         # take half of the number form integers()

    def take(n, seq):
        return [next(seq) for _ in range(n)]    #

    return (take, halves, integers)


take = solution()[0]    # return (take, halves, integers) - index 0
halves = solution()[1]  # return (take, halves, integers) - index 1
print(take(5, halves()))    # range 5, element from halves()
