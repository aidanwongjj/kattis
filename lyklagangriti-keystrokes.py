
# https://nus.kattis.com/problems/lyklagangriti

from collections import deque

def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

myinput = input()
output = deque()

rotations = 0
for char in myinput:
    if not char.isupper():
        output.append(char)
    elif char == 'B':
        output.pop()
    elif char == 'L':
        output.rotate(1)
        rotations += 1
    else: # char == R
        output.rotate(-1)
        rotations -= 1

output.rotate(rotations * -1)
print("".join(output))


