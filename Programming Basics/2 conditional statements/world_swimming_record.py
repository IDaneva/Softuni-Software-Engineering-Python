world_record = float(input())
distance = float(input())
time_for_1_meter = float(input())

seconds_for_competeter = distance * time_for_1_meter
water_resistance = int(distance / 15)
water_resistance_time = water_resistance * 12.5

overall_time = seconds_for_competeter + water_resistance_time
diff = abs(world_record - overall_time)


if overall_time < world_record:
    print(f"Yes, he succeeded! The new world record is {overall_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
