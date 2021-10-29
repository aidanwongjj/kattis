
# https://open.kattis.com/problems/numbertree

myinput = input().split()
h = int(myinput[0])
if len(myinput) > 1:
    path = myinput[1]
else:
    path = ""
    
start = 1

for char in path:
    if char == 'L':
        start = start*2
    else: # if char == 'R'
        start = start*2 + 1

print((2**(h+1)) - start)
