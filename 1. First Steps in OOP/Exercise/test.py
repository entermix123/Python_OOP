class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, centimeters):
        self.height += centimeters


maria = Person('Maria', 170)
maria.grow(10)

print(maria.height)
