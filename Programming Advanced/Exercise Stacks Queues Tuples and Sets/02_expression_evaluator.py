from collections import deque

expression = input().split()
evaluator = deque()


for ch in expression:
    if ch in ["*", "+", "-", "/"] and len(evaluator) > 0:
        current = 0
        if ch == "*":
            while len(evaluator) > 1:
                current = evaluator.popleft() * evaluator.popleft()
                evaluator.append(current)

        elif ch == "+":
            while len(evaluator) > 1:
                current = evaluator.popleft() + evaluator.popleft()
                evaluator.append(current)
        elif ch == "-":
            while len(evaluator) > 1:
                current = evaluator.popleft() - evaluator.popleft()
                evaluator.appendleft(current)
        elif ch == "/":
            while len(evaluator) > 1:
                current = evaluator.popleft() // evaluator.popleft()
                evaluator.appendleft(current)
    else:
        evaluator.append(int(ch))

print(*evaluator, sep="")
