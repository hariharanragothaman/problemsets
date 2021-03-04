
s = []
n = 15
i = 1

while i<=n:
    if i == 1: s.append(i)
    elif i%3 == 0 and i%5 == 0: s.append("FizzBuzz")
    elif i%3 == 0: s.append("Fizz")
    elif i%5 == 0: s.append("Buzz")
    else: s.append(i)
    i += 1
print s
