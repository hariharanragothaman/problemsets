"""
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a prime below one-hundred.abs
    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

limit = 1000000
num = 2
sum = 0

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

ll = []

while num < limit:
    flag = is_prime2(num)
    if flag:
        sum += num
        if is_prime2(sum):
            print "The prime sum is:", sum
            if sum < limit:
                ll.append(sum)
    num += 1

print "The num we need is:",ll[-1]
