import calendar

# week header in 3 letters
print(calendar.weekheader(3))

# monday is 0
print(calendar.firstweekday())

# print the whole month
print(calendar.month(2019, 3))

# print the whole month with the array of the week
print(calendar.monthcalendar(2019, 3))

# print the year
print(calendar.calendar(2021))

# print of the day of the week
day_of_the_week = calendar.weekday(2021, 4, 8)
print(day_of_the_week)

#print if the year is a leap year or not.
is_leap = calendar.isleap(2022)
print(is_leap)

# print leap days
how_many_leap_days = calendar.leapdays(2020,2022)
print(how_many_leap_days)