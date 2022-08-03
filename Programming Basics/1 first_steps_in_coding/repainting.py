nailon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_for_the_job = int(input())

nailon_price = 1.50
paint_price = 14.50
thinner_price = 5
bags = 0.40

sum_nailon = nailon_price * (nailon_needed + 2)
sum_paint = paint_price * (paint_needed+(paint_needed * 0.1))
sum_thinner = thinner_price * thinner_needed

total_sum_materials = sum_nailon + sum_paint + sum_thinner + bags
human_factor = (total_sum_materials * 0.3) * hours_for_the_job

total_everything = total_sum_materials + human_factor
print(total_everything)
