
# https://nus.kattis.com/problems/ofugsnuid

n = int(input())
mylist = []

for i in range(n):
    mylist.append(input())

for i in range(n):
    print(mylist.pop())
