class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen_sum = {0:0}
        total_sum, largest_len = 0, 0
        for i in range(len(nums)):
            total_sum += nums[i]
            if total_sum == k:
                largest_len = i + 1
            else: 
                required = total_sum - k
                if required in seen_sum:
                    largest_len = max(largest_len, i - seen_sum[required])
            if total_sum not in seen_sum:
                seen_sum[total_sum] = i
        return largest_len