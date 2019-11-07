import collections

"""
The easy and straightforward solution
"""
def intersect(A,B):
    ctr = collections.Counter(A)
    res = []

    for nums in B:
        if ctr[nums] >= 0:
            res += nums, 
            ctr[nums] -= 1
    return res


"""
There are scenario's to consider when the array is sorted and so on...
"""
