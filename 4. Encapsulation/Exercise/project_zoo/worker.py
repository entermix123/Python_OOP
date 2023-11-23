class Worker:       # create base class

    def __init__(self, name: str, age: int, salary: float):  # create constructor
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:      # create print method
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
