class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                continue
            elif neg == 0 and nums[i] > 0:
                return n - i
            elif nums[i] < 0:
                neg += 1
            elif nums[i] > 0:
                return max(neg, n - i)

        return max(neg, 0)