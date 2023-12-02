from project_formula_1_manager.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def sponsors(self):
        return {
            'Petronas': {
                1: 1_000_000,
                3: 500_000
            },
            'TeamViewer': {
                5: 100_000,
                7: 500_00
            }
        }

    @property
    def expenses_for_one_race(self):
        return 200_000

    # def __init__(self, budget: int):
    #     super().__init__(budget)
    #     self.BUDGET = budget
    #     self.sponsors = MercedesTeam.SPONSORS
    #     self.expenses = 250000
    #
    # @abstractmethod
    # def calculate_revenue_after_race(self, race_pos: int):
    #     # sponsor_value = [[x for x in self.sponsors.values()] for y in self.sponsors.keys() if str(race_pos) in self.sponsors[y]]
    #     for x in self.sponsors.values():
    #         if str(race_pos) in self.sponsors[x].keys():
    #             self.revenue += self.sponsors[x][race_pos]
    #
    #     self.revenue -= self.expenses
    #     return self.revenue
    #
    # @abstractmethod
    # def get_budget(self):
    #     self.BUDGET += self.revenue
    #     return f"The revenue after the race is {self.revenue}$. Current budget { self.BUDGET }$"
