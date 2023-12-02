from project_formula_1_manager.formula_teams.mercedes_team import MercedesTeam
from project_formula_1_manager.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team: RedBullTeam or None = None
        self.mercedes_team: MercedesTeam or None = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)
        else:
            raise ValueError(f"Invalid team name!")

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception(f"Not all teams have registered for the season.")

        return self.get_race_result(race_name, red_bull_pos, mercedes_pos)

    def get_race_result(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        ahead_team = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return f"Red Bull: {red_bull_revenue}. Mercedes: {mercedes_revenue}. " \
               f"{ahead_team} is ahead at the {race_name} race."

# from typing import List
#
# from project_formula_1_manager.formula_teams.mercedes_team import MercedesTeam
# from project_formula_1_manager.formula_teams.red_bull_team import RedBullTeam
#
#
# class F1SeasonApp:
#     red_bull_team: RedBullTeam = None
#     mercedes_team: MercedesTeam = None
#     valid_team_names = List[str] = ["Red Bull", "Mercedes"]
#
#     def __init__(self, red_bull_team: RedBullTeam, mercedes_team: MercedesTeam):
#         self.red_bull_team: RedBullTeam = red_bull_team
#         self.mercedes_team: MercedesTeam = mercedes_team
#
#     @staticmethod
#     def register_team_for_season():
#         pass
#
#     def is_valid_name(self, team_name):
#         if team_name not in self.valid_team_names:
#             raise ValueError(f"Invalid team name!")
#         elif team_name == "Red Bull":
#             self.red_bull_team = RedBullTeam(team_name)
#         else:
#             self.mercedes_team = MercedesTeam(team_name)
#
#         return f"{ team_name } has joined the new F1 season."
#
#     @classmethod
#     def new_race_results(cls, race_name: str, red_bull_pos: int, mercedes_pos: int):
#         if cls.red_bull_team is None or cls.mercedes_team is None:
#             raise Exception("Not all teams have registered for the season.")
#
#         if red_bull_pos < mercedes_pos:
#             winner_team = cls.red_bull_team
#         else:
#             winner_team = cls.mercedes_team
#
#         return f"Red Bull: {cls.red_bull_team.calculate_revenue_after_race}. Mercedes: {cls.mercedes_team.calculate_revenue_after_race()}." \
#                f" {winner_team} is ahead at the {race_name} race."

