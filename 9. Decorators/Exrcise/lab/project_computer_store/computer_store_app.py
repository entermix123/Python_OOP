from project_computer_store.computer_types.laptop import Laptop
from project_computer_store.computer_types.desktop_computer import DesktopComputer


class ComputerStoreApp:             # set application class

    def __init__(self):
        self.warehouse = []     # set storage warehouse with list of Computer instances
        self.profits = 0                         # set profit value

    # set function to build a computer
    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Desktop Computer":                 # check if Desktop Computer
            computer = DesktopComputer(manufacturer, model)     # if desktop computer, create DesktopComputer instance
        elif type_computer == "Laptop":                         # check if Laptop
            computer = Laptop(manufacturer, model)              # if laptop, create Laptop instance
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")  # if not either, raise error

        # if Computer object is created
        configuration = computer.configure_computer(processor, ram)  # configure processor and ram
        self.warehouse.append(computer)                              # add Computer instance to storage warehouse
        return configuration                    # return configuration of computer

    # set function to sell a computer
    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:     # iterate through warehouse
            # if client budget is more than computer price, computer processor is equal to wanted_processor and
            # ram is equal or more than wanted_ram
            if computer.price <= client_budget and \
                    computer.processor == wanted_processor and \
                    computer.ram >= wanted_ram:

                self.profits += client_budget - computer.price   # take client budget and subtract computer price
                self.warehouse.remove(computer)                 # remove computer from storage warehouse

                return f"{computer} sold for {client_budget}$."     # return message

        # if any of the conditions above is not met, raise error
        raise Exception(f"Sorry, we don't have a computer for you.")
