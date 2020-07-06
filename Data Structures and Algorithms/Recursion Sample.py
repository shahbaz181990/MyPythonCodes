# A simple way to show how recursion works.

def fact(n):
    if n == 0:
        return 1
    smallOutput = fact(n-1)
    return n * smallOutput


def sum_n(n):
    if n == 0:
        return 0
    smallOutput = sum_n(n-1)
    output = sum_n(n-1) + n
    return output


#def func(n):
 #   return func(n-1)


n = int(input())
print(fact(n))
print(sum_n(n))
#print(func(n))