class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp_list = list(sorted(nums1 + nums2))
        length = len(temp_list)       
        if length % 2 == 0:
            index1 = length / 2
            index2 = (length / 2) - 1
            return (temp_list[index1] + temp_list[index2] ) / 2.0        
        else:
            index1 = (length//2)
            return temp_list[index1]
