spell_to_decipher = input()

while True:
    command = input()
    if command == "Abracadabra":
        break
    command = command.split()
    instructions = command[0]
    if instructions == "Abjuration":
        spell_to_decipher = spell_to_decipher.upper()
        print(spell_to_decipher)

    elif instructions == "Necromancy":
        spell_to_decipher = spell_to_decipher.lower()
        print(spell_to_decipher)

    elif instructions == "Illusion":
        index = int(command[1])
        letter = command[2]
        if 0 <= index < len(spell_to_decipher):
            spell_to_decipher = spell_to_decipher[:index] + letter + spell_to_decipher[index+1:]
            print("Done!")
        else:
            print("The spell was too weak.")

    elif instructions == "Divination":
        first_sub = command[1]
        second_sub = command[2]
        if first_sub in spell_to_decipher:
            spell_to_decipher = spell_to_decipher.replace(first_sub, second_sub)
            print(spell_to_decipher)
        else:
            continue

    elif instructions == "Alteration":
        sub = command[1]
        if sub in spell_to_decipher:
            spell_to_decipher = spell_to_decipher.replace(sub, "")
            print(spell_to_decipher)
        else:
            continue

    else:
        print("The spell di not work!")