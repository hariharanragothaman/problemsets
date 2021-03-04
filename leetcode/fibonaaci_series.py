def fibonacci(n):
    first = 0
    second = 1

    print(first)
    print(second)

    n = 0
    while n < 50:
        third = first + second 
        print(third)
        first = second
        second = third
        n += 1

fibonacci(20)
