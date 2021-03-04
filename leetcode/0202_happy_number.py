"""
Leetcode Problem 202: Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.


Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""


class Solution:
    def gethappy(self, n: int):
        result_sum = 0 
        num_list = [int(d) for d in str(n)]
        for element in num_list:
            result_sum += element ** 2
        return result_sum
    
    def isHappy(self, n: int) -> bool:
        have_seen_elements = [n]
        current_value = n
        
        while (current_value!=1):
            nexthop = self.gethappy(current_value)
            if nexthop not in have_seen_elements:
                have_seen_elements.append(nexthop)
            elif nexthop in have_seen_elements:
                return False
            current_value = nexthop
        
        return True
