class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        rlist = []
        arr = sorted(arr, reverse=True)
        print(arr)

        min_difference = 999999        
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) < min_difference:
                min_difference = abs(arr[i]-arr[i-1])
        
        print(min_difference)
        
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) == min_difference:
                rlist.append([arr[i], arr[i-1]])
        
        return sorted(rlist)
