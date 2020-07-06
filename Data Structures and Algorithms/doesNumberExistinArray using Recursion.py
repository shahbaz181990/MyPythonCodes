def checkNumber(arr, x):
    # Please add your code here
    n = len(arr)
    if n == 0:
        return 0
    if x == arr[0]:
        return "true"
    b = arr[1:]
    isNumAvail = checkNumber(b, x)
    if isNumAvail:
        return True


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
