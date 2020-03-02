def check(my_string):
    brackets = ['()', '{}', '[]']
    while any( x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
    return not my_string

open_list = ['[', '{', '(']
close_list = [']', '}', ')']

def check_paranth(my_string):
    stack = []

    for char in my_string:
        if char in open_list:
            stack.append(char)
        elif char in close_list:
            position = close_list.index(char)
            if len(stack) > 0 and open_list[position] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True

string = '{[]{()}}'
res = check(string)
res2 = check_paranth(string)
print(res)

print(res2)
