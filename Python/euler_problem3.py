"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

#test_num = 600851475143
test_num = 13195

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

# Find all factors

while factor_limit > 2:
    if test_num % factor_limit == 0:
        print "The factor is:", factor_limit
        result = check_prime(factor_limit)
        if result:
            largest_prime_factor = factor_limit
            break
        else:
            print "Searching for other factors..."

    factor_limit = factor_limit-1

print "The largest prime factor is:", largest_prime_factor
