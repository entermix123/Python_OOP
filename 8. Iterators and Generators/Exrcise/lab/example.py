
# REVIEW OF ITERATORS
# from typing import List  # import list
#
#
# class MyList:   # create class
#
#     def __init__(self, my_list: List):      # initialize the list
#         self.my_list = my_list              # assign the list to the class
#         self.index = -1     # start index -1, because first loop increase index by 1 and use index 0
#
#     def __iter__(self):         # called only the first time when iterating true the collection MyList
#         return self    # 90 % of times return iteself- self
#
#     def __next__(self):
#         if self.index == len(self.my_list) - 1:     # check if end range of the list is reached
#             raise StopIteration                     # if end range is reached raise StopIteration
#         self.index += 1                             # increment index by 1
#
#         return self.my_list[self.index]             # return the element at index
#

# solution 1
# my_list = MyList([1, 2, 3])     # create a list with elements 1, 2, 3
# for el in my_list:              # iterate over the list
#     print(el)                   # print the elements

# solution 2
# a = iter([1, 2, 3])             # create an iterator with elements 1, 2, 3
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))      # error StopIteration

# solution 3
# my_list = iter(MyList([1, 2, 3]))   # create an iterator with elements 1, 2, 3
# print(next(my_list))                # print the elements of index 0
# print(next(my_list))                # print the elements of index 1
# print(next(my_list))                # print the elements of index 2
# # print(next(my_list))                # error StopIteration


# REVIEW OF GENERATORS

def add_one_to_numer_in_list(numbers):

    for num in numbers:     # when go true for cycle to print, then goes true for cycle to yield
        yield num + 1       # every time continue last iteration with yield


b = add_one_to_numer_in_list([1, 2, 3])     # create object
for el in b:                                # iterate over the list
    print(el, end=" ")  # 2 3 4             # print each element on same line
