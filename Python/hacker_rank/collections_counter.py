
from collections import Counter

"""

ll = [1,1, 2, 5, 6, 4, 2,3,4,5]
c = Counter(ll)
print c
print c.items()
print c.keys()
print c.values()

"""
"""
stock_num = int(raw_input("Enter the number of shoes"))
l_stock = []
while stock_num > 0:
    s = raw_input("Enter the size")
    l_stock.append(s)
    stock_num -= 1

print "The stock available is:", l_stock

# To accept tuple as I/P
"""

size_cost = tuple(int(x.strip()) for x in raw_input().split(' '))




"""
c = Counter(ll)
print "The stock tags are", c
shoes_to_purchase  = raw_input("How many number of shoes to be purchased?")
# To collect shoe-size and cost?
"""
