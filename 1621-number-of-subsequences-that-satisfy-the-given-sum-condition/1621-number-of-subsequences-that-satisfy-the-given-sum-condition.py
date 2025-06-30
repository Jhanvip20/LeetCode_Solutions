class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        # Step 2: Precompute powers of 2
        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % MOD

        # Step 3: Two pointers
        left, right = 0, n - 1
        result = 0

        # Step 4: Use two-pointer approach
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + powers[right - left]) % MOD
                left += 1
            else:
                right -= 1

        # Step 5: Return result
        return result