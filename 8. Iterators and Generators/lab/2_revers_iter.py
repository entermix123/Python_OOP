# class reverse_iter:
#
#     def __init__(self, iterable):
#         self.iterable = iter(reversed(iterable))    # reverse the list
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             return next(self.iterable)
#         except StopIteration:
#             self.iterable = iter(self.iterable)
#             return next(self.iterable)
#
#
# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)


class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.iterable[self.index]
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item, end=' ')    # 4 3 2 1
