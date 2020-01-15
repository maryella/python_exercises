# 4. Day of the Week
day = int(input('Day (0-6)? '))
if day == 0:
    dayname = "Sunday"
elif day == 1:
    dayname = "Monday"
elif day == 2:
    dayname = "Tuesday"
elif day == 3:
    dayname = "Wednesday"
elif day == 4:
    dayname = "Thursday"
elif day == 5:
    dayname = "Friday"
elif day == 6:
    dayname = "Saturday"
else:
    dayname = "not an option! (Gotta choose 0 through 6)"

print(str(day) + " = " + dayname)
