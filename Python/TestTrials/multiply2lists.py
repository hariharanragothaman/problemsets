#a = [1, 2, 3, 4]
#b = [7, 8, 9, 5]

input_string = input()
ll = input_string.split('|')
print(ll)
a = ll[0].split(' ')
b = ll[1].split(' ')
print(a)
print(b)
a = [ int(c) for c in a if c]
b = [ int(c) for c in b if c]
print(a)
print(b)
result = [int(a)*int(b) for a,b in zip(a,b)]
print(result)