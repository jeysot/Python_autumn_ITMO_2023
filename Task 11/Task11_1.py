import calendar

def free_dates(year):
    free_days = []
    for month in range(1, 13):
        first_day_of_month = calendar.weekday(year, month, 1)
        if first_day_of_month == 3:
            third_thursday = 15
        elif first_day_of_month < 3:
            third_thursday = 15 + (3 - first_day_of_month)
        else:
            third_thursday = 15 + (10 - first_day_of_month)
        free_days.append((year, month, third_thursday))
    return free_days

free_museum_days_2023 = free_dates(2023)

for year, month, day in free_museum_days_2023:
    print(f"{day:02d}-{month:02d}-{year}")
