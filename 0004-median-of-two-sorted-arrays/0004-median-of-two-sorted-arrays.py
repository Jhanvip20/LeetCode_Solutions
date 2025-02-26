class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted(nums1 + nums2)
        n = len(merged_array)
        
        if n % 2 == 0:
            mid1, mid2 = n // 2 -1, n // 2
            median = (merged_array[mid1] + merged_array[mid2])/2
        else:
            median = merged_array[n // 2]
        
        return median

        