class Solution:
    def searchRange(self, nums, target: int):
        ll = []
        first_occurance = self.search_first_k(nums, target)
        ll.append(first_occurance)
        i = first_occurance
        last_occurance = 0
        while i < len(nums):
            if nums[i] != target:
                break
            last_occurance = i 
            i += 1
        ll.append(last_occurance)
        return ll
    
    def search_first_k(self, nums, target: int):
        left, right, result = 0, len(nums)-1, -1
        ll = []
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] == target:
                result = mid
                right = mid -1
            else:
                left = mid +1
        return result

def search_for_first_k(A, k: int) -> int:
    left, right, result = 0, len(A)-1, -1

    while left <= right:
        mid = (left+right)//2
        if A[mid] > k:
            right = mid -1    # here if it's found, the iteration is halved every loop
        elif A[mid] == k:
            result = mid
            right = mid -1
        else: # A[mid] < k
            left = mid+1
    return result

if __name__ == '__main__':
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    B = [2,2]
    f_result = search_for_first_k(A, 108)
    print(f_result)

    s = Solution()
    ll_result = s.searchRange(B, 2)
    print (ll_result)
