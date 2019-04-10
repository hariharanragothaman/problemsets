# Reverse an integer

def reverse(x):
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

    print "The initial result is:", result



    # Converting the result back into a list
    rr = [x for x in result]
    flag = 0
    
    if len(ll) == 1:
        return rr

    for i in range(len(ll)):
        if int(ll[i]) == 0 and int(ll[i+1]) != 0:
            flag = i+1
            break
    print "The value of flag is", flag

    if not rr[0].isdigit():
        q = rr[0] + ''.join(rr[flag:])
        print q
        return q
    else:
        q = ''.join(rr[flag:]) 
        print q
        return q


x = 123 * -1
result = reverse(x)
print result
