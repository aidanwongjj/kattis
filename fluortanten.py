
# https://open.kattis.com/problems/fluortanten

def listhappiness(l):
    '''
    Edited function to calculate h of list's right half for first time only
    '''
    i = 2
    h = 0
    for a in l:
        h += i * a
        i += 1
    return h

n = int(input())
mylist = list(map(int, input().split()))
#print(mylist)

# Remove bjorn first
mylist.remove(0)

# then do O(n) pass to check where is Bjorn's optimal position
# Hint: use dynamic programming
'''
List is divided into two halves: before(left) and after(right) Bjorn
On each iteration, Bjorn moves right, displacing 1 person from right to left
Happiness of right half decreases by that person's current i * his a
Happiness of left half increases by that person's new i * his a
Take into account indices:
- since mylist doesn't include Bjorn, and
- happiness calculation is 1-indexed (front is 1, not 0)
'''
LRH = listhappiness(mylist) #"list right happiness"
LLH = 0 #"list left happiness"
happiness = LRH

for i in range(0,n-1):
    a = mylist[i]
    LRH -= (i+2) * a
    LLH += (i+1) * a 
    lh = LLH + LRH
    if lh > happiness:
        happiness = lh
    
print(happiness)
