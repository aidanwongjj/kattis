
# https://nus.kattis.com/problems/annoyedcoworkers

import heapq

h, c = map(int, input().split())

'''
Strategy: Always annoy the least annoyed coworker
-Store coworkers in (min) heap
-Find which coworker to irritate by popping from min heap
-After adding irritation val, push back onto heap
-Return largest value in heap for max irritation
'''

myheap = []

# Read in coworkers
for i in range(c):
    a, d = map(int, input().split())
    pot = a + d # potential annoyance val (a on next ask for help) 
    heapq.heappush(myheap, tuple([pot, a, d]))

# Ask for help h times
for i in range(h):
    worker = heapq.heappop(myheap)
    # update values
    ## annoyance (taken from potential)
    new_a = worker[0]
    ## potential (new + d)
    d = worker[2] # d is unchanged, new variable for clarity
    new_pot = new_a + d
    # Push back updated values
    heapq.heappush(myheap, tuple([new_pot, new_a, d]))
    
# Return largest irritation
print(max(myheap, key=lambda x: x[1])[1])


