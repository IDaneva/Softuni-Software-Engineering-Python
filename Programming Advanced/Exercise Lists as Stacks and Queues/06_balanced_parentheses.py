sequence = input()
parentheses_stack = []

balanced = None
for ch in sequence:
    if ch in "({[":
        parentheses_stack.append(ch)
    else:
        balanced = False
        if len(parentheses_stack) > 0 and f'{parentheses_stack[-1]}{ch}' in '{}[]()':
            balanced = True
            parentheses_stack.pop()
        else:
            balanced = False

if balanced:
    print("YES")
else:
    print("NO")
