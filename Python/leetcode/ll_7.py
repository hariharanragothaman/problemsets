# Reverse an integer

import math

def reverse(x):

    limit = math.pow(2, 31)
    ll = [x for x in str(x)]
    str_len = len(ll)
    
    if ll[0].isdigit():
        ll = ll[::-1]
        result = ''.join(x for x in ll)
    else: 
        sign = ll[0]
        ll = ll[:-(str_len):-1]
        result = ''.join(x for x in ll)
        result = sign + result

    unsigned  = ''.join(x for x in ll)

    if int(unsigned) > limit: return 0

    # Converting the result back into a list
    rr = [x for x in result]
    flag = 0
    
    if len(ll) == 1:
        res = ''.join(x for x in rr)
        return int(res)

    # Removing all unwanted zero's in the start
    if int(ll[0]) == 0:
        for i in range(len(ll)):
            if int(ll[i]) == 0 and int(ll[i+1]) != 0:
                flag = i+1
                break

    # Modifying the string

    if not rr[0].isdigit():
        q = rr[0] + ''.join(rr[flag+1:])
        return int(q)
    else:
        print "Entered here"
        q = ''.join(rr[flag:]) 
        return int(q)
