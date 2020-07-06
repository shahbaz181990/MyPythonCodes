def isListSorted(li):
    n = len(li)-1
    if len(li) == 0 or len(li) == 1:
        return True

    if li[0] > li[1]:
        return False

    b = li[1:]
    issmallerListSorted = isListSorted(b)
    if issmallerListSorted:
        return True
    else:
        return False


li = list(map(int, input().split()))
print(isListSorted(li))
