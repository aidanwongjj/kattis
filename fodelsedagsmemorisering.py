
#https://open.kattis.com/problems/fodelsedagsmemorisering
# birthday memorization

birthdays = {}

n = int(input())

for i in range(n):
    name, liking, date = input().split()
    liking = int(liking)
    if date not in birthdays.keys():
        birthdays[date] = (name, liking)
    else:
        if birthdays[date][1] < liking:
            birthdays[date] = (name, liking)

remembered_list = sorted([x[0] for x in birthdays.values()])

print(len(remembered_list))
for name in remembered_list:
    print(name)
