import math

movie_name = input()
episode_length = int(input())
break_length = int(input())

time_for_eating = break_length * 1/8
time_for_rest = break_length * 1/4

left_time = break_length - time_for_eating - time_for_rest
diff = abs(left_time - episode_length)

if left_time >= episode_length:
    print(f"You have enough time to watch {movie_name} and left with {math.ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {math.ceil(diff)} more minutes.")
