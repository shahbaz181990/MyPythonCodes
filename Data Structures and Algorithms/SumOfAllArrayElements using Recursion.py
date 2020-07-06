def sumArray(arr):
    n = len(arr)
    sum = 0
    if n == 0:
        return 0
    b = arr[1:]
    sum += sumArray(b)
    return sum + arr[0]

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
