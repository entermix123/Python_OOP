# def choose_pattern():
#     user_figure = input("Figure for represent:\n"
#                         "1: triangle\n"
#                         "2: rombus\n"
#                         "3: square\n"
#                         "Select Figure: ")
#     size1 = int(input("Select size of the figure: "))
#     return user_figure, size1
#
#
# def print_figure(spaces, stars):
#     print(' ' * spaces + '* ' * stars)
#
#
# def choose_figure(pattern, size):
#     if pattern == '1':              # triangle
#         for a in range(0, size):
#             spaces = size - a
#             stars = a + 1
#             print_figure(spaces, stars)
#
#     elif pattern == '2':           # rombus
#         for x in range(0, size):
#             spaces = size - x - 1
#             stars = x + 1
#             print_figure(spaces, stars)
#
#         for x in range(size - 2, -1, -1):
#             spaces = size - x - 1
#             stars = x + 1
#             print_figure(spaces, stars)
#
#     elif pattern == '3':          # square
#         for x in range(0, size):
#             stars = x + 1
#             print_figure(0, stars)
#
#
# result1, result2 = choose_pattern()
# choose_figure(result1, result2)

size = int(input())

for x in range(0, size):
    spaces = size - x - 1
    stars = x + 1
    print(' ' * spaces + '* ' * stars)

for x in range(size - 2, -1, -1):
    spaces = size - x - 1
    stars = x + 1
    print(' ' * spaces + '* ' * stars)
