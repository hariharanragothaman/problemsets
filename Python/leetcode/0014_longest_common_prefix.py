"""
Problem 14: To find the longest common prefix (LCP):

Write a function to find the longest common prefix strig amongst an array of strings.
If there is no prefix, return an empty string. "".
"""

# This is a very important problem - It has more than 5 ways of solving
# We should learn all the possible ways to do this!


# Solution1: Pythonic Smart Solution

def longestCommonPrefix(stringList):
    print("Function to find the longest common substring")
    prefix_control = list(zip(*stringList))
    prefix = ""
    for data in prefix_control:
        if len(set(data)) == 1:
            prefix += data[0]
        else:
            break
    return prefix

# Solution2: Traditional Method

def longestCommonPrefix2(stringList):
    if stringList == None or len(stringList) ==0:
        return ""
    # Initiating the general scanning.
    for data in range(len(stringList[0])):
        print("The index in check now is:", data)
        c = stringList[0][data]
        print("the prefix control is:", c)
        for elements in range(1, len(stringList)):
            # CORE CHECK!
            if data == (len(stringList[elements])) or stringList[elements][data] != c:
                print ("Entering the if condition")
                return stringList[0][:data]
    return stringList[0] if stringList else ""

stringList = ["flower", "flow", "flight"]
result = longestCommonPrefix(stringList)
result2 = longestCommonPrefix2(stringList)
print(result2)
