"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

test_num = 600851475143

i = 2
largest_prime_factor = 0
factor_limit = test_num / 2

def check_prime(num):
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

# Improved method to find all factors

def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

factors = factors(test_num)
for i, e in reversed(list(enumerate(factors))):
    if check_prime(e):
        print "The highest prime factor is:", e
        break




