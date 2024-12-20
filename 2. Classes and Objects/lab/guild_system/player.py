from typing import Dict


class Player:
    NOT_IN_GUILD = 'Unaffiliated'

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}
        self.guild = Player.NOT_IN_GUILD

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return f"Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skill_list = ['===' + str(key) + ' - ' + str(value) for key, value in self.skills.items()]
        return f'Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n{", ".join(x for x in skill_list)}'
