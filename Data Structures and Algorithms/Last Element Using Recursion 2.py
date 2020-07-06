def lastElementinArray(arr, x, si):
    l = len(arr)
    if si == l:
        return -1
    op = lastElementinArray(arr, x, si + 1)
    if op != -1:
        return op
    else:
        if arr[si] == x:
            return si
        else:
            return -1


arr = list(map(int, input().split()))
x = int(input())
print(lastElementinArray(arr, x, 0))
