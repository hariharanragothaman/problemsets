def singleNonDuplicate(num):
    """
    :type nums: List[int]
    :rtype: int
    """
    dict1 = {}
    for i in range(len(num)):
        if num[i] not in dict1:
            dict1[num[i]] = 1
        else:
            dict1[num[i]] += 1
    
    for k, v in dict.items():
        if v == 1:
            return k
