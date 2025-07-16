from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_count = 0  # Count of odd numbers
        even_count = 0  # Count of even numbers
        odd_even_count = 1  # Length of longest alternating subsequence
        prev = 0  # 0 = odd, 1 = even

        if nums[0] % 2 == 0:
            prev = 1

        for num in nums:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

            if num % 2 == 1 and prev == 1:
                prev = 0
                odd_even_count += 1
            elif num % 2 == 0 and prev == 0:
                prev = 1
                odd_even_count += 1

        return max(odd_count, even_count, odd_even_count)