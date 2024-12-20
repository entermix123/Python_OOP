def vowel_filter(function):     # create decorator function that require a function

    def wrapper():                          # inner decorator function
        letters = function()                # call function
        vowels = ["a", "e", "i", "o", "u"]
        filtered_letters = [k for k in letters if k in vowels]
        return filtered_letters
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
