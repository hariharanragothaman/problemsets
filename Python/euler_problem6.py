import math

def sum_of_squares(n):
    return n*(n+1)*(2*n+1)/6

def square_of_sum(limit):
    result = limit*(limit+1)/2
    return math.pow(result, 2)

n = 100
result = square_of_sum(n)
result2 = sum_of_squares(n)
print result - result2
