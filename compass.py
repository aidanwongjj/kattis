
#https://nus.kattis.com/problems/compass

def findChange(curPos, truePos):
    diff = abs(curPos - truePos)
    if diff == 180:
        print(diff)
        return

    ans = min(diff, 360 - diff) 
    ans = ans if (curPos + ans == truePos or curPos + ans == truePos + 360) else -ans
    print(ans)
    

findChange(int(input()), int(input()))

