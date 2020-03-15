"""
Whatte a legendary peice of code

"""
def generateMatrix(n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n*n):
        A[i][j] = k + 1
        
        print((i+di)%n, (j+dj)%n)

        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A


res = generateMatrix(3)

print(" ".join([str(row) for row in res]))
