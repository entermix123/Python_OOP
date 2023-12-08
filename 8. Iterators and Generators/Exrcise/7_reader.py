def read_next(*args):

    for collection in args:         # iterate true input of collections
        for char in collection:     # iterate true current collection
            yield char              # yield true current collection


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)