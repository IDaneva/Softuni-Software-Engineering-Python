from collections import deque

players = deque(input().split(", "))
rows = 6

maze_board = [input().split() for _ in range(rows)]

resting_dict = {players[0]: False, players[1]: False}

while True:
    coordinates = input().replace("(", '').replace(")", "").split(", ")
    current_player = players.popleft()
    if not resting_dict[current_player]:
        row = int(coordinates[0])
        col = int(coordinates[1])
        if maze_board[row][col] == "E":
            print(f"{current_player} found the Exit and wins the game!")
            break
        elif maze_board[row][col] == "T":
            print(f"{current_player} is out of the game! The winner is {players.pop()}.")
            break
        elif maze_board[row][col] == "W":
            print(f"{current_player} hits a wall and needs to rest.")
            resting_dict[current_player] = True
            players.append(current_player)
            continue
        else:
            players.append(current_player)
    else:
        players.append(current_player)
        resting_dict[current_player] = False
