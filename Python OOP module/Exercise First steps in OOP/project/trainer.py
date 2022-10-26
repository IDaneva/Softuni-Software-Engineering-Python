from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []
        self.names = []

    def add_pokemon(self, pokemon):
        if pokemon.name not in self.names:
            info = pokemon.pokemon_details()
            self.pokemons.append(info)
            self.names.append(pokemon.name)
            return f"Caught {info}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        if pokemon_name not in self.names:
            return f"{pokemon_name} is not caught"
        else:
            print(pokemon.pokemon_details())
            print(pokemon)
            self.pokemons.remove(pokemon.pokemon_details())
            self.names.remove(pokemon_name)
            return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = ""
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for info in self.pokemons:
            result += f"- {info}\n"
        return result


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
