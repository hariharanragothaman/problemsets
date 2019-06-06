class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i, data in list(enumerate(nums)):
            if data == val:
                nums.remove(data)
        return len(nums)

# Alternative Solution

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0 
        j = 0 

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


# The best solution
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length  = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                nums[i] = nums[length-1]
                length -- 
            else:
                i += 1 
        return length
