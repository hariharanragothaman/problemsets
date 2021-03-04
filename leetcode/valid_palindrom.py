def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    r_list = [c.lower() for c in s if c.isalpha()]
    t_list = []
    for i, data in reversed(list(enumerate(r_list))):
        t_list.append(data)

    print t_list 
    if r_list == t_list:
        return True
    else:
        return False

s = "0P"
rst = isPalindrome(s)
print rst
