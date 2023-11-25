class Equipment:
    id = 1

    def __init__(self, name: str):
        self.name = name
        self.__next_id = Equipment.id
        self.id = Equipment.get_next_id()
        Equipment.id += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.id
