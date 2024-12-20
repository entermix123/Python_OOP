def tags(tag):                  # create a function received a tag
    def decorator(func):        # create a decorator that receive function
        def wrapper(*args):     # create a wrapper that receive arguments
            return f"<{tag}>{func(*args)}</{tag}>"  # execute the function
        return wrapper      # return wrapper
    return decorator        # return decorator


@tags('div')
@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
