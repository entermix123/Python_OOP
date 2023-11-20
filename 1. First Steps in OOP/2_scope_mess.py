x = "global"        # global x


def outer():
    x = "local"

    def inner():
        nonlocal x          # change x in outer() to 'nonlocal'
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x                # change global x to "global: changed!"
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)
