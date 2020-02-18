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

def remove_duplicates_new(nums):

    """
    Parse through the array
    Maintain a slow pointer

    with fast pointer - when elements are not equal
    move it to the slow pointers next location
    Increment slow pointer

    A[0---<slow-pointer] is the sub-list we need
    """
    j = 1
    if len(nums) == 0: return 0


    print "The initial value of A is", A

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j +=1
            print "The value of A is", A

    del nums[j:len(nums)]
    return A

A = [0,0,1,1,1,2,2,3,3,4]

rst = remove_duplicates_new(A)
print rst
