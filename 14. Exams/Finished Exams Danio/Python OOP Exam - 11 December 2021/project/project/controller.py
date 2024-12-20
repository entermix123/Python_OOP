from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    ALLOWED_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):

        if model in [x.model for x in self.cars]:
            raise Exception(f"Car {model} is already created!")

        if car_type in self.ALLOWED_CAR_TYPES:
            self.cars.append(self.ALLOWED_CAR_TYPES[car_type](model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [x.name for x in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        cars = []

        if driver_name not in [x.name for x in self.drivers]:
            raise Exception(f"Driver {driver_name} could not be found!")
        driver = next(filter(lambda x: x.name == driver_name, self.drivers))
        # driver = [x for x in self.drivers if x.name == driver_name][0]

        for c in range(len(self.cars) - 1, -1, -1):
            if not self.cars[c].is_taken and self.cars[c].__class__.__name__ == car_type:
                cars.append(self.cars[c])
        if not cars:
            raise Exception(f"Car {car_type} could not be found!")
        available_car = cars[0]

        if driver.car is not None:
            old_car = driver.car
            old_car_idx = self.cars.index(old_car)
            driver.car = available_car
            self.cars[old_car_idx].is_taken = False
            available_car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_car.model} to {available_car.model}."

        driver.car = available_car
        available_car.driver = driver
        available_car.is_taken = True
        return f"Driver {driver_name} chose the car {available_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):

        if race_name not in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} could not be found!")

        if driver_name not in [x.name for x in self.drivers]:
            raise Exception(f"Driver {driver_name} could not be found!")

        race = next(filter(lambda x: x.name == race_name, self.races))
        driver = next(filter(lambda x: x.name == driver_name, self.drivers))

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for rc in self.races:
            for dr in rc.drivers:
                if dr.name == driver_name:
                    raise Exception(f"Driver {driver_name} is already added in {rc.name} race.")

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race.name} race."

    def start_race(self, race_name: str):

        if race_name not in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} could not be found!")

        race = next(filter(lambda x: x.name == race_name, self.races))

        if len(race.drivers) < 3:
            raise Exception(f"Race {race.name} cannot start with less than 3 participants!")

        cars = [x.car for x in race.drivers]
        drivers = [x for x in race.drivers]
        winners = sorted(cars, key=lambda x: (-x.speed_limit))

        result = []
        for idx in range(3):
            driver = [x for x in drivers if x.car == winners[idx]][0]
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(result)
