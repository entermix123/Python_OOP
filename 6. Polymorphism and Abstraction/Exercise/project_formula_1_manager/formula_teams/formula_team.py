from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self.budget = budget
        # self.sponsors: Dict[str: []] = {}
        # self.expenses: int = 0
        # self.revenue = 0

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def expenses_for_one_race(self):
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:       # valid integer
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        for positions in self.sponsors.values():
            for pos in positions.keys():
                if race_pos <= pos:
                    revenue += positions[pos]
                    break

        revenue -= self.expenses_for_one_race
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    # @abstractmethod
    # def calculate_revenue_after_race(self, race_pos: int):
    #     ...
    #
    # @abstractmethod
    # def get_budget(self) -> int:
    #     ...

