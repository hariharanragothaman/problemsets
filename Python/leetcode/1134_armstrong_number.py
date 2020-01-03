"""
Problem 1134: Armstrong Number
@brief: The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.
        Given a positive integer N, return true if and only if it is an Armstrong number.
"""

class Solution:
    def isArmstrong(self, N: int) -> bool:
        number_list = [int(d) for d in str(N)]
        sum = 0 
        k = len(number_list)
        for element in number_list:
            sum += element**k
        if sum == N:
            return True
        return False
