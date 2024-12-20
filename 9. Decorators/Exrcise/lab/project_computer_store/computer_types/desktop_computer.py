from project_computer_store.computer_types.computer import Computer


class DesktopComputer(Computer):

    @property
    def type(self):                 # property to check if computer type is valid for desktop computer
        return "desktop computer"

    @property                       # property to assign computer max ram
    def max_ram(self):
        return 128

    @property                       # property to check if computer type is valid in dictionary
    def av_processor(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }
