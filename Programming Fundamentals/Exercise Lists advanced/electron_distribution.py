number_of_electrons = int(input())
shells = []

for atom_shell_number in range(1, number_of_electrons):
    shell_capacity = 2 * atom_shell_number ** 2
    current_shell = 0
    if number_of_electrons >= shell_capacity:
        number_of_electrons -= shell_capacity
        current_shell = shell_capacity
        shells.append(current_shell)
    else:
        current_shell = number_of_electrons
        shells.append(current_shell)
        break

print(shells)
