def removeDuplicates(A):
    """
    :type A: List[int]
    :rtype: int
    """
    print "The initial value of A is:", A
    if len(A) == 0:
        return 0 

    i = 0 
    while i < len(A)-1:
        if A[i] == A[i+1]:
            del A[i]
        else:
            i += 1

    return A

A = [0,0,1,1,1,2,2,3,3,4]

rst = removeDuplicates(A)
print rst
