
# https://open.kattis.com/problems/grandpabernie
# Using defaultdict
from collections import defaultdict

num_trips = int(input())
trips = defaultdict(lambda: [])

for i in range(num_trips): # O(n)
    country, year = input().split() #O(1)
    trips[country].append(int(year)) #O(1)

for country in trips.keys():
    # If alpha is the chain length
    # O(alpha log alpha) per chain (multiply by n)
    # alpha is small
    trips[country].sort()

num_queries = int(input())
for i in range(num_queries):
    country, instance = input().split()
    print(trips[country][int(instance) - 1])
