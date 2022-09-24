import math

time_for_action = int(input())
number_of_scenes = int(input())
length_of_scene = int(input())

preparation_time = time_for_action * 0.15

time_for_scenes = number_of_scenes * length_of_scene

total_needed_time = preparation_time + time_for_scenes

diff = math.ceil(abs(time_for_action - total_needed_time))

if total_needed_time >= time_for_action:
    print(f"Time is up! To complete the movie you need {diff} minutes.")

else:
    print(f"You managed to finish the movie on time! You have {diff} minutes left!")