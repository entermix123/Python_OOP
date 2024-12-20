from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players_list: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players: Player):
        players_added = []
        for player in [*players]:
            if player not in self.players_list:
                self.players_list.append(player)
                players_added.append(player)

        return f"Successfully added: {', '.join([x.name for x in players_added])}"

    def add_supply(self, *supplies: Supply):
        for supply in [*supplies]:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):

        # check ths sustenance type
        if sustenance_type not in Supply.TYPES:
            return

        for player in self.players_list:
            if player.name == player_name:
                break
        else:
            return

        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        for idx in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[idx]

            if supply.__class__.__name__ == sustenance_type:
                self.supplies.pop(idx)
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(player.stamina + supply.energy, 100)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        # first_player = [x for x in self.players_list if x.name == first_player_name][0]
        # second_player = [x for x in self.players_list if x.name == second_player_name][0]

        # find players and sort them by stamina ascending
        players = sorted([
            next(filter(lambda x: x.name == first_player_name, self.players_list)),
            next(filter(lambda x: x.name == second_player_name, self.players_list)),
        ], key=lambda p: p.stamina)

        errors = []
        for player in players:
            if player.stamina <= 0:
                errors.append(f"Player {player.name} does not have enough stamina.")
        if errors:
            return '\n'.join(errors)

        return self.fight(players)

    def fight(self, players: List[Player]):

        first_player_dmg = players[0].stamina / 2
        players[1].stamina = max(players[1].stamina - first_player_dmg, 0)

        second_player_dmg = players[1].stamina / 2
        players[0].stamina = max(players[0].stamina - second_player_dmg, 0)

        winner = sorted(players, key=lambda x: -x.stamina)[0]
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players_list:
            if (player.stamina - player.age * 2) <= 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        result = '\n'.join([x.__str__() for x in self.players_list]) + '\n' + '\n'.join(
            [x.details() for x in self.supplies])
        return result
