"""
Function to do binary search
"""

def bsearch(t: int, A) -> int:
    L, U = 0 , len(A) - 1 # Getting the lower and upper index
    while L <= U:
        M = L + (U-L) // 2
        if A[M] < t:
            L = M+1
        elif A[M] == t:
            return M
        else:
            U = M-1
    return -1

if __name__ == '__main__':
    t = 7
    A = [1,2,3,4,5,6,7,8,9,10]
    result = bsearch(t, A)
    print (result)
