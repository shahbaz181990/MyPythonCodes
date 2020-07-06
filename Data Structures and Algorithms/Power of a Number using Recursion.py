def pow_of_num(x, n):
    if n == 0:
        return 1
    return x * pow_of_num(x, (n-1))


x, n = map(int, input().split())


print(pow_of_num(x, n))
