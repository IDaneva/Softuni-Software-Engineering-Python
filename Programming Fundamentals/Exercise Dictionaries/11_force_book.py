force_dict = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    present = False

    if "|" in command:
        force_side, force_user = command.split(" | ")
        for value in force_dict.values():
            if force_user in value:
                present = True
        if not present:
            if force_side not in force_dict:
                force_dict[force_side] = [force_user]
            else:
                force_dict[force_side].append(force_user)

    else:
        force_user, force_side = command.split(" -> ")
        for key, value in force_dict.items():
            if force_user in value:
                force_dict[key].pop(value.index(force_user))
                break

        if force_side not in force_dict:
            force_dict[force_side] = [force_user]
        else:
            force_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")


print(force_dict)
for k, v in force_dict.items():
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        for s in v:
            print(f"! {s}")