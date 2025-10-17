def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    # Days in each month
    month_days = [31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]

def days_from_start(d, m, y):
    # Count days from start of year to given date
    days = d
    for i in range(1, m):
        days += days_in_month(i, y)
    return days

def days_between(d1, d2):
    day1, month1, year1 = d1
    day2, month2, year2 = d2

    # Make sure date1 is earlier
    if (year1, month1, day1) > (year2, month2, day2):
        day1, month1, year1, day2, month2, year2 = day2, month2, year2, day1, month1, year1

    total_days = 0

    # Add full years between
    for y in range(year1, year2):
        total_days += 366 if is_leap(y) else 365

    # Subtract extra days after d2’s month/day in final year
    total_days += days_from_start(day2, month2, year2)
    total_days -= days_from_start(day1, month1, year1)

    return abs(total_days)

# Example
d1 = (1, 1, 2024)
d2 = (17, 10, 2025)

#print("Number of days between:", days_between(d1, d2))
print(is_leap(2016))
