"""
Two sum - target problem.
I/P array is sorted

Solution is not zero-based.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Here, we are using the standard 2 pointer method!
        """
        left = 0 
        right = len(numbers)-1
        
        while left < right:
            sum1 = numbers[left] + numbers[right]
            if sum1 == target:
                return [left+1, right+1]
            elif sum1 < target:
                left += 1
            else:
                right -= 1
                    
