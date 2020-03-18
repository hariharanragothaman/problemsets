from math import ceil

def theatre_square(n, m, a):
    A = ceil(n/a)
    B = ceil(m/a)
    return int(A*B)

if __name__ == '__main__':
    res = theatre_square(6, 6, 4)
    print(res)