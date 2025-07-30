class Solution:
    def longestSubarray(self, nums):
        maxi = max(nums)
        max_len = 0
        length = 0

        for num in nums:
            if num == maxi:
                length += 1
                max_len = max(max_len, length)
            else:
                length = 0

        return max_len