def reverse_text(string):
    for x in reversed(string):
        yield x


for char in reverse_text("step"):
    print(char, end='')