from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    ALLOWED_HORSE_BREDS = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
    ADDED_HORSES = {"Appaloosa": [], "Thoroughbred": []}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        # if horse in self.
        if horse_name in [x.name for x in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.ALLOWED_HORSE_BREDS.keys():
            # create horse
            horse = self.ALLOWED_HORSE_BREDS[horse_type](horse_name, horse_speed)

            # add horse to ADDED_HORSES
            self.ADDED_HORSES[horse_type].append(horse_name)

            # add horse to self.horses
            self.horses.append(horse)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [x.name for x in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        # create jockey and add it to self.jockeys
        self.jockeys.append(Jockey(jockey_name, age))

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):

        # check if race already in created races
        if [x for x in self.horse_races if x.race_type == race_type]:
            raise Exception(f"Race {race_type} has been already created!")

        # create race
        race = HorseRace(race_type)

        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        # check if jockey is created
        current_jockey = [x for x in self.jockeys if x.name == jockey_name]

        # if not created
        if not current_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        # set existing jockey
        current_jockey = current_jockey[0]

        # find if existing horses form this type
        horses_from_type = [x for x in self.horses if x.__class__.__name__ == horse_type]

        # if existing horses from this type
        if not horses_from_type:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        # check if eny of found horses is not taken
        available_horse = [x for x in horses_from_type if x.is_taken == False]

        # if not available horse
        if not available_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        # set available horse
        available_horse = available_horse[0]

        # check if jockey have a horse
        if current_jockey.horse:
            return f"Jockey {current_jockey.name} already has a horse."

        # add the available horse to jockey
        current_jockey.horse = available_horse

        # set horse as taken
        available_horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {current_jockey.horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        # if not existing race
        if not [x for x in self.horse_races if x.race_type == race_type]:
            raise Exception(f"Race {race_type} could not be found!")

        # find if existing jockey
        current_jockey = [x for x in self.jockeys if x.name == jockey_name]

        # if jockey don't exist
        if not current_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        # of not existing jockey
        current_jockey = current_jockey[0]

        if not current_jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        # find current race
        current_race = [x for x in self.horse_races if x.race_type == race_type][0]

        # check if jockey is already added to the race
        if current_jockey in current_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        # add jockey to the race
        current_race.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        # find current race
        current_race = [x for x in self.horse_races if x.race_type == race_type]

        # check if current race exist
        if not current_race:
            raise Exception(f"Race {race_type} could not be found!")

        # validate race participants
        current_race = current_race[0]

        # check if participants are minimum two
        if len(current_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        winner_jockey = ""
        winner_horse = ""

        for jockey in current_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                winner_jockey = jockey.name
                winner_horse = jockey.horse.name

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is" \
               f" {winner_jockey}! Winner's horse: {winner_horse}."
