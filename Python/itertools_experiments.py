"""
Built in functions-learning
"""
# Zip Function

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

