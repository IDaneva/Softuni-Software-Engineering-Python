competitor_1 = int(input())
competitor_2 = int(input())
competitor_3 = int(input())

overall_time = competitor_1 + competitor_2 + competitor_3

minutes = overall_time // 60
seconds = overall_time % 60

print(f"{minutes}:{seconds:02d}")
