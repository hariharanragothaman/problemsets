"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44
    As 1 = 14 is not a sum it is not included.abs
    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

import math

def check_num(num):
    sum = 0
    # This is the crux logic - line
    digits = [int(d) for d in str(num)]
    for dts in digits:
        sum = sum + math.pow(dts,5)
    if sum == num:
        return True
    return False

i = 1
result_sum = 0
while i < 1000000:
    if check_num(i):
        print "The number is:", i 
        result_sum += i 
    i += 1

print "The result sum is:", result_sum-1
