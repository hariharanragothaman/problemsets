"""
Find the index of the fibonaaci term that has 1000 digits
"""

# 3,5,8,13

first_term = 1
second_term = 1
third_term = 0

count = 2 # Since the first generated one will be the 3rd term

while True:
    third_term = second_term + first_term
    first_term = second_term
    second_term = third_term
    count = count + 1

    print "The third term is", third_term

    if len(str(third_term)) == 1000:
        print "The index count is", count
        break
