import itertools as it

"""
this
is
git
check
Hello World
"""

"""
Built in functions-learning
"""
# Zip Function
# Note: zip returns a tuple

temp_list = ['$', '%', '@']
num_list = [1, 2, 3]
string_list = ['a', 'b', 'c']
print list(zip(num_list, string_list, temp_list))

# Map function

string_list = ['abcd', 'bde', 'carwrt']
length_list = map(len, string_list)
print "The initial string list", string_list
print "The length of each string", length_list

# For example if we want a sum of 2 list or a product of 2 list

n_list = [2, 3, 4, 5, 6]
t_list = [1, 2, 7 , 3, 2]

print "The first list is:", n_list
print "The second list is:", t_list
print "The sum of 2 lists", map(sum, zip(n_list, t_list))


"""
Given a list of values inputs and a positive integer n, write a function that splits inputs into groups of length n. 
For simplicity, assume that the length of the input list is divisible by n. 
For example, if inputs = [1, 2, 3, 4, 5, 6] and n = 2, your function should return [(1, 2), (3, 4), (5, 6)].
"""

n = 2
nums =  [1, 2, 3, 4, 5, 6]
print "The initial list is:", nums
print [nums[i] for i in range(len(nums))]

# Remember the iter stuff  - Super cool to generate multiple iterators
def better_grouper(nums, n):
    iters = [iter(nums)]*n
    return zip(*iters)

result = better_grouper(nums, n)
print result


# Generate even (or) odd numbers
def gen_even():
    n = 0 
    while True:
        yield n
        n += 2
 
evens  = gen_even()
print list(next(evens) for _ in range(5))

# using itertools to do the same thing
counter  = it.count(start = 4, step=2)
print list(next(counter) for _ in range(5))

"""
Generate a fibonacci sequence
"""

def fib():
    a,b = 0, 1
    while True:
        yield a
        a, b = b, a+b
f = fib()
#print the first 5 digits of a fibonaaci sequence
print list(next(f) for _ in range(100))

# Convert list to string

n1 = [4, 5, 6]
n2 = [4, 5, 6]
string_n1 = ['1', '2', '3']

print n1
print string_n1

print ''.join(string_n1)
# To use join -  we have to typecast
print ''.join(str(i) for i in n1)
