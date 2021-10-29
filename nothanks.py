
# https://nus.kattis.com/problems/nothanks

n = int(input())
l = [int(x) for x in input().split()]
l.sort()

expect = None
total = 0
for num in l:
    if num == expect or num is None:
        pass
    else:
        total += num
    expect = num + 1

print(total)
        

        
        
        

