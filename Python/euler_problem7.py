def check_prime(num):
    if num <=1:
        return False
    if num <=3:
        return True
    if num%2==0 or num%3==0:
        return False

    i = 5
    while num >= (i*i):
        if num%i == 0 or num%(i+2) == 0:
            return False
        i += 6
    return True

p_num = 0 
i = 0

while i <= 10000000:
    if check_prime(i):
        print i
        p_num = p_num + 1
        print "The value of p_num is:", p_num
        if p_num == 10001:
            print "The number is:", i
            break
    i = i + 1
