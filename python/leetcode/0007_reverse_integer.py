# Reverse an integer

import math

def reverse(x):

    limit = math.pow(2, 31)
    input_list = [x for x in str(x)]
    length = len(input_list)
    
    if input_list[0].isdigit():
        input_list = input_list[::-1]
        result = ''.join(x for x in input_list)
    else: 
        sign = input_list[0]
        input_list = input_list[:-(length):-1]
        result = ''.join(x for x in input_list)
        result = sign + result


    # SANITY CHECKS - FOR TEST CASES
    unsigned  = ''.join(x for x in input_list)
    if int(unsigned) > limit: return 0

    if len(input_list) == 1:
        res = ''.join(x for x in rr)
        return int(res)

    # Removing unwanted zero's in the start
    rr = [x for x in result]
    flag = 0

    if int(input_list[0]) == 0:
        for i in range(len(input_list)):
            if int(input_list[i]) == 0 and int(input_list[i+1]) != 0:
                flag = i+1
                break

    # Preparing the result
    if not rr[0].isdigit():
        return int(rr[0] + ''.join(rr[flag+1:]))
    else:
        return int(''.join(rr[flag:]))

result = reverse(100)
print(result)
