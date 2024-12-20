class Person:
    def __init__(self, name, age):
        self.__name = name              # mangled name(погрознено име на атрибута за име на човека)
        self.__age = age                # mangled age(погрознено име на атрибута за възраст на човека)

    def get_age(self):                  # function that can be used to get the age outside the class
        return self.__age

    def get_name(self):                 # function that can be used to get the name outside the class
        return self.__name


person = Person("George", 32)
print(person.get_name())
print(person.get_age())
