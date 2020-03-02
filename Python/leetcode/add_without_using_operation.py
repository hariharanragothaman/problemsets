a = 5
b = 3

def add(a, b):
    while a > 0:
        a -= 1
        b += 1
    
    while a < 0:
        a += 1
        b -= 1
    
    return b

result = add(5, 3)
print(result)
