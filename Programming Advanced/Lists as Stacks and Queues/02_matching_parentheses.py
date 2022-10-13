math_equation = input()

found_parentheses_idx = []

for index in range(len(math_equation)):
    if math_equation[index] == "(":
        found_parentheses_idx.append(index)

    elif math_equation[index] == ")":
        print(math_equation[found_parentheses_idx[-1]:index+1])
        found_parentheses_idx.pop()
