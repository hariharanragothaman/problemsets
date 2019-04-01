
# Function to get all factors
def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

# Function to generate triangluar numbers


limit = 100000
num = 1

while num < limit:
    t_num = (num*(num+1)) / 2
    print "The number is:", num
    print "The T-number is:", t_num
    num_factors = factors(t_num)
    print "The number of factors is:", len(num_factors)
    if len(num_factors) > 500:
        print "******** WE FOUND IT ***********"
        print "The t-number is:", t_num
        break
    num = num+1

"""
num = 28
factor = factors(num)
print factor
print len(factor)
"""
