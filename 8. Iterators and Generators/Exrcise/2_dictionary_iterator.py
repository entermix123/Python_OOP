class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())   # return a tuple of (key, value) pairs
        self.length = len(dictionary.keys())    # end of dictionary condition
        self.index = -1                         # start index

    def __iter__(self):         # return an iterator object of class object
        return self

    def __next__(self):
        if self.index >= len(self.items) - 1:   # if iteration not in range
            raise StopIteration                 # raise StopIteration exception

        self.index += 1                         # increase index by 1

        return self.items[self.index]           # return item pair


result = dictionary_iter({"name": "Peter",
"age": 24})
for x in result:
    print(x)
