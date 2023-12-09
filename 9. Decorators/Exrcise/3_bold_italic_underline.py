def make_bold(func):        # decorator receive function @make_italic
    def wrapper(*args):
        return f"<b>{func(*args)}</b>"  # execute function @make_italic with args
    return wrapper                      # return result to call print(greet("Peter"))


def make_italic(func):      # decorator receive function @make_underline
    def wrapper(*args):
        return f"<i>{func(*args)}</i>"  # execute function make_underline with args
    return wrapper                      # return result to function @make_bold


def make_underline(func):   # decorator receive function greet(name)
    def wrapper(*args):
        return f"<u>{func(*args)}</u>"  # execute function greet(name)
    return wrapper                      # return result to function @make_italic


@make_bold          # decorator decorate make_italic
@make_italic        # decorator decorate make_Underline
@make_underline     # decorator decorate geet function
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
