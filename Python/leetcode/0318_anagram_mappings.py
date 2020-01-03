"""
Problem 318: Anagram Mappings

Given 2 anagrams - find the index mappings.
For example, given
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
We should return  [1, 4, 3, 2, 0]
"""

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
result = []

A_dict = {}
B_dict = {}

for i, element in list(enumerate(A)):
    A_dict[element] = i 
for i, element in list(enumerate(B)):
    B_dict[element] = i

for key, value in B_dict.items():
    if key in A_dict:
        result.append(B_dict[key])

#### - Note: The above logic is a hashmap implementation; and it fails for duplicates. DAMN!
#### Improved Logic


P = []
for element in A:
    P.append(B.index(i))
print(P)
