# Example
# my_list = [1, 2, 3, 4, 5]
#
# my_iterator = iter(my_list)     # iterator object
#
# print(next(my_iterator))        # next function takes 1 (next) argument fot the iterator
# print(next(my_iterator))        # if there are no more elements in the iterator, it will raise StopIteration exception
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))        # raise StopIteration exception


# Example
# class MyIterator:
#
#     def __init__(self, start=1, end=11):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.end:
#             result = self.current
#             self.current += 1
#             return result
#         else:
#             raise StopIteration
#
#
# my_iterator = MyIterator()
#
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # print(next(my_iterator))
# # ...
#
# for num in my_iterator:
#     print(num)


# Example
# my_list = [4, 7, 0, 3]
#
# # get an iterator using iter()
# my_iter = iter(my_list)
#
# print(next(my_iter))        # 4
# print(next(my_iter))        # 7
#
# print(my_iter.__next__())   # 0
# print(my_iter.__next__())   # 3
#
# next(my_iter)               # Error


# Example
# my_list = [1, 2, 3, 4, 5]
# my_iter = iter(my_list)
#
# # for element in my_list:     # for cycle call automatic iter functions, more used in Python
# #     print(element, end=" ")  # 1 2 3 4 5
#
# while True:
#     try:
#         element = next(my_iter)
#         print(element)
#     except StopIteration:
#         break

# Example take range from class
# class MyRange:
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             result = self.start
#             self.start += 1
#             return result
#         else:
#             raise StopIteration
#
#
# for i in MyRange(1, 6):     # for cycle receive range directly from class
#     print(i, end=" ")


# # Example1 Generator
# def string_generator(string):
#     for char in string:
#         yield char                # from last iteration continue to next iteration till string is exhausted
#         # return char                 # return first iteration and break the cycle
#
#
# my_string = string_generator("Hello MF")
# for char in string_generator(my_string):
#     print(char, end=" ")        # yield char: H e l l o   M F      # return char: H

# # Example2 Generator
# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
#
# sum_first_n = sum(first_n(5))
# print(sum_first_n)

# Example3 Generator
# def my_generator(n):
#     i = 0
#
#     while i < n:
#         yield i
#         i += 1
#
#
# gen = my_generator(5)
#
# for value in gen:
#     print(value, end=" ")

# Example4 Generator
# def return_example():
#     return 1    # 1
#     return 2    # return <generator object yield_example at 0x000001AE8794B8A0>, because the function is interpreted
#
#
# def yield_example():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#
#
# print(return_example())     # 1, <generator object yield_example at 0x000001AE8794B8A0>
# print(yield_example())      # ' '
#
# for value in yield_example():
#     print(value, end=" ")       # 1 2 3 4 5 goes true every yield statement and returns value

# Example5 Generator
# def count_up_to(n):
#     num = 1
#
#     while num <= n:
#         yield num
#         num += 1
#
#
# it = count_up_to(5)
#
# for num1 in count_up_to(5):
#     print(num1, end=" ")    # 1 2 3 4 5

# def my_gen():
#
#     n = 1
#     print('This is printed first')
#     yield n
#
#     n += 1
#     print('This is printed second')
#     yield n
#
#     n += 1
#     print('This is printed at last')
#     yield n
#
#
# gen = my_gen()
# for num in gen:
#     print(num)

# comprehension: generator expression example

class SumOfSquares:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return (x * x for x in range(self.start, self.end + 1))     # generator expression

    def sum(self):
        return sum(self)


s = SumOfSquares(1, 5)

for x in s:
    print(x, end=" ")   # 1 4 9 16 25

print(s.sum())          # 55
