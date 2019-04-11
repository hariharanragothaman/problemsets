import math

def reverse(x):
    limit = math.pow(2, 31)
    sign = [1,-1][x < 0]
    ll = sign * int(str(abs(x))[::-1])
    return ll if -(2**31)-1 < ll < 2**31 else 0

a = 1020300
rst = reverse(a)
print rst
