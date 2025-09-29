class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)
        maxfreq = max(counter.values())
        n = len(nums)
        if maxfreq * k > n:
            return False 
        return True 