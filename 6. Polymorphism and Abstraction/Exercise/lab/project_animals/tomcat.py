from project_animals.cat import Cat


class Tomcat(Cat):

    def __init__(self, name: str, age, gender='Male'):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound():
        return f"Hiss"
