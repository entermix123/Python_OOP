from abc import abstractmethod, ABC     # import abstraction


class Person(ABC):          # create abstract class

    def __init__(self, name, age):      # inherited in every other class (Employee and Boss)
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1

    @abstractmethod         # force inherited classes to implement this method
    def work(self):
        ...


class Employee(Person):

    def work(self):             # Duck typing
        print("Working...")


class Boss(Person):

    def work(self):             # Duck typing
        print("Taking risks")


instances = [Boss("Ivan", 20), Employee("John", 19)]    # create instances

for instance in instances:      # iterate true instances
    instance.work()             # use common method work()
