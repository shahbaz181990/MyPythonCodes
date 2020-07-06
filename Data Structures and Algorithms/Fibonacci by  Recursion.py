def fibo(n):
    if n == 1 or n == 2:
        return 1
    n = fibo(n-1) + fibo(n-2)
    return n


def fun(n):
    if n == 4:
        return n
    else:
        return 2 * (fun(n+1))


n = int(input())
print(fibo(n))
print(fun(n))

