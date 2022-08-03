hours = int(input())
minutes = int(input())

minutes_in_15 = (hours * 60) + minutes + 15

hours_now = minutes_in_15 // 60
minutes_now = minutes_in_15 % 60

if hours_now > 23:
    hours_now = 0

print(f"{hours_now}:{minutes_now:02d}")
