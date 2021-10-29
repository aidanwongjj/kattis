
# https://open.kattis.com/problems/snowflakes
# Aim: find length of the longest contiguous segment of unique snowflakes.

from collections import deque

def count_max_unique(n):
    uniques = set() # python set lookup ('in') has O(1) time [hash table]
    package = deque() # Use shifting window using deque
    max_len = 0

    for i in range(n):
        snowflake = int(input())
        if snowflake in uniques:
            # update max length
            max_len = max(max_len, len(package))
            # get rid of all previous snowflakes up to and including duplicate
            while True:
                old = package.popleft()
                if old != snowflake:
                    uniques.remove(old)
                else:
                    # gotten rid of old dupe
                    # add new dupe to end of deque to reflect new position
                    package.append(snowflake)
                    break
                
        else: #snowflake is new
            uniques.add(snowflake)
            package.append(snowflake)
    
    print(max(max_len, len(package))) #print final updated max value

num_cases = int(input()) 
for i in range(num_cases):
    count_max_unique(int(input()))
