
# https://nus.kattis.com/problems/basicprogramming1

def f1(A,N):
    print(7)

def f2(A,N):
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")

def f3(A,N):
    print(sorted(A[0:3])[1])

def f4(A,N):
    print(sum(A))

def f5(A,N):
    print(sum(filter(lambda x: x%2 == 0, A)))

def f6(A,N):
    print("".join(list(map(lambda x: "abcdefghijklmnopqrstuvwxyz"[x%26], A))))

def f7(A,N):
    '''
    A set is used to keep track of visited nodes
    Lookup of "item in set" is faster than list
    '''
    visited = set()
    i = 0
    while True:
        i = A[i]
        if (i > (N-1)):
            print("Out")
            break
        elif (i == (N-1)):
            print("Done")
            break
        if i in visited:
            print("Cyclic")
            break
        visited.add(i)

action = {1:f1, 2:f2, 3:f3, 4:f4, 5:f5, 6:f6, 7:f7}

N, t = map(int, input().split())
A = list(map(int, input().split()))

action[t](A,N)


