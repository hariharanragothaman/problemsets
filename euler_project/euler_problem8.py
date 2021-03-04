"""
Find largest adjacent product in a number
"""

num = "123456789345678"

# When modifying strings - Remember list comprehensions
# it generates a list
result = [int(i) for i in num]
print result


# Create a new list from exisiting list
from itertools import zip

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip(*args)
