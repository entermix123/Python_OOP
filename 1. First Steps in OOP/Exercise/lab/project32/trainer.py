from typing import List
from guild_system.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []       # define empty list for current trainer

    def add_pokemon(self, pokemon: Pokemon) -> str:     # received instance of class Pokemon
        if pokemon in self.pokemons:                    # check if received pokemon is in pokemon db - class pokemon
            return f'This pokemon is already caught'
        else:
            self.pokemons.append(pokemon)               # if is not, add object
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:        # defining releasing pokemon

        # case with comprehension
        # try:
        #     pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]  # comprehension, return 0 index
        # except StopIteration:
        #     return f"Pokemon is not caught"

        # case with next(), filter() and lambda
        try:                                        # try to release pokemon
            # using next(), filter() and lambda to search true the list defined in __init__
            # filter() is iterator and save it in memory
            # next() take that element from memory and return it
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:                               # if pokemon not found in trainer collection/error raised
            return f"Pokemon is not caught"                 # return result

        self.pokemons.remove(pokemon)                       # if found in trainer list of pokemons, release it

        return f"You have released {pokemon_name}"          # return result

    def trainer_data(self) -> str:                      # create trainer

        # make collection of items in class Pokemons
        pokemons_data = "\n".join(f"- {p.pokemon_details()}" for p in self.pokemons)

        # return result from requirement
        return f"Pokemon Trainer {self.name}\n" + \
               f"Pokemon count {len(self.pokemons)}\n" + \
               f"{pokemons_data}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
