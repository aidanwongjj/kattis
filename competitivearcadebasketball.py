
# https://nus.kattis.com/problems/competitivearcadebasketball

num_participants, points_required, num_rounds = map(int, input().split())

dict_p = {}
for i in range(num_participants):
    dict_p[input()] = 0

for i in range(num_rounds):
    temp = input().split()
    dict_p[temp[0]] += int(temp[1])

outputstr = ""
for person, score in dict_p.items():
    if score >= points_required:
        outputstr += f"{person} wins!\n"

if not outputstr:
    outputstr += "No winner!"

print(outputstr.rstrip())
