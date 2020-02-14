class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        A.sort()
        min_number = A[0]
        t_list = [int(c) for c in str(min_number)]
        tsum = sum(t_list)
        
        if tsum %2 != 0:
            return 0
        else:
            return 1  
