class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def valid(k: int) -> bool:
            # Create a prefix sum array initialized to zero, size (n + 1)
            pref = [0] * (n + 1)

            # Apply the first 'k' operations from queries to the prefix sum array
            for left, rght, val in queries[:k]:
                pref[left] += val  # Increase value at the starting index
                if rght < n:  
                    pref[rght + 1] -= val  # Decrease value at the end+1 index to mark end of effect

            # Compute prefix sum to determine final modified array
            for i in range(n):
                if nums[i] > pref[i]:  # If the current element is still greater, it's invalid
                    return False
                pref[i + 1] += pref[i]  # Accumulate prefix sum to propagate changes

            return True  # If all elements in `nums` are satisfied, return True
        # Determine the length of `nums` and number of queries
        n, q = len(nums), len(queries)

        # Perform a binary search to find the smallest `k` for which `valid(k) == True`
        idx = bisect_left(range(q + 1), True, key=valid)

        # If the found index `idx` is greater than `q`, return -1 (no valid solution found)
        # Otherwise, return `idx` (smallest valid number of queries needed)
        return -1 if idx > q else idx