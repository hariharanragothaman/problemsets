import math

def reverse(x):
    limit = math.pow(2, 31)
    sign = [-1,1][x<0]
    ll = sign * int(str(abs(x))[::-1])
    return ll
