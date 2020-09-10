
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

result = fact(100)
print (result)

digits = [x for x in str(result)]
print (digits)

result_sum = 0
for i, e in list(enumerate(digits)):
    result_sum += int(e)

print result_sum
