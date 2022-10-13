def data_base_generator(number_of_heroes, hero_data_base):
    for _ in range(number_of_heroes):
        hero_name, hp, mp = input().split()
        hero_data_base[hero_name] = [int(hp), int(mp)]
    return hero_data_base


def game_play(hero_data_base):
    while True:
        command = input()
        if command == "End":
            for hero in hero_data_base:
                print(hero)
                print(f"  HP: {hero_data_base[hero][0]}")
                print(f"  MP: {hero_data_base[hero][1]}")
            break

        command = command.split(" - ")
        instructions = command[0]
        hero_name = command[1]

        if instructions == "CastSpell":
            needed_mp = int(command[2])
            spell_name = command[3]
            if hero_data_base[hero_name][1] >= needed_mp:
                hero_data_base[hero_name][1] -= needed_mp
                print(f"{hero_name} has successfully cast {spell_name} and now has {hero_data_base[hero_name][1]} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif instructions == "TakeDamage":
            damage_points = int(command[2])
            attacker = command[3]

            if hero_data_base[hero_name][0] - damage_points <= 0:
                print(f"{hero_name} has been killed by {attacker}!")
                del hero_data_base[hero_name]
            else:
                hero_data_base[hero_name][0] -= damage_points
                print(f"{hero_name} was hit for {damage_points} HP by {attacker} and now has {hero_data_base[hero_name][0]} HP left!")

        elif instructions == "Recharge":
            wanted_amount = int(command[2])
            affordable_amount = 200 - hero_data_base[hero_name][1]

            if wanted_amount > affordable_amount:
                hero_data_base[hero_name][1] += affordable_amount
                print(f"{hero_name} recharged for {affordable_amount} MP!")
            else:
                hero_data_base[hero_name][1] += wanted_amount
                print(f"{hero_name} recharged for {wanted_amount} MP!")

        elif instructions == "Heal":
            wanted_amount = int(command[2])
            affordable_amount = 100 - hero_data_base[hero_name][0]

            if wanted_amount > affordable_amount:
                hero_data_base[hero_name][0] += affordable_amount
                print(f"{hero_name} healed for {affordable_amount} HP!")
            else:
                hero_data_base[hero_name][0] += wanted_amount
                print(f"{hero_name} healed for {wanted_amount} HP!")
    return hero_data_base


number_of_heroes = int(input())
hero_data_base = {}

data_base_generator(number_of_heroes, hero_data_base)
game_play(hero_data_base)
