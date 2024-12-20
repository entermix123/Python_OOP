class Account:
    def __init__(self, id: int, balance: int, pin: int):    # initialization of the account class
        self.__id = id                                      # set private id attribute
        self.__pin = pin                                    # set private pin attribute
        self.balance = balance                              # set public balance attribute

    def get_id(self, pin):       # set function for showing private id
        if pin == self.__pin:    # check if entered pin equals the private pin
            return self.__id     # return private __id attribute
        else:
            return "Wrong pin"          # return wrong pin if entered pin is different from private pin

    def change_pin(self, old_pin, new_pin):  # set function for changing private pin
        if old_pin == self.__pin:            # check if entered pin equals the private pin
            self.__pin = new_pin             # set private __pin attribute as new pin
            return "Pin changed"             # return pin changed
        else:                                # if entered pin is different from private pin
            return "Wrong pin"               # return wrong pin


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
