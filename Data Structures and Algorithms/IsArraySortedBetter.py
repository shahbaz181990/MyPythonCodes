def isArraySorted(arr, si):
    n = len(arr)
    if si == n-1 or si == n:
        return True
    if arr[si] > arr[si+1]:
        return False
    isArray = isArraySorted(arr, si + 1)
    return isArray


arr = list(map(int, input().split()))
si = 0
print(isArraySorted(arr, 0))