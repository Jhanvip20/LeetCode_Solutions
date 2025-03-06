class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n

        # Expected sums
        expected_sum = size * (size + 1) // 2
        expected_sum_sq = size * (size + 1) * (2 * size + 1) // 6

        # Actual sums
        actual_sum = actual_sum_sq = 0
        num_set = set()
        repeated = None

        for row in grid:
            for num in row:
                actual_sum += num
                actual_sum_sq += num * num
                if num in num_set:
                    repeated = num
                num_set.add(num)

        # Compute missing number
        missing = (expected_sum - (actual_sum - repeated))
        
        return [repeated, missing]

