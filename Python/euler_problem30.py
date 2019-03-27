import math

def check_num(num):
    sum = 0
    digits = [int(d) for d in str(num)]
    for dts in digits:
        sum = sum + math.pow(dts,5)
    if sum == num:
        return True
    return False

i = 1
result_sum = 0
while i < 1000000:
    if check_num(i):
        print "The number is:", i 
        result_sum += i 
    i += 1

print "The result sum is:", result_sum-1
