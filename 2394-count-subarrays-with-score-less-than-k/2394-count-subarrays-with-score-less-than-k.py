class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        count = s = j = 0
        for i in range(n):
            s += nums[i]
            while s * (i - j + 1) >= k and j <= i:
                s -= nums[j]
                j += 1
            count += i - j + 1
        return count