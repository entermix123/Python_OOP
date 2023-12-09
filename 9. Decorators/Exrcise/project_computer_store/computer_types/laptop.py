from project_computer_store.computer_types.computer import Computer


class Laptop(Computer):

    @property                   # property to check if computer type is valid for Laptop
    def type(self):
        return "laptop"

    @property                   # property to assign computer max ram
    def max_ram(self):
        return 64

    @property
    def av_processor(self):     # property to check if computer type is valid in dictionary
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }
