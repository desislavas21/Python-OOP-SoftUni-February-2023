from project.pokemon import Pokemon
from typing import List


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: str) -> str:
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
            self.pokemons.remove(pokemon)
            return f"You have released {pokemon_name}"
        except StopIteration:
            return "Pokemon is not caught"

    def trainer_data(self):
        final = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            final += f"- {pokemon.pokemon_details()}\n"
        return final

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
