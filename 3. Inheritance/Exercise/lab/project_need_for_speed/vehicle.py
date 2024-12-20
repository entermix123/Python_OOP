class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption: float = self.DEFAULT_FUEL_CONSUMPTION
        # using self.DEFAULT_FUEL_CONSUMPTION gurantees every inheritance class he same attribute

    def drive(self, kilometers: int):
        if self.fuel - kilometers * self.fuel_consumption >= 0:
            self.fuel -= kilometers * self.fuel_consumption
