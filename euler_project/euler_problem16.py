import math

result = math.pow(2,1000)
result = int(result)
result = str(result)

print result
ll = [x for x in result]
print ll

result_sum = 0 

for i, e in list(enumerate(result)):
    result_sum += int(e)

print "The result is:", result_sum
