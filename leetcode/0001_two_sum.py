"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        nums.sort()
        print("The numbers are", nums)
        print("The target is:", target)
        
        for x in range(0, len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] + nums[y] == target:
                    return  x,y

if __name__ == '__main__':
    s = Solution()
    nums = [-1, -2, -3, -4, -5]
    target = -8
    indices = s.twoSum(nums,target)
    print("The indices are:", indices)
