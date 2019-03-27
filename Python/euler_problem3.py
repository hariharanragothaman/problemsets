"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

test_num = 600851475143

#test_num = 13195
i = 2
largest_prime_factor = 0
factor_limit = test_num / 2


def check_prime(num):
    i = 2
    flag = True
    flimit = num/2

    while flimit > i:
        if num % flimit == 0:
            flag = False
            break
        else:
            flag=True
        flimit = flimit - 1

    if flag:
        print "This factor is a prime number"
        return num
    else:
        print "This factor is not a prime number"
        return False


while factor_limit > 2:
    if test_num % factor_limit == 0:
        print "The factor is:", factor_limit
        print "Checking if the factor is prime..."
        result = check_prime(factor_limit)
        if result:
            largest_prime_factor = result
            break
        else:
            print "Searching for other factors..."

    factor_limit = factor_limit-1

print "The largest prime factor is:", largest_prime_factor
