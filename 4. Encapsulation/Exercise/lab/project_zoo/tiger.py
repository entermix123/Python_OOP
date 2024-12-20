from project_zoo.animal import Animal


class Tiger(Animal):        # create class inherited from Animal
    MONEY_FOR_CARE = 45     # create class attribute that is constant = 50

    def __init__(self, name: str, gender: str, age: int):   # do not initialize money_for_care because is class attribute
        super().__init__(name, gender, age, Tiger.MONEY_FOR_CARE)  # import money_for_care and set to class attribute
