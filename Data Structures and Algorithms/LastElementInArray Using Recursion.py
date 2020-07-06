def lastElementinArray(arr, x):
    l = len(arr)
    if l == 0:
        return -1

    b = arr[1:]
    op = lastElementinArray(b, x)
    if op != -1:
        return op + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1

arr = list(map(int, input().split()))
x = int(input())
print(lastElementinArray(arr, x))
