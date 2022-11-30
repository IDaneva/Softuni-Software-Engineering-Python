from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    @staticmethod
    def create_horsey(horse_type):
        if horse_type == "Appaloosa":
            return Appaloosa
        elif horse_type == "Thoroughbred":
            return Thoroughbred

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        for horse in self.horses:
            if horse.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in ["Appaloosa", "Thoroughbred"]:
            self.horses.append(self.create_horsey(horse_type)(horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            self.jockeys.append(Jockey(jockey_name, age))
            return f"Jockey {jockey_name} is added."

        raise Exception(f"Jockey {jockey_name} has been already added!")

    def create_horse_race(self, race_type: str):
        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            self.horse_races.append(HorseRace(race_type))
            return f"Race {race_type} is created."

        raise Exception(f"Race {race_type} has been already created!")

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        found_available = [h for h in self.horses if not h.is_taken and h.__class__.__name__ == horse_type]

        if not found_available:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        jockey.horse = found_available[-1]
        jockey.horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {jockey.horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None
        winner_speed = 0
        for j in race.jockeys:
            if j.horse.speed > winner_speed:
                winner_speed = j.horse.speed
                winner = j
        return f"The winner of the {race_type} race, with a speed of {winner_speed}km/h is {winner.name}!" \
               f" Winner's horse: {winner.horse.name}."


horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
