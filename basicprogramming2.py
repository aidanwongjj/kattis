
# https://nus.kattis.com/problems/basicprogramming2

def f1(A,N):
    # Print "Yes" if there are two integers x∈A and y∈A
    # such that x+y=7777, "No" otherwise
    numDict = {}
    for i in range(N):
        numDict[7777 - A[i]] = (i, A[i])
    
    for i in range(N):    
        if numDict.get(A[i]) is not None:
            secondNumIndex = numDict.get(A[i])[0]
            if i != secondNumIndex:
                print("Yes")
                return
    print("No")
    

def f2(A,N):
    # Print "Unique" if all ints in A differnt
    # "Contains duplicate" otherwise
    if len(set(A)) == N:
        print("Unique")
    else:
        print("Contains duplicate")

def f3(A,N):
    '''
    Print int that appears > N/2 times in A
    Print -1 if none exists
    '''
    # list.count() is O(n) time
    A.sort()
    if A.count(A[N//2]) > N//2:
        print(A[N//2])
    else:
        print(-1)

def f4(A,N):
    A.sort()
    mystr = str(A[N//2])
    if (N % 2 == 0):
        print(str(A[N//2 - 1]) + " " + mystr)
    else:
        print(mystr)

def f5(A,N):
    '''
    Print integers in A that fall between a range [100…999] in sorted order;
    (print a single space between two integers)
    '''
    #python sort is O(nlogn) [timsort]
    mylist = []
    for num in A:
        if num >= 100 and num <= 999:
            mylist.append(num)
    mylist.sort()
    print(" ".join(str(elem) for elem in mylist))


action = {1:f1, 2:f2, 3:f3, 4:f4, 5:f5}

N, t = map(int, input().split())
A = list(map(int, input().split()))

action[t](A,N)
