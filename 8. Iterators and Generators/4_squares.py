def squares(n):
    for i in range(1, n+1):
        yield i * i            # consume the generator object


print(list(squares(5)))
