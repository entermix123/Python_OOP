from typing import List

from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ALLOWED_ASTRONAUT_TYPES = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository: PlanetRepository = PlanetRepository()
        self.astronaut_repository: AstronautRepository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):

        astronauts = [x.name for x in self.astronaut_repository.astronauts]

        if name in [x.name for x in astronauts]:
            return f"{name} is already added."

        if astronaut_type not in self.ALLOWED_ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        self.astronaut_repository.astronauts.append(self.ALLOWED_ASTRONAUT_TYPES[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        items = items.split(', ')
        if [x for x in self.planet_repository.planets if x.name == name]:
            return f"{name} is already added."

        self.planet_repository.planets.append(Planet(name))
        created_planet = [x for x in self.planet_repository.planets if x.name == name][0]
        for item in items:
            created_planet.items.append(item)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = [x for x in self.astronaut_repository.astronauts if x.name == name]
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.astronauts.remove(astronaut[0])
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = [x for x in self.planet_repository.planets if x.name == planet_name]
        if not planet:
            raise Exception("Invalid planet name!")
        planet = planet[0]

        astronauts = [x for x in self.astronaut_repository.astronauts if x.oxygen > 30]
        if not astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_astronauts = sorted(astronauts, key=lambda x: -x.oxygen)
        sorted_astronauts = [x for x in sorted_astronauts]
        count_astronauts = min(5, len(sorted_astronauts))
        selected_astronauts: List[Astronaut] = []
        for x in range(count_astronauts):
            astronaut = selected_astronauts[x]
            selected_astronauts.append(astronaut)

        self.start_mission(selected_astronauts, planet)

    def start_mission(self, selected_astronauts, planet):
        count = 0
        for a in selected_astronauts:
            items_collected = []
            count += 1
            for i in range(len(planet.items) - 1, -1, -1):
                oxygen_needed = a.breathe()
                if a.oxygen - oxygen_needed <= 0:
                    break
                a.breathe()
                a.backpack.append(planet.items(i))
            planet.items -= items_collected
            if not planet.items:
                self.successful_missions += 1
                return f"Planet: {planet.name} was explored. {count} astronauts participated in collecting items."
        self.not_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        astronauts_info = ''
        result = f'{self.successful_missions} successful missions!\n'
        result += f"Astronauts' info:\n"
        for a in self.astronaut_repository.astronauts:
            astronauts_info = f"Name: {a.name}\nOxygen: {a.oxygen}\nBackpack items: "
            if a.backpack:
                items = f"{', '.join(x for x in a.backpack)}"
            else:
                items = "None"
            astronauts_info += items
            result += astronauts_info
        return result


