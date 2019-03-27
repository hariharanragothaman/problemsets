"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.abs
"""

limit = 2000000
num = 2
sum = 0

def is_prime1(num):
    i = 2
    while i < (num-1):
        if num % i == 0:
            return False
        i = i+1
    return True

# Optimized algorithm
def is_prime2(num):
    if num <=1:
        return False
    if num <=3:
        return True
    if num%2==0 or num%3==0:
        return False

    i = 5
    while num >= (i*i):
        if num%i == 0 or num%(i+2) == 0:
            return False
        i += 6
    return True

while num < limit:
    flag = is_prime1(num)
    if flag:
        sum += num 
    print "The num is: {} and flag is {}".format(num, flag)
    num += 1

print "The final sum is:", sum
