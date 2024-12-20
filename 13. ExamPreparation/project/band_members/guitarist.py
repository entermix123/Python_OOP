from project_pizza.project import Musician


class Guitarist(Musician):

    AVAILABLE_SKILLS = ["play metal", "play rock", "play jazz"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.available_skills_to_learn = self.AVAILABLE_SKILLS
