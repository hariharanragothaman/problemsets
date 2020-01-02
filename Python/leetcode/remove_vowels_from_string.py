"""
LeetCode Problem #1119:
@brief: Remove Vowels from String
"""

class Solution:
    def removeVowels(self, S:str) ->str:
        cmp_list = ['a', 'e', 'i', 'o', 'u']
        input_list = [d for d in S]
        for i, data in list(enumerate(input_list)):
            if data in cmp_list:
                input_list.remove(data)
        return "".join(d for d in input_list)
