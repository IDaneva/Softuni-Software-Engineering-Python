def generate_music_data_base(music_dict, number_of_pieces):
    for _ in range(number_of_pieces):
        piece_name, composer_name, key = input().split("|")
        music_dict[piece_name] = [composer_name, key]


def things_to_do_with_info(music_dict):
    while True:
        command = input()
        if command == "Stop":
            for key, value in music_dict.items():
                print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
            break
        command = command.split("|")
        instructions = command[0]
        if instructions == "Add":
            piece_name = command[1]
            composer_name = command[2]
            key = command[3]
            if piece_name not in music_dict:
                music_dict[piece_name] = [composer_name, key]
                print(f"{piece_name} by {composer_name} in {key} added to the collection!")
            else:
                print(f"{piece_name} is already in the collection!")
        elif instructions == "Remove":
            piece_name = command[1]
            if piece_name in music_dict:
                del music_dict[piece_name]
                print(f"Successfully removed {piece_name}!")
            else:
                print(f"Invalid operation! {piece_name} does not exist in the collection.")
        elif instructions == "ChangeKey":
            piece_name = command[1]
            new_key = command[2]
            if piece_name in music_dict:
                music_dict[piece_name][1] = new_key
                print(f"Changed the key of {piece_name} to {new_key}!")
            else:
                print(f"Invalid operation! {piece_name} does not exist in the collection.")


number_of_pieces = int(input())
music_dict = {}
generate_music_data_base(music_dict, number_of_pieces)
things_to_do_with_info(music_dict)
