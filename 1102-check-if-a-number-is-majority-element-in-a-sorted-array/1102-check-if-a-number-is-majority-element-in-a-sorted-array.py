class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        start = bisect_left(nums, target)
        end = bisect_left(nums, target+1)
        n = len(nums)
        if end - start > n/2:
            return True 
        return False 