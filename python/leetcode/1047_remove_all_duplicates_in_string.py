"""
Problem 1047: Remove all duplicates in string

Duplicate removal: Choosing 2 adjacent and equal letters and removing them


"""
S = "abbaca"

def removeDuplicates(S):
    """ 
    This logic works but - for very very long strings, the time limit exceeds
    """
    string_list = [char for char in S]
    i = 1
    while i < len(string_list):
        if string_list[i] == string_list[i-1]:
            string_list.pop(i)
            string_list.pop(i-1)
            i = 1
        else:
            i += 1
    return string_list

result = removeDuplicates(S)
print(result)



"""
Intelligent concept oriented solution:
    Use a stack!
    As characters from the string are injected into the stack
    if top of stack; and current character in stream are same; pop the stack!
"""

def removeDuplicates(S):
    stack = []
    for i in range(len(S)):
        if stack and stack[-1] == S[i]:
            stack.pop()
        else:
            stack.append(S[i])
    return "".join(stack)
