# The array always has unique numbers

num = [9, 4, 3, 1, 7, 12]
num.sort() # Sort the Array
print num

result = []
rst = []


i = 0
for i in range(len(num)):
    j = 0
    while j < len(num) and i!=j :
        total = num[i] + num[j]
        if total not in result:
            result.append(total)
        if total in result:
            t_ple = (num[i], num[j])
            rst.append(t_ple)
        j += 1
    i += 1

print result

print rst
