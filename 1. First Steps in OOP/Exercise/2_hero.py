class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        self.health -= damage

        # anutasion:
        # def defend(self, damage: int) -> str: /defines that the method return string

        if self.health <= 0:
            return f"{self.name} was defeated"

    def heal(self, amount):
        self.health += amount


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
