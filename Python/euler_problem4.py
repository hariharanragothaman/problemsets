#Check if a number is Palindrome

def check_palindrome():
    num = raw_input()
    reversed_list = []
    num_list = [ d for d in str(num)]
    for i,e in reversed(list(enumerate(num_list))):
        reversed_list.append(e)
    if reversed_list == num_list:
        return True
    else:
        return False
