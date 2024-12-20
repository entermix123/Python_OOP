class vowels:

    def __init__(self, string):
        self.string = string
        self.vowels = 'aeiouy'
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            letter = self.string[self.index]
            self.index += 1
            if letter.lower() in self.vowels:
                return letter
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
