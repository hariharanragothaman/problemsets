# Function to get all factors                                                                                           
def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))   

def check_palindrome(num):
    reversed_list = []
    num_list = [ d for d in str(num)]
    for i,e in reversed(list(enumerate(num_list))):
        reversed_list.append(e)
    if reversed_list == num_list:
        return True
    else:
        return False


def check_product(num_list, num):
    for i in num_list:
        for j in num_list:
            if i *j == num:
                print i, j

limit = 1000000
num = 1

big_p = 0

while num < limit:
    if check_palindrome(num):
        print "\nThe number is:", num
        num_factors = factors(num)
        temp_list = []

        for i, e in list(enumerate(num_factors)):
            if len(str(e)) == 3:
                temp_list.append(e)
        print "The interesting factors are:", temp_list
        check_product(temp_list, num)

    num = num+1
print "The big_ps is", big_p
