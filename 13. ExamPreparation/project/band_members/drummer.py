from project_pizza.project import Musician


class Drummer(Musician):

    AVAILABLE_SKILLS = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.available_skills_to_learn = self.AVAILABLE_SKILLS
