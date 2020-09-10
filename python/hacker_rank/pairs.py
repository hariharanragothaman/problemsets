a = [1, 2, 3, 4, 5, 7, 3, 2, 8,]
k = 1
print (set(a))
print (set(x+k for x in a))
print (set(a) & set(x+k for x in a))
