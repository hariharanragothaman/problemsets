from itertools import permutations

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if set(nums) == set([0]):
            return '0'
        # This is just converting to strings
        n = list(map(str, nums))
        print(n)
        for i in range(len(n)):
            for j in range(i, len(n)):
                #Here you are appnending and using bubble sort! Holy fuck
                print(n[i] + n[j], (n[j] + n[i]))
                if (n[i] + n[j]) < (n[j] + n[i]):
                    n[i], n[j] = n[j], n[i]
        return ''.join(n)


        """
        Another way to solve the same problem using itertools

        lst = [] 
        for i in permutations(nums, len(nums)): 
        # provides all permutations of the list values, 
        # store them in list to find max 
            lst.append("".join(map(str,i)))  
        return max(lst) 
        """
