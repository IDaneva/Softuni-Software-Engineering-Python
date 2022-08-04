hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

total_exam_minutes = hour_of_exam * 60 + minutes_of_exam

total_arrival_minutes = hour_of_arrival * 60 + minutes_of_arrival

diff = abs(total_arrival_minutes - total_exam_minutes)
hours = diff // 60
minutes = diff % 60

if total_exam_minutes == total_arrival_minutes:
    print("On time")

elif total_arrival_minutes < total_exam_minutes:
    if diff > 59:
        print("Early")
        print(f"{hours}:{minutes:02d} hours before the start")
    elif diff > 30 and diff <= 59:
        print("Early")
        print(f"{minutes} minutes before the start")
    else:
        print("On time")
        print(f"{minutes} minutes before the start")
elif total_arrival_minutes > total_exam_minutes:
    if diff > 59:
        print("Late")
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print("Late")
        print(f"{minutes} minutes after the start")
