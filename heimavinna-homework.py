
# https://open.kattis.com/problems/heimavinna

# Non-DAT (direct addressing table) approach

problem_list = list(input().split(';'))

num_problems = 0

for elem in problem_list:
    if '-' in elem:
        p1, p2 = map(int, elem.split('-'))
        num_problems += p2 - p1 + 1
    else:
        num_problems += 1

print(num_problems)
