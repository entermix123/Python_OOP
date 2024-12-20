from project_multi_inher.person import Person
from project_multi_inher.employee import Employee


class Teacher(Person, Employee):

    def teach(self):
        return "teaching..."
