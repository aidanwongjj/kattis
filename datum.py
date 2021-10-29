
# https://open.kattis.com/problems/datum

"""
Write a program that, given a date in 2009, determines the day of week
on that date.
"""
# Use Rata Die method
# https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Rata_Die

date = input()
day, month = int(date.split()[0]), int(date.split()[1])

daysPast = -1
monthDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
             7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

# find days since Jan 1
for m in range(1, month):
    daysPast += monthDays[m]
daysPast += day

# find day of the week
# 0 is encoded as Thursday since 1st Jan is a Thursday
rataDie = {0:"Thursday", 1:"Friday", 2:"Saturday", 3:"Sunday",
           4:"Monday", 5:"Tuesday", 6:"Wednesday"}

print(rataDie[daysPast % 7])

#print(f"day is {day}, month is {month}")
#print(f"{daysPast} days since Jan 1")
