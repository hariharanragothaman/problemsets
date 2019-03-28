"""
Built in functions-learning
"""
from itertools import zip_longest


# Zip Function

num_list = [1, 2, 3]
string_list = ['a', 'b', 'c']
print list(zip(num_list, string_list))


num_list = [1, 2, 3, 4, 5]
string_list = ['a', 'b', 'c']
print list(zip_longest(num_list, string_list))



# Map function


