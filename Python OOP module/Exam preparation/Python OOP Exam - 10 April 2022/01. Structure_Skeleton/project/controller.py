from project.supply.food import Food
from project.supply.drink import Drink


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                added_players.append(player)

        self.players.extend(added_players)
        return f"Successfully added: {', '.join([x.name for x in added_players])}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        if player_name not in [x.name for x in self.players] or sustenance_type not in ["Food", "Drink"]:
            return
        player = next(filter(lambda p: p.name == player_name, self.players))

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        foods = [x for x in self.supplies if type(x) == Food]
        drinks = [x for x in self.supplies if type(x) == Drink]

        if sustenance_type == "Food":
            if not foods:
                raise Exception("There are no food supplies left!")
            food = foods[-1]
            # self.supplies.remove(food)
            indices = [i for i, x in enumerate(self.supplies) if x.name == food.name]
            self.supplies.pop(indices[-1])
            player.stamina = 100 if player.stamina + food.energy > 100 else player.stamina + food.energy
            return f"{player_name} sustained successfully with {food.name}."

        if sustenance_type == "Drink":
            if not drinks:
                raise Exception("There are no drink supplies left!")
            drink = drinks[-1]
            # self.supplies.remove(drink)
            indices = [i for i, x in enumerate(self.supplies) if x.name == drink.name]
            self.supplies.pop(indices[-1])
            player.stamina = 100 if player.stamina + drink.energy > 100 else player.stamina + drink.energy
            return f"{player_name} sustained successfully with {drink.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = next(filter(lambda p: p.name == first_player_name, self.players))
        player2 = next(filter(lambda p: p.name == second_player_name, self.players))
        if player1.stamina == 0 and player2.stamina == 0:
            return f"Player {player1.name} does not have enough stamina.\n" \
                   f"Player {player2.name} does not have enough stamina."
        if player1.stamina == 0:
            return f"Player {player1.name} does not have enough stamina."

        if player2.stamina == 0:
            return f"Player {player2.name} does not have enough stamina."

        first = player1 if player1.stamina < player2.stamina else player2
        second = player1 if first == player2 else player2

#       first one attacks second
        second.stamina = 0 if second.stamina - first.stamina / 2 < 0 else second.stamina - first.stamina / 2
        if second.stamina == 0:
            return f"Winner: {first.name}"

#       second one attacks first

        first.stamina = 0 if first.stamina - second.stamina / 2 < 0 else first.stamina - second.stamina / 2
        if first.stamina == 0:
            return f"Winner: {second.name}"

        winner = first if first.stamina > second.stamina else second
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = [str(x) for x in self.players]
        result.extend([x.details() for x in self.supplies])
        return "\n".join(result)

