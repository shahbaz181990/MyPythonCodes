# Function to Print Numbers from 1 to n
def natural_1_to_n(n):
    if n == 0:
        return ''
    print(natural_1_to_n(n-1))
    print(n)
    return ''

def natural_n_to_1(n):
    if n == 0:
        return ''
    print(n)
    print(natural_n_to_1(n-1))
    return ''


n = int(input())
print(natural_1_to_n(n))
print(natural_n_to_1(n))