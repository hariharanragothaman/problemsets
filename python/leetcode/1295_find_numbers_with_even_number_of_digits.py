"""
@brief: Find numbers with even number of digits
"""

nums = [12, 345, 2, 6, 7896]
result = 0 

for elements in nums:
    element_digits = [ d for d in str(elements)]
    if len(element_digits)%2 == 0:
        result += 1
print (result)
